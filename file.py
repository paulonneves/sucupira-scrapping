import requests
import json
from bs4 import BeautifulSoup


def download_soup(url: str) -> BeautifulSoup | None:
    """
    Verifica se ocorreu tudo OK com a requisição.
    :param url: URL do Sucupira.
    :return: Parser da página BS4.
    """
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        page_content_bs = BeautifulSoup(response.content, 'html.parser')
        return page_content_bs


def save_json(filepath: str, elemento: any):
    with open(filepath, 'w', encoding='utf8') as file:
        json.dump(elemento, file, indent=4, ensure_ascii=False)
