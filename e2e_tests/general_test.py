from unittest import TestCase

from main import run


class Tests(TestCase):
    def test_google_search(self):
        run(
            [
                {"role": "assistant", "content": "Hi! How can I assist you today?"},
                {"role": "user", "content": "i want to do a google search"},
                {
                    "role": "assistant",
                    "content": "Sure! I can help you with that. Please provide me with the search query you would like to perform on Google.",
                },
                {"role": "user", "content": "dogs"},
            ]
        )

    def test_ufos(self):
        run(
            [
                {"role": "assistant", "content": "Hi! How can I assist you today?"},
                {"role": "user", "content": "are ufos real?"},
                {
                    "role": "assistant",
                    "content": 'The existence of UFOs, or unidentified flying objects, is a topic of debate and speculation. While there have been numerous reports of sightings and encounters, there is no conclusive scientific evidence to prove the existence of extraterrestrial life or advanced alien civilizations visiting Earth. The term "UFO" simply refers to any object in the sky that cannot be identified. It is important to approach this topic with critical thinking and consider the available evidence.',
                },
                {"role": "user", "content": "go a google search"},
            ]
        )

    def test_visit_website(self):
        run(
            [
                {"role": "assistant", "content": "Hi! How can I assist you today?"},
                {"role": "user", "content": "i want you to visit a website for me"},
                {
                    "role": "assistant",
                    "content": "Of course! Please provide me with the website URL you would like me to visit.",
                },
                {"role": "user", "content": "openai.com"},
            ]
        )

    def test_subway(self):
        run(
            [
                {"role": "assistant", "content": "Hi! How can I assist you today?"},
                {
                    "role": "user",
                    "content": "i want to know when the next c train is coming to spring street",
                },
            ]
        )

    def test_katana(self):
        run(
            [
                {"role": "assistant", "content": "Hi! How can I assist you today?"},
                {
                    "role": "user",
                    "content": "i want to know whether i need a reservation for katana kitten at this time",
                },
            ]
        )

    def test_ad(self):
        run(
            [
                {"role": "assistant", "content": "Hi! How can I assist you today?"},
                {"role": "user", "content": "i want to create an ad for my website"},
                {
                    "role": "assistant",
                    "content": "That's great! I can help you with that. Could you please provide me with some details about your website and the type of ad you would like to create?",
                },
                {
                    "role": "user",
                    "content": "i want you to scrape my website, download all images, pick the best one, create a headline and then edit it to fit 500x600",
                },
            ]
        )

    def test_code(self):
        run(
            [
                {"role": "assistant", "content": "Hi! How can I assist you today?"},
                {
                    "role": "user",
                    "content": "i want you to write a python function to do a google search",
                },
                {
                    "role": "assistant",
                    "content": "Sure! Here's a Python function that uses the `googlesearch-python` library to perform a Google search:\n\n```python\nfrom googlesearch import search\n\ndef google_search(query):\n    results = []\n    for result in search(query, num_results=5):\n        results.append(result)\n    return results\n```\n\nYou can use this function by passing your search query as an argument to the `google_search` function. It will return a list of the top 5 search results.",
                },
                {"role": "user", "content": "execute it"},
            ]
        )

    def test_maps(self):
        run(
            [
                {"role": "assistant", "content": "Hi! How can I assist you today?"},
                {
                    "role": "user",
                    "content": "Use the Google Maps API to find out when Katana Kitten is open",
                },
            ]
        )

    def test_learn(self):
        run(
            [
                {"role": "assistant", "content": "Hi! How can I assist you today?"},
                {
                    "role": "user",
                    "content": "i want you to find the latest google calendar documentation, learn how to use it and then make a summary of my calendar",
                },
            ]
        )

    def test_snl(self):
        run(
            [
                {"role": "assistant", "content": "Hi! How can I assist you today?"},
                {"role": "user", "content": "how can i get to attend snl?"},
                {
                    "role": "assistant",
                    "content": "To attend a live taping of Saturday Night Live (SNL), you will need to request tickets directly from the show's ticketing website. Here's how you can do it:\n\n1. Visit the official SNL ticketing website: https://www.nbc.com/tickets/pages/tickets-and-nbc-studio-tour\n2. Check the ticket availability: The website will provide information on upcoming show dates and whether tickets are available.\n3. Submit a ticket request: If tickets are available, you will need to fill out a ticket request form with your personal information, including your name, contact details, and the number of tickets you are requesting.\n4. Wait for confirmation: After submitting your ticket request, you will need to wait for a response from the SNL ticketing team. If your request is approved, you will receive an email with further instructions.\n5. Follow the instructions: The email will provide details on when and where to pick up your tickets, as well as any additional instructions for attending the show.\n6. Attend the show: On the day of the taping, make sure to arrive early and follow the instructions provided to ensure a smooth entry into the studio.\n\nPlease note that SNL tickets are in high demand, and availability is limited. It's recommended to submit your ticket request well in advance and be prepared for the possibility of not securing tickets for your desired date.",
                },
                {"role": "user", "content": "can you google it?"},
            ]
        )

    def test_seo(self):
        run(
            [
                {"role": "assistant", "content": "Hi! How can I assist you today?"},
                {
                    "role": "user",
                    "content": "write an app where i can submit an article on my blog and you give me recommendations for seo",
                },
                {
                    "role": "assistant",
                    "content": "Sure! I can help you with that. To get started, I'll need some more information. \n\n1. What platform or framework are you using to build your blog?\n2. Do you have any specific SEO requirements or guidelines that you follow?\n3. Are there any specific SEO tools or APIs that you would like me to integrate with?\n\nPlease provide as much detail as possible so that I can assist you better.",
                },
                {"role": "user", "content": "can you do everything for me?"},
                {
                    "role": "assistant",
                    "content": "Yes, I can assist you with the SEO recommendations for your blog article. Here's how we can proceed:\n\n1. You can submit your article to me, either by providing the text or sharing a link to the article.\n2. I will analyze the content of the article and provide you with SEO recommendations.\n3. The recommendations may include suggestions for optimizing the title, headings, meta tags, keyword usage, content structure, and more.\n4. I can also provide suggestions for improving the readability, user experience, and overall quality of the article.\n5. Additionally, I can help you with on-page SEO techniques, such as internal linking, image optimization, and URL structure.\n\nPlease provide the article or the link to the article, and I will generate the SEO recommendations for you.",
                },
                {
                    "role": "user",
                    "content": "https://blog.hubspot.com/marketing/how-to-start-a-blog",
                },
            ]
        )

    def test_weather(self):
        run(
            [
                {"role": "assistant", "content": "Hi! How can I assist you today?"},
                {"role": "user", "content": "is it going to rain tomorrow?"},
                {
                    "role": "assistant",
                    "content": "I'm sorry, but as an AI assistant, I don't have access to real-time weather information. However, you can check the weather forecast for tomorrow by using a weather website or app, or by asking a voice assistant like Siri or Google Assistant.",
                },
                {"role": "user", "content": "can you look for it?"},
                {
                    "role": "user",
                    "content": "{'task': \"Search for tomorrow's weather forecast\"}",
                },
            ]
        )
