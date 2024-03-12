import logging
from pathlib import Path
from typing import Dict, List

import tomli
from tox.config.sets import EnvConfigSet
from tox.plugin import impl
from tox.session.state import State
from tox.tox_env.api import ToxEnv
from tox.tox_env.errors import Recreate
from tox.tox_env.python.pip.req_file import PythonDeps

LOGGER = logging.getLogger(__name__)


def split_tox_config_list(config_list: str) -> List[str]:
    """
    Splits a comma- or newline-separated tox config value into a list of
    strings.
    """
    return [x.strip() for x in config_list.split(",") if x.strip()]


def parse_extras_from_pyproject_toml(root: Path) -> Dict[str, PythonDeps]:
    """
    Parse the `[project.optional-dependencies]` section (AKA "extras") from
    `pyproject.toml`.
    """
    with open(root / "pyproject.toml", "rb") as f:
        pyproject_toml = tomli.load(f)
    return {
        k: PythonDeps(raw="\n".join(v), root=root)
        for k, v in pyproject_toml["project"]["optional-dependencies"].items()
    }


@impl
def tox_add_env_config(env_conf: EnvConfigSet, state: State):
    """
    Add the "tox_extras" option to the tox `EnvConfigSet`.
    """
    env_conf.add_config(
        keys=["tox_extras"],
        of_type=List[str],
        default=[],
        desc="extras to install",
        factory=split_tox_config_list,  # type: ignore
    )


@impl
def tox_before_run_commands(tox_env: ToxEnv):
    # infer the root directory from the tox env
    root = tox_env.conf._conf._root

    # parse the extras from pyproject.toml, relative to the root
    extras = parse_extras_from_pyproject_toml(root)

    # a function to install the extras listed in the tox_extras option
    def install_tox_extras():
        for extra in tox_env.conf["tox_extras"]:
            tox_env.installer.install(extras[extra], f"tox_extras_{extra}", "deps")

    try:
        # try to run it once
        install_tox_extras()
    except Recreate as exception:
        # if the deps required by the extras have changed, we will hit this exception
        LOGGER.warning(f"recreate env because {exception.args[0]}")

        # recreate the testenv
        tox_env._clean(transitive=False)
        tox_env._setup_env()
        tox_env._setup_with_env()

        # try installing the extras again
        install_tox_extras()
