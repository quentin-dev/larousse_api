import requests
import unicodedata
from bs4 import BeautifulSoup


def get_definitions(word):
    """
    :param word: The word whose definition you are looking for
    :return: A list containing all the definitions of word
    """

    definitions = []

    url = "https://www.larousse.fr/dictionnaires/francais/" + word.lower()
    soup = BeautifulSoup(requests.get(url=url).text, 'html.parser')

    for definition in soup.select('.Definitions .DivisionDefinition'):
        definitions.append(unicodedata.normalize("NFKD", definition.text))
    
    return definitions

def get_synonyms(word):
    """
    :param word: The word whose synonyms you are looking for
    :return: A list containing all the synonyms of word
    """

    synonyms = []

    url = "https://www.larousse.fr/dictionnaires/francais/" + word.lower()
    soup = BeautifulSoup(requests.get(url=url).text, 'html.parser')

    for synonym in soup.select('.Definitions .DivisionDefinition .Synonymes'):
        synonyms += unicodedata.normalize("NFKD", synonym.text).split('-')
    
    for i in range(len(synonyms)):
        synonyms[i] = synonyms[i].strip()

    return synonyms

def get_homonyms(word):
    """
    :param word: The word whose homonyms you are looking for
    :return: A list containing all the homonyms of word
    """

    homonyms = []

    url = "https://www.larousse.fr/dictionnaires/francais/" + word.lower()
    soup = BeautifulSoup(requests.get(url=url).text, 'html.parser')

    for homonym in soup.select('#homonyme .HomonymeDirects .Homonyme'):
        homonyms.append(unicodedata.normalize("NFKD", homonym.text))

    return homonyms

def get_word_type(word):
    """
    :param word: The word whose type you are looking for
    :return: A string containing the type of word
    """

    url = "https://www.larousse.fr/dictionnaires/francais/" + word.lower()
    soup = BeautifulSoup(requests.get(url=url).text, 'html.parser')
    word_type = unicodedata.normalize("NFKD", soup.select_one('.CatgramDefinition').text).strip()

    return word_type
