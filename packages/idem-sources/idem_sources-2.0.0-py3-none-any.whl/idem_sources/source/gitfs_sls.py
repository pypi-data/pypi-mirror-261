import contextlib
import os
import shutil
import stat
import tempfile
from typing import ByteString
from typing import Dict
from typing import Tuple

import git

# https://pypi.org/project/gitfs2

# This would make an interesting way to do everything in memory only: https://github.com/ElsevierSoftwareX/SOFTX_2018_49


__virtualname__ = "git"


def __init__(hub):
    hub.source.git.ACCT = ["git"]


async def cache(
    hub, ctx, protocol: str, source: str, location: str
) -> Tuple[str, ByteString]:
    """
    Take a file from git and cache it in the target location

    Create a git profile in your acct_file.

    Every parameter for the git profile is optional

    .. code-block:: sls

        git:
          my_profile:
            username: my_user
            password: my_pass
            branch: main
            ssh_key: >
                -----BEGIN RSA PRIVATE KEY-----
                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX==
                -----END RSA PRIVATE KEY-----


    This profile can now be specified for git sources

    .. code-block:: bash

        $ idem state my_source --sls-sources "git+https//my_profile@gitlab.com/vmware/idem/sls.git"
    """
    url = hub.source.git.build_git_url(ctx, protocol=protocol, source=source)
    with hub.source.git.build_ssh_command(ctx) as ssh_command:
        async with hub.source.git.clone(
            ctx, url=url, env={"GIT_SSH_COMMAND": ssh_command}
        ) as local_folder:
            return await hub.source.file.cache(
                ctx=None, protocol="file", source=local_folder, location=location
            )


@contextlib.asynccontextmanager
async def clone(hub, ctx, url: str, env: Dict[str, str]):
    """
    Clone the given url asynchronously
    """
    # Collect other git options
    branch = ctx.acct.get("branch")

    local_folder = await hub.pop.loop.wrap(tempfile.mkdtemp)
    try:
        # Wrap the git command in a ThreadPoolExecutor to run in a separate process
        await hub.pop.loop.wrap(
            _clone_proxy, local_folder=local_folder, url=url, branch=branch, env=env
        )
        yield local_folder
    finally:
        await hub.pop.loop.wrap(shutil.rmtree, local_folder)


def _clone_proxy(local_folder: str, url: str, branch: str, env: Dict[str, str]):
    """
    Provide a single function for the clone operation that can be easily wrapped in a ThreadPoolExecutor
    """
    git_ = git.Git(local_folder)
    git_.update_environment(**env)
    with git.Repo.clone_from(
        to_path=local_folder, url=url, branch=branch, single_branch=True, depth=1
    ):
        return local_folder


@contextlib.contextmanager
def build_ssh_command(hub, ctx) -> str:
    """
    Build the ssh proxy command
    """
    port = ctx.acct.get("port")

    ssh_key_path_or_contents = ctx.acct.get("ssh_key")
    ssh_command = os.environ.get("GIT_SSH_COMMAND", "ssh")
    if port:
        ssh_command += f" -p {port}"

    if ssh_key_path_or_contents:
        if (
            os.path.exists(ssh_key_path_or_contents)
            and os.stat(ssh_key_path_or_contents).st_mode & stat.S_IRUSR
        ):
            # It's a path to an existing file with read permissions
            ssh_key_path = ssh_key_path_or_contents
            ssh_command += f" -i {ssh_key_path}"
        elif "PRIVATE KEY" in ssh_key_path_or_contents:
            # It's the contents of an SSH key
            with tempfile.NamedTemporaryFile() as temp_key_file:
                temp_key_file.write(ssh_key_path_or_contents.encode())
                temp_key_file.flush()
                ssh_key_path = temp_key_file.name
                # Set the permissions of the temporary SSH key file
                os.chmod(ssh_key_path, 0o600)
                ssh_command += f" -i {ssh_key_path}"
                yield ssh_command
                return
        else:
            raise ValueError("Invalid SSH key provided.")

    yield ssh_command
    return


def build_git_url(hub, ctx, protocol: str, source: str) -> str:
    # Build the git url
    # Allow for git+http and git+https
    _, protocol = protocol.split("+", maxsplit=1)
    protocol = protocol or "git"
    username = ctx.acct.get("username", "")
    password = ctx.acct.get("password", "")
    if username:
        login = username
        if password:
            login = f"{username}:{password}"
        url = f"{protocol}://{login}@{source}"
    else:
        if "ssh_key" in ctx.acct or "ssh" in protocol:
            source = f"git@{source}"
        url = f"{protocol}://{source}"
    return url
