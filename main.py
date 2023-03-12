from file import download_soup, save_json
from select import (
    extract_label_content_or_span_from_form,
    finds_indexes_each_tag,
    split_sequence_by_index)

soup = download_soup("https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/programa/viewPrograma.jsf?popup"
                     "=true&cd_programa=53045009001P3")

sections = soup.select(".conteudo-container .conteudo fieldset")
fieldset_admin_program = extract_label_content_or_span_from_form(sections[0].select('.row'))
fieldset_course = extract_label_content_or_span_from_form(sections[2].select('.row'))

fieldset_university_content = sections[1].select('h5, .row')
fieldset_university_indexes = finds_indexes_each_tag('h5', fieldset_university_content)
fieldset_university_map_index = split_sequence_by_index(fieldset_university_content, fieldset_university_indexes)
fieldset_university_map_object = list(map(extract_label_content_or_span_from_form, fieldset_university_map_index))

print(fieldset_admin_program)
print(fieldset_course)
print(fieldset_university_map_object)

save_json('output/basic_program.json', fieldset_admin_program)
save_json('output/course.json', fieldset_course)
save_json('output/university.json', fieldset_university_map_object)
