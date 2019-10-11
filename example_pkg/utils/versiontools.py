"""Version tools set."""

import os

def get_version_from_scm_tag() -> str:
    """Retrieve the version from SCM tag in Git or Hg."""
    try:
        import setuptools_scm  # only available during setup time

        local_scheme = 'node-and-date'

        is_pypi_upload = os.getenv('PYPI_UPLOAD') == 'true'
        if is_pypi_upload:
            # Cut local version on upload
            local_scheme = lambda version: ''

        return setuptools_scm.get_version(
            root='../..',
            relative_to=__file__,
            local_scheme = local_scheme
        )
    except:
        return 'unknown'


def get_self_version():
    pass
