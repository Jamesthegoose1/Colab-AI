# plugins/web_prompt.py

import json
import requests
from bs4 import BeautifulSoup
from core.utils import save_text_file

class WebPromptPlugin:
    def __init__(self, json_path="/content/data/datasets/info_sites.json"):
        with open(json_path, "r") as f:
            self.sites = json.load(f)

    def fetch_site_texts(self, category="math_sites"):
        """
        Fetch all text from the URLs in the given category
        """
        urls = self.sites.get(category, [])
        all_texts = []
        for url in urls:
            try:
                response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.text, "html.parser")
                texts = [p.get_text().strip() for p in soup.find_all("p") if p.get_text().strip()]
                all_texts.extend(texts)
            except Exception as e:
                print(f"Failed to fetch {url}: {e}")
        return all_texts

    def save_to_dataset(self, category="math_sites", filename="web_prompts.txt"):
        texts = self.fetch_site_texts(category)
        content = "\n\n".join(texts)
        path = save_text_file(filename, content)
        print(f"Saved {len(texts)} texts to {path}")
        return path
