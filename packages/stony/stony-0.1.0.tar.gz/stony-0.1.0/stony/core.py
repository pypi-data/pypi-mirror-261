import shutil
import os
import sys
from pathlib import Path
from functools import cache
from jinja2 import FileSystemLoader, Environment
from stony.client import Client
from stony.models import (
    NotionPage,
    RootPage,
    NotionChildPageBlock,
    NotionContentBlock,
)
from stony.config import Config


class Stony:
    def __init__(self, config: Config, client: Client):
        self.client = client
        self.config = config
        self.templates_searchpath = [
            self.config.templates_dir(),
            self.get_default_templates_dir(),
        ]
        self.template_loader = FileSystemLoader(searchpath=self.templates_searchpath)
        self.template_env = Environment(loader=self.template_loader)

    @cache
    def get_page(self, page_id: str) -> NotionPage:
        resp = self.client.get_page(page_id)
        return NotionPage(**resp)

    @cache
    def get_block_children(self, page_id: str) -> list[NotionContentBlock]:
        resp = self.client.get_block_children(page_id)
        blocks = [NotionContentBlock(content=d) for d in resp["results"]]
        return blocks

    @cache
    def get_child_page_blocks(self, page_id: str) -> list[NotionChildPageBlock]:
        return [
            b
            for b in self.get_block_children(page_id)
            if b.content.type == "child_page"
        ]

    def get_root_page(self) -> RootPage:
        page = self.get_page(self.config.root)
        children = self.get_child_page_blocks(self.config.root)
        return RootPage(page=page, children=children)

    def iter_root_child_pages(self, root_page: RootPage):
        for child in root_page.children:
            page = self.get_page(child.id)
            yield page

    def get_default_templates_dir(self):
        module = sys.modules[__name__]
        module_path = os.path.dirname(module.__file__)
        return os.path.join(module_path, "templates")

    def get_template(self, name: str):
        return self.template_env.get_template(name)

    def render_template(self, name, **variables):
        template = self.get_template(name)
        return template.render(**variables, config=self.config)

    def render_index(self, root=None):
        root = root or self.get_root_page()
        return self.render_template("index.html", root=root)

    def build(self, out: Path):
        if os.path.exists(out):
            shutil.rmtree(out)
        os.makedirs(out)
        root = self.get_root_page()
        index = self.render_index(root=root)
        print(out / "index.html")
        with open(out / "index.html", "w") as fh:
            fh.write(index)
        for child in self.iter_root_child_pages(root_page=root):
            page = self.get_page(child.id)
            blocks = self.get_block_children(page.id)
            article = self.render_template("article.html", page=page, blocks=blocks)
            path = out / page.url()[1:]
            print(path)
            with open(path, "w") as fh:
                fh.write(article)
