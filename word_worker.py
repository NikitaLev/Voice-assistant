import aspose.words as aw
from aspose.words import DocumentBuilder


doc = aw.Document()
builder = aw.DocumentBuilder(doc)


def set_standart_text_style():
    builder.font.size = 12
    builder.font.name = "Arial"


def set_header_text_style():
    builder.font.size = 16
    builder.font.name = "Arial"


def set_dynamic_text_style(size):
    builder.font.size = size
    builder.font.name = "Arial"


def set_standart_paragraph_format():
    builder.paragraph_format.style_identifier = 0
    builder.paragraph_format.first_line_indent = 10
    builder.paragraph_format.alignment = aw.ParagraphAlignment.LEFT
    builder.paragraph_format.keep_together = True


def set_default_paragraph_format():
    builder.paragraph_format.style_identifier = 0
    builder.paragraph_format.first_line_indent = 0
    builder.paragraph_format.alignment = 0
    builder.paragraph_format.keep_together = False


def set_standart_text():
    set_standart_text_style()
    set_standart_paragraph_format()


def set_header_text(header):
    set_header_text_style()
    builder.paragraph_format.first_line_indent = 10 * header
    builder.paragraph_format.alignment = aw.ParagraphAlignment.JUSTIFY
    builder.paragraph_format.style_identifier = header
    builder.paragraph_format.keep_together = False


def create_list():
    builder.list_format.apply_number_default()


def end_list():
    builder.list_format.remove_numbers()


def up_lvl_list():
    builder.list_format.list_indent()


def back_lvl_list():
    builder.list_format.list_indent()


def bage_break():
    builder.insert_break(aw.BreakType.PAGE_BREAK)


def string_writer(str):
    builder.writeln(str)


def start_print():
    builder.insert_table_of_contents("\\o \"1-3\" \\h \\z \\u")
    bage_break()


def save_file():
    doc.update_fields()
    doc.save("out.docx")
    return "файл сохранён"