from unittest import TestCase

from tasks import analyzer


class Tests(TestCase):
    def test_google_search(self):
        analyzer.task_breakdown(
            [{"role": "user", "content": "Task: Do a google search about dogs"}]
        )

    def test_ufos(self):
        analyzer.task_breakdown(
            [{"role": "user", "content": "Task: Do a Google search about UFOs"}]
        )

    def test_visit_website(self):
        analyzer.task_breakdown([{"role": "user", "content": "Task: Visit openai.com"}])

    def test_subway(self):
        analyzer.task_breakdown(
            [
                {
                    "role": "user",
                    "content": "Task: Check the next C train arrival at Spring Street",
                }
            ]
        )

    def test_katana(self):
        analyzer.task_breakdown(
            [
                {
                    "role": "user",
                    "content": "Task: Check if a reservation is needed for Katana Kitten at this time",
                }
            ]
        )

    def test_ad(self):
        analyzer.task_breakdown(
            [
                {
                    "role": "user",
                    "content": "Task: Scrape the website, download all images, pick the best one, create a headline, and edit it to fit 500x600.",
                }
            ]
        )

    def test_code(self):
        analyzer.task_breakdown(
            [
                {
                    "role": "user",
                    "content": "Task: Execute the Python code for performing a Google search",
                }
            ]
        )

    def test_maps(self):
        analyzer.task_breakdown(
            [
                {
                    "role": "user",
                    "content": "Task: Use the Google Maps API to find out when Katana Kitten is open",
                }
            ]
        )

    def test_learn(self):
        analyzer.task_breakdown(
            [
                {
                    "role": "user",
                    "content": "Task: Find the latest Google Calendar documentation, learn how to use it, and make a summary of your calendar.",
                }
            ]
        )

    def test_snl(self):
        analyzer.task_breakdown(
            [
                {
                    "role": "user",
                    "content": "Task: Do a Google search about how to attend SNL",
                }
            ]
        )

    def test_seo(self):
        analyzer.task_breakdown(
            [
                {
                    "role": "user",
                    "content": "Task: Visit the article and generate SEO recommendations",
                }
            ]
        )
