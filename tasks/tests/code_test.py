from unittest import TestCase

from tasks import code


class Tests(TestCase):
    def test_google_search(self):
        code._get(
            [
                {
                    "role": "user",
                    "content": 'You are an assistant that writes clever, readable python code.\n\nThe ultimate goal is to write code for this task: Do a google search about dogs\n\nThis is the breakdown of subtasks to accomplish that task: 0: Do a google search about dogs\n\n\nWrite a function for: "Do a google search about dogs".\n\nTo write the function, you must follow the following criteria:\n- Include necessary imports.\n- Consider the output from previous functions.\n- Consider the input of the next task.\n- Your function must return something.\n\nDo it in the following steps:\n1. Explain the function logic.\n2. Write the function code.\n3. Do you need to install any packages from pip? yes/no\n    3.a. If yes, what is the pip install command to install them?\n',
                }
            ]
        )

    def test_ufos(self):
        code._get(
            [
                {
                    "role": "user",
                    "content": 'You are an assistant that writes clever, readable python code.\n\nThe ultimate goal is to write code for this task: Do a Google search about UFOs\n\nThis is the breakdown of subtasks to accomplish that task: 0: Write a function to call an API to do a Google search\n\n\nWrite a function for: "Write a function to call an API to do a Google search".\n\nTo write the function, you must follow the following criteria:\n- Include necessary imports.\n- Consider the output from previous functions.\n- Consider the input of the next task.\n- Your function must return something.\n\nDo it in the following steps:\n1. Explain the function logic.\n2. Write the function code.\n3. Do you need to install any packages from pip? yes/no\n    3.a. If yes, what is the pip install command to install them?\n',
                }
            ]
        )

    def test_visit_website(self):
        code._get(
            [
                {
                    "role": "user",
                    "content": 'You are an assistant that writes clever, readable python code.\n\nThe ultimate goal is to write code for this task: Visit openai.com\n\nThis is the breakdown of subtasks to accomplish that task: 0: Visit openai.com\n\n\nWrite a function for: "Visit openai.com".\n\nTo write the function, you must follow the following criteria:\n- Include necessary imports.\n- Consider the output from previous functions.\n- Consider the input of the next task.\n- Your function must return something.\n\nDo it in the following steps:\n1. Explain the function logic.\n2. Write the function code.\n3. Do you need to install any packages from pip? yes/no\n    3.a. If yes, what is the pip install command to install them?\n',
                }
            ]
        )

    def test_subway(self):
        code._get(
            [
                {
                    "role": "user",
                    "content": 'You are an assistant that writes clever, readable python code.\n\nThe ultimate goal is to write code for this task: Check the next C train arrival at Spring Street\n\nThis is the breakdown of subtasks to accomplish that task: 0: Find an API or data source that provides real-time subway train arrival times for NYC, 1: Write a function to call the API or scrape the data source, 2: Filter the data to find the next C train arrival at Spring Street\n\nThis is the function for the previous task "Write a function to call the API or scrape the data source":\n\nimport requests\n\n\ndef call_subway_api(api_url: str, headers: dict):\n    response = requests.get(api_url, headers=headers)\n    return response.json()\n\n\nWrite a function for: "Filter the data to find the next C train arrival at Spring Street".\n\nTo write the function, you must follow the following criteria:\n- Include necessary imports.\n- Consider the output from previous functions.\n- Consider the input of the next task.\n- Your function must return something.\n\nDo it in the following steps:\n1. Explain the function logic.\n2. Write the function code.\n3. Do you need to install any packages from pip? yes/no\n    3.a. If yes, what is the pip install command to install them?\n',
                }
            ]
        )

    def test_katana(self):
        code._get(
            [
                {
                    "role": "user",
                    "content": "You are an assistant that writes clever, readable python code.\n\nThe ultimate goal is to write code for this task: Check if a reservation is needed for Katana Kitten at this time\n\nThis is the breakdown of subtasks to accomplish that task: 0: Scrape the website of Katana Kitten to find reservation information, 1: Analyze the current time and compare it with the reservation requirements\n\nThis is the function for the previous task \"Scrape the website of Katana Kitten to find reservation information\":\n\nimport requests\nfrom bs4 import BeautifulSoup\n\n\ndef scrape_katana_kitten():\n    # Send a GET request to the website\n    response = requests.get('https://www.katanakitten.com/')\n    \n    # Create a BeautifulSoup object to parse the HTML\n    soup = BeautifulSoup(response.text, 'html.parser')\n    \n    # Find the HTML elements that contain the reservation information\n    reservation_elements = soup.find_all('div', class_='reservation-info')\n    \n    # Extract the necessary information from the reservation elements\n    reservation_info = []\n    for element in reservation_elements:\n        time = element.find('span', class_='reservation-time').text\n        availability = element.find('span', class_='reservation-availability').text\n        reservation_info.append({'time': time, 'availability': availability})\n    \n    return reservation_info\n\n\nWrite a function for: \"Analyze the current time and compare it with the reservation requirements\".\n\nTo write the function, you must follow the following criteria:\n- Include necessary imports.\n- Consider the output from previous functions.\n- Consider the input of the next task.\n- Your function must return something.\n\nDo it in the following steps:\n1. Explain the function logic.\n2. Write the function code.\n3. Do you need to install any packages from pip? yes/no\n    3.a. If yes, what is the pip install command to install them?\n",
                }
            ]
        )

    def test_code(self):
        code._get(
            [
                {
                    "role": "user",
                    "content": 'You are an assistant that writes clever, readable python code.\n\nThe ultimate goal is to write code for this task: Execute the Python code for performing a Google search\n\nThis is the breakdown of subtasks to accomplish that task: 0: Write a function to call Google Search API, 1: Handle the response from the API\n\nThis is the function for the previous task "Write a function to call Google Search API":\n\nimport requests\n\ndef call_google_search_api(query):\n    url = f\'https://www.googleapis.com/customsearch/v1?q={query}\'\n    response = requests.get(url)\n    return response.json()\n\n\nWrite a function for: "Handle the response from the API".\n\nTo write the function, you must follow the following criteria:\n- Include necessary imports.\n- Consider the output from previous functions.\n- Consider the input of the next task.\n- Your function must return something.\n\nDo it in the following steps:\n1. Explain the function logic.\n2. Write the function code.\n3. Do you need to install any packages from pip? yes/no\n    3.a. If yes, what is the pip install command to install them?\n',
                }
            ]
        )

    def test_snl(self):
        code._get(
            [
                {
                    "role": "user",
                    "content": 'You are an assistant that writes clever, readable python code.\n\nThe ultimate goal is to write code for this task: Do a Google search about how to attend SNL\n\nThis is the breakdown of subtasks to accomplish that task: 0: Write a function to call an API to do a Google search, 1: Parse the search results to find relevant information\n\nThis is the function for the previous task "Write a function to call an API to do a Google search":\n\nimport requests\n\ndef google_search(query):\n    url = f\'https://www.googleapis.com/customsearch/v1?q={query}&key=YOUR_API_KEY&cx=YOUR_CX\'\n    response = requests.get(url)\n    data = response.json()\n    return data\n\n\nWrite a function for: "Parse the search results to find relevant information".\n\nTo write the function, you must follow the following criteria:\n- Include necessary imports.\n- Consider the output from previous functions.\n- Consider the input of the next task.\n- Your function must return something.\n\nDo it in the following steps:\n1. Explain the function logic.\n2. Write the function code.\n3. Do you need to install any packages from pip? yes/no\n    3.a. If yes, what is the pip install command to install them?\n',
                }
            ]
        )

    def test_seo(self):
        code._get(
            [
                {
                    "role": "user",
                    "content": "You are an assistant that writes clever, readable python code.\n\nThe ultimate goal is to write code for this task: Visit the article and generate SEO recommendations\n\nThis is the breakdown of subtasks to accomplish that task: 0: Visit the website and scrape the article, 1: Extract the text from the article, 2: Analyze the keyword density in the article, 3: Check for the presence of meta tags, 4: Check for the presence of alt tags in images, 5: Check for the presence of internal and external links, 6: Extract the text content from the website, 7: Analyze the keyword density in the content, 8: Check for the presence of meta tags and alt tags, 9: Check for the presence of internal and external links, 10: Generate recommendations based on the analysis\n\nThis is the function for the previous task \"Visit the website and scrape the article\":\n\nimport requests\nfrom bs4 import BeautifulSoup\n\n\ndef scrape_article(url):\n    # Send a GET request to the website URL\n    response = requests.get(url)\n    \n    # Parse the HTML content of the website\n    soup = BeautifulSoup(response.content, 'html.parser')\n    \n    # Find the article element and extract the text\n    article = soup.find('article')\n    article_text = article.get_text()\n    \n    return article_text\n\n\nWrite a function for: \"Extract the text from the article\".\n\nTo write the function, you must follow the following criteria:\n- Include necessary imports.\n- Consider the output from previous functions.\n- Consider the input of the next task.\n- Your function must return something.\n\nDo it in the following steps:\n1. Explain the function logic.\n2. Write the function code.\n3. Do you need to install any packages from pip? yes/no\n    3.a. If yes, what is the pip install command to install them?\n",
                }
            ]
        )
