"""
A module responsible for calculating expected and skipped variations from
`conf/variations` yaml file and convert them into processable list
"""
from functools import cached_property
from pathlib import Path

import yaml


class Variations:
    def __init__(self, settings):
        self.settings = settings

    def get_paths(self, variations, prefix="", separator="/"):
        paths = []
        if isinstance(variations, dict):
            for key, value in variations.items():
                paths.extend(self.get_paths(value, f"{prefix}{key}{separator}"))
        elif isinstance(variations, list):
            for item in variations:
                paths.extend(self.get_paths(item, prefix, separator))
        else:
            paths.append(f"{prefix}{variations}")

        return paths

    @cached_property
    def variations(self):
        templates_path = Path(self.settings.candore.var_file)
        if not templates_path.exists():
            print(f"The file {templates_path} does not exist.")
        with templates_path.open() as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
        return yaml_data

    @cached_property
    def expected_variations(self):
        return self.get_paths(variations=self.variations.get("expected_variations"))

    @cached_property
    def skipped_variations(self):
        return self.get_paths(variations=self.variations.get("skipped_variations"))
