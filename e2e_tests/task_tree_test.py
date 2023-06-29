from unittest import TestCase

from main import Conversation, build_solvable_tree


class Tests(TestCase):
    def test_subway(self):
        build_solvable_tree(
            Conversation([]), "Check the next C train arrival at Spring Street"
        )

    def test_seo(self):
        build_solvable_tree(
            Conversation([]),
            "Visit the article and generate SEO recommendations",
        )

    def test_katana(self):
        build_solvable_tree(
            Conversation([]),
            "Check if a reservation is needed for Katana Kitten at this time",
        )

    def test_ad(self):
        build_solvable_tree(
            Conversation([]),
            "Scrape the website, download all images, pick the best one, create a headline, and edit it to fit 500x600.",
        )

    def test_learn(self):
        build_solvable_tree(
            Conversation([]),
            "Find the latest Google Calendar documentation, learn how to use it, and make a summary of your calendar",
        )

    def test_google(self):
        build_solvable_tree(Conversation([]), "Do a google search about dogs")

    def test_ufos(self):
        build_solvable_tree(Conversation([]), "Do a Google search about UFOs")

    def test_visit(self):
        build_solvable_tree(Conversation([]), "Visit openai.com")

    def test_snl(self):
        build_solvable_tree(
            Conversation([]),
            "Do a Google search about how to attend SNL",
        )

    def test_map(self):
        build_solvable_tree(
            Conversation([]),
            "Use the Google Maps API to find out when Katana Kitten is open",
        )

    def test_weather(self):
        build_solvable_tree(
            Conversation([]),
            "Search for tomorrow's weather forecast",
        )
