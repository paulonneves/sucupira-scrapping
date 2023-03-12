from bs4.element import ResultSet, Tag
from typing import List, Dict, Tuple
import filters


def tag_comprehension(tag_selector: str, document_collection_tag: ResultSet[Tag], unique: bool = True) -> List[Tag]:
    """
    Extrai uma subseleção de elementos a partir de uma lista de Tags
    :param tag_selector: Seletor tag HTML, por exemplo, "h4"
    :param document_collection_tag: Coleção de tags resultado de uma seleção do bs4
    :param unique: Caso afirmativo é selecionado apenas um elemento, mas caso negativo extende a seleção para vários
    :return: Coleção de Tags
    """
    collection = list()
    for element in document_collection_tag:
        item = element.select_one(tag_selector) if unique else element.select(tag_selector)
        collection.append(item)
    return collection


def text_comprehension(document_collection_tag: ResultSet[Tag]) -> List[str]:
    """
    :param document_collection_tag: Coleção de tags resultado de uma seleção do bs4
    :return: Coleção de textos extraidos de elementos HTML
    """
    collection = list()
    for element in document_collection_tag:
        item = element.text
        collection.append(item)
    return collection


def finds_indexes_each_tag(tag_selector: str, document: ResultSet[Tag]) -> List[int]:
    """
    Encontra os índices de cada Tag especificado encontradas na lista.
    :param tag_selector: Seletor tag HTML, por exemplo, "h4"
    :param document: coleção de elementos HTML (h5 ou div.row).
    :return: coleção com os índices de todos os elementos indexados na lista.
    """
    collection_index = list()

    for index in range(len(document)):
        item = document[index]

        if filters.checks_toplevel_tag(source_text_html=str(item), tag_selector=tag_selector):
            collection_index.append(index)
    return collection_index


def split_sequence_by_index(array: ResultSet[Tag], indexes: List[int]):
    """
    Agrupa as informações das universidades usando cada elemento h5 como separador.
    :param indexes: Coleção de indices de elementos HTML de interesse
    :param array: coleção de elementos HTML (h5 ou div.row)
    :return: Agrupamento [[nome_universidade(h5), atributo(div.row), atributo(div.row), ...], [nome_universidade, ...]]
    """
    group = list()

    for index in range(0, len(indexes), 1):
        if index != len(indexes) - 1:
            group.append(array[indexes[index]: indexes[index + 1]])
        else:
            group.append(array[indexes[index]:])
    return group


def select_label_content_form(document_tag_item: Tag) -> Tuple[str, List[str]]:
    """

    :param document_tag_item:
    :return:
    """
    label = document_tag_item.select_one('label')
    label = label.text.replace(':', '')
    document_collection_content = document_tag_item.select('div span')
    content_collection = text_comprehension(document_collection_content)
    return label, content_collection


def extract_label_content_or_span_from_form(document_list_tag: ResultSet[Tag]) -> Dict[str, str]:
    """
    Extrai o conteúdo de uma lista de um formulário de exibição.
    :param document_list_tag: coleção de elementos HTML [nome_universidade(h5), atributo(div.row), ...].
    :return: dicionário com atributos rótulo e conteúdo.
    """
    document_key_content = dict()
    row_form_collection = filter(filters.check_form_row_tag, document_list_tag)

    for item in row_form_collection:
        item_source = str(item)
        if filters.checks_toplevel_tag(source_text_html=item_source, tag_selector='h5'):
            document_key_content['name'] = item.select_one('span').text
        else:
            label, content = select_label_content_form(item)
            document_key_content[label] = content
    return document_key_content
