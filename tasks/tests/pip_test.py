from unittest import TestCase

from tasks import pip


class TestPip(TestCase):
    def test_google_search(self):
        text = """def google_search(query: str):
    # imports
    from googlesearch import search
    # code
    results = search(query, num=5)
    for result in results:
        print(result)"""
        self.assertEqual(pip.get_packages(text), ["googlesearch-python"])

    def test_requests(self):
        text = """import requests
from bs4 import BeautifulSoup
def get_website_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text(separator='\n').strip()
    text = '\n'.join(line for line in text.split('\n') if line.strip())
    return text"""
        self.assertEqual(pip.get_packages(text), ["requests", "beautifulsoup4"])
