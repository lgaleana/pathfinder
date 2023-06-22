from unittest import TestCase

from tasks import code


class Tests(TestCase):
    def test_google_search(self):
        code.get(
            [
                {
                    "role": "system",
                    "content": "{'task': 'Do a google search about dogs'}",
                },
                {
                    "role": "assistant",
                    "content": "task='Do a google search about dogs' is_atomic=True subtasks=None",
                },
                {
                    "role": "user",
                    "content": "Write a python function for: Do a google search about dogs.",
                },
            ]
        )

    def test_ufos(self):
        code.get(
            [
                {
                    "role": "system",
                    "content": "{'task': 'Do a Google search about UFOs'}",
                },
                {
                    "role": "assistant",
                    "content": "task='Do a Google search about UFOs' is_atomic=True subtasks=None",
                },
                {
                    "role": "user",
                    "content": "Write a python function for: Do a Google search about UFOs.",
                },
            ]
        )

    def test_visit_website(self):
        code.get(
            [
                {"role": "system", "content": "{'task': 'Visit openai.com'}"},
                {
                    "role": "assistant",
                    "content": "task='Visit openai.com' is_atomic=True subtasks=None",
                },
                {
                    "role": "user",
                    "content": "Write a python function for: Visit openai.com.",
                },
            ]
        )

    def test_subway(self):
        code.get(
            [
                {
                    "role": "system",
                    "content": "{'task': 'Check the next C train arrival at Spring Street'}",
                },
                {
                    "role": "assistant",
                    "content": "task='Check the next C train arrival at Spring Street' is_atomic=False subtasks=[SubTask(task='Find a reliable source of real-time train schedules', is_code_solvable=True), SubTask(task='Write a function to scrape or call an API to get the train schedules', is_code_solvable=True), SubTask(task='Filter the schedules for the C train at Spring Street', is_code_solvable=True), SubTask(task='Find the next train arrival from the filtered schedules', is_code_solvable=True)]",
                },
                {
                    "role": "user",
                    "content": "Write a python function for: Find a reliable source of real-time train schedules.",
                },
            ]
        )

    def test_katana(self):
        code.get(
            [
                {
                    "role": "system",
                    "content": "{'task': 'Check if a reservation is needed for Katana Kitten at this time'}",
                },
                {
                    "role": "assistant",
                    "content": "task='Check if a reservation is needed for Katana Kitten at this time' is_atomic=False subtasks=[SubTask(task='Find the official website or a reliable source of information for Katana Kitten', is_code_solvable=True), SubTask(task='Scrape the website or source to find information about reservation requirements', is_code_solvable=True), SubTask(task='Parse the scraped data to determine if a reservation is needed at this time', is_code_solvable=True)]",
                },
                {
                    "role": "user",
                    "content": "Write a python function for: Find the official website or a reliable source of information for Katana Kitten.",
                },
            ]
        )

    def test_ad(self):
        code.get(
            [
                {
                    "role": "system",
                    "content": "{'task': 'Scrape the website, download all images, pick the best one, create a headline, and edit it to fit 500x600.'}",
                },
                {
                    "role": "assistant",
                    "content": "task='Scrape the website, download all images, pick the best one, create a headline, and edit it to fit 500x600.' is_atomic=False subtasks=[SubTask(task='Scrape the website', is_code_solvable=True), SubTask(task='Download all images', is_code_solvable=True), SubTask(task='Pick the best one', is_code_solvable=False), SubTask(task='Create a headline', is_code_solvable=False), SubTask(task='Edit the image to fit 500x600', is_code_solvable=True)]",
                },
                {
                    "role": "user",
                    "content": "Write a python function for: Scrape the website.",
                },
            ]
        )

    def test_code(self):
        code.get(
            [
                {
                    "role": "system",
                    "content": "{'task': 'Execute the Python code for performing a Google search'}",
                },
                {
                    "role": "assistant",
                    "content": "task='Execute the Python code for performing a Google search' is_atomic=False subtasks=[SubTask(task='Install the necessary Python library', is_code_solvable=True), SubTask(task='Write the Python function for performing a Google search', is_code_solvable=True), SubTask(task='Execute the Python function', is_code_solvable=True)]",
                },
                {
                    "role": "user",
                    "content": "Write a python function for: Install the necessary Python library.",
                },
            ]
        )

    def test_maps(self):
        code.get(
            [
                {
                    "role": "system",
                    "content": "{'task': 'Use the Google Maps API to find out when Katana Kitten is open'}",
                },
                {
                    "role": "assistant",
                    "content": "task='Use the Google Maps API to find out when Katana Kitten is open' is_atomic=False subtasks=[SubTask(task='Get API key for Google Maps', is_code_solvable=False), SubTask(task='Write a function to call the Google Maps API', is_code_solvable=True), SubTask(task='Extract opening hours from the API response', is_code_solvable=True)]",
                },
                {
                    "role": "user",
                    "content": "Write a python function for: Write a function to call the Google Maps API.",
                },
            ]
        )

    def test_learn(self):
        code.get(
            [
                {
                    "role": "system",
                    "content": "{'task': 'Find the latest Google Calendar documentation, learn how to use it, and make a summary of your calendar.'}",
                },
                {
                    "role": "assistant",
                    "content": "task='Find the latest Google Calendar documentation, learn how to use it, and make a summary of your calendar.' is_atomic=False subtasks=[SubTask(task='Find the latest Google Calendar documentation.', is_code_solvable=True), SubTask(task='Learn how to use Google Calendar API.', is_code_solvable=False), SubTask(task='Make a summary of your calendar.', is_code_solvable=True)]",
                },
                {
                    "role": "user",
                    "content": "Write a python function for: Find the latest Google Calendar documentation..",
                },
            ]
        )

    def test_snl(self):
        code.get(
            [
                {
                    "role": "system",
                    "content": "{'task': 'Do a Google search about how to attend SNL'}",
                },
                {
                    "role": "assistant",
                    "content": "task='Do a Google search about how to attend SNL' is_atomic=False subtasks=[SubTask(task='Write a function to call a Google Search API', is_code_solvable=True), SubTask(task='Parse the search results to extract relevant information', is_code_solvable=True)]",
                },
                {
                    "role": "user",
                    "content": "Write a python function for: Write a function to call a Google Search API.",
                },
            ]
        )

    def test_seo(self):
        code.get(
            [
                {
                    "role": "system",
                    "content": "{'task': 'Visit the article and generate SEO recommendations'}",
                },
                {
                    "role": "assistant",
                    "content": "task='Visit the article and generate SEO recommendations' is_atomic=False subtasks=[SubTask(task='Fetch the content of the article from the provided URL', is_code_solvable=True), SubTask(task='Parse the content to extract text, headings, meta tags, etc.', is_code_solvable=True), SubTask(task='Analyze the extracted information for SEO optimization', is_code_solvable=True), SubTask(task='Generate SEO recommendations based on the analysis', is_code_solvable=True)]",
                },
                {
                    "role": "user",
                    "content": "Write a python function for: Fetch the content of the article from the provided URL.",
                },
            ]
        )
