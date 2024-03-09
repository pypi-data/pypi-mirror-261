import logging
import pathlib
from typing import List

from addons_installer import addons_installer
from typing_extensions import Self

from .. import api

_logger = logging.getLogger(__name__)


class AddonsPathConfigSection(api.EnvConfigSection):
    def __init__(self):
        super().__init__()
        self.registry = addons_installer.AddonsFinder()
        self.addons_path: List[str] = []

    def init(self, curr_env: api.Env) -> Self:
        results = addons_installer.AddonsFinder.parse_env(env_vars=curr_env)
        self.addons_path = []
        for result in results:
            path = pathlib.Path(result.addons_path)
            self.addons_path.extend(addons_installer.AddonsFinder.parse_submodule([result]))
            if (path / "EXCLUDE").exists():
                # .odooignore not exclude submodule discover
                # Only exclude this module from the addon-path
                _logger.info("Ignore %s with EXCLUDE file", result.addons_path)
                continue
            self.addons_path.append(result.addons_path)
        return self

    def to_values(self) -> api.OdooCliFlag:
        res = super().to_values()
        res.set("addons-path", self.addons_path)
        return res
