import requests
import re
from bs4 import BeautifulSoup


def get_definitions(word):
    """
    :param word: The word whose definition you are looking for
    :return: A list containing all the definitions of word
    """
    url = "https://www.larousse.fr/dictionnaires/francais/" + word.lower()
    print(url)
    soup = BeautifulSoup(requests.get(url=url).text, 'html.parser')
    for ul in soup.find_all('ul'):
        if ul.get('class') is not None and 'Definitions' in ul.get('class'):
            return [re.sub("<.*?>", "", str(li)) for li in ul.find_all('li')]
    return []