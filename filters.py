from re import compile
from bs4.element import Tag


def checks_toplevel_tag(source_text_html: str, tag_selector: str) -> bool:
    """
    Verifica se a tag HTML é uma tag especificada.
    :param tag_selector: Seletor tag HTML, por exemplo, "h4"
    :param source_text_html: Código fonte da tag HTML.
    :return: Boleano True caso contenha <h5>... na string.
    """
    tag_pattern = compile(rf'<{tag_selector}>.*')
    return bool(tag_pattern.match(source_text_html))


def check_form_row_tag(document_tag_item: Tag) -> bool:
    """
    Cada elemento de formulário é encadeado com alguma das tags h5, label e span.
    Uma forma de selecionar esses elementos é restrigindo uma lista a apenas elementos que
    contenham essas tags.
    :param document_tag_item: Elemento tag HTML resultado de uma seleção bs4.
    :return: Caso afirmativo
    """
    array = document_tag_item.select('h5, label, span')
    return bool(array)
