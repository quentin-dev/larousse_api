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

        definitions.append(unicodedata.normalize("NFKD", (''.join( definition.find_all(text=True, recursive=False))
                                                            .replace(u'\n',   '')
                                                            .replace(u'\t',   '')
                                                            .replace(u'\r',   ''))))

    for i in range(len(definitions)):
        definitions[i] = definitions[i].strip()

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
        homonyms.append(unicodedata.normalize("NFKD", homonym.select_one('*:first-child').text))

    for i in range(len(homonyms)):
        homonyms[i] = homonyms[i].strip()

    return homonyms
