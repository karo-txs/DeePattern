from dataclasses import dataclass
import toml


@dataclass
class ProjectConfig:
    toml_path: str = None

    def __post_init__(self):
        config_data = toml.load(self.toml_path)
        current_section = None

        for section, entries in config_data.items():
            parts = section.split(".")
            if len(parts) > 1:
                current_section = parts[0]

            if current_section:
                for key, value in entries.items():
                    attr_name = f"{current_section}_{section}_{key}"
                    setattr(self, attr_name, value)
            else:
                for key, value in entries.items():
                    attr_name = f"{section}_{key}"
                    setattr(self, attr_name, value)

    def to_dict(self):
        return {
            name: getattr(self, name) for name in dir(self) if not name.startswith("_")
        }
