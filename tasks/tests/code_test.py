from unittest import TestCase

from tasks import code


class TestCode(TestCase):
    def test_google_search(self):
        text = """Here is a python function to do a google search about dogs:

```
def google_search(query):
    from googlesearch import search

    results = []
    for result in search(query, num_results=5):
        results.append(result)

    return results
```

Would you like me to run that for you?
        """
        self.assertEqual(
            code.extract(text),
            """def google_search(query):
    from googlesearch import search

    results = []
    for result in search(query, num_results=5):
        results.append(result)

    return results""",
        )
