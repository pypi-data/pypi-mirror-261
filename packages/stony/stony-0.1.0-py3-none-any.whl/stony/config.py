from pathlib import Path
from pydantic import BaseModel
from yaml import load as load_yaml, Loader as YamlLoader


class Config(BaseModel):
    project_dir: Path
    root: str
    title: str

    def templates_dir(self):
        return self.project_dir / "templates"


def load_config(project_dir: Path) -> Config:
    with open(project_dir / "stony.yml") as fh:
        conf = load_yaml(fh, Loader=YamlLoader)
    return Config(**conf, project_dir=project_dir)
