from unittest import TestCase

from tasks import pip


class TestPip(TestCase):
    def test_google_search(self):
        code = """def google_search(query):
    from googlesearch import search

    results = []
    for result in search(query, num_results=5):
        results.append(result)

    return results
        """
        self.assertEqual(pip.get_packages(code), ["googlesearch-python", "google"])
