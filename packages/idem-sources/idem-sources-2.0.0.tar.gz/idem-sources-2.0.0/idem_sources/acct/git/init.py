async def gather(hub, profiles):
    """
    Load profiles from local user environment

    If no git profiles were found in the acct_file, profiles will be extrapolated from local ssh keys.

    Example:
    .. code-block:: yaml

        git:
          profile_name:
            username: my_user
            password: my_pass
            branch: main
            ssh_key: >
                -----BEGIN RSA PRIVATE KEY-----
                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX==
                -----END RSA PRIVATE KEY-----
    """
    sub_profiles = {}

    # Use the profiles from an acct_file
    if profiles:
        for profile, ctx in profiles.get("git", {}).items():
            sub_profiles[profile] = ctx

    # If there were no git profiles in the acct_file, use local ssh keys
    else:
        default_idem_profile = hub.OPT.idem.get("acct_profile", hub.acct.DEFAULT)
        sub_profiles[default_idem_profile] = {"placeholder": True}

    return sub_profiles
