from typing import Optional, Any
import os
import requests


class Client:
    def __init__(self) -> None:
        self.api_url = "https://api.notion.com/v1"
        self.api_key = self.load_api_key()

    def load_api_key(self, api_key: Optional[str] = None) -> Optional[str]:
        if api_key:
            return api_key
        else:
            return os.environ.get("NOTION_API_KEY")

    def get_headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

    def get_page(self, page_id: str) -> dict[str, Any]:
        url = self.api_url + f"/pages/{page_id}"
        headers = self.get_headers()
        resp = requests.get(url, headers=headers)
        return resp.json()

    def get_block(self, block_id: str) -> dict[str, Any]:
        url = self.api_url + f"/blocks/{block_id}/"
        headers = self.get_headers()
        resp = requests.get(url, headers=headers)
        return resp.json()

    def get_block_children(self, block_id: str) -> dict[str, Any]:
        url = self.api_url + f"/blocks/{block_id}/children"
        headers = self.get_headers()
        resp = requests.get(url, headers=headers)
        return resp.json()
