from config import *
from csv_get_update import get_uniq_numbers, update_uniq_numbers
from get_google_data import get_sheet_range
from PyPDF2 import PdfFileReader, PdfFileWriter


def generate_pdfs(gdata, progress_bar = None):
    strings_from_file = get_uniq_numbers(FILE_UNIQ_NUMBERS)
    ustrings = sorted(get_sheet_range(gdata.creds, gdata.spreadsheet_id, gdata.range) \
                      - strings_from_file)
    if len(ustrings) >= gdata.files_amount:
        if progress_bar:
            progress_bar.reset()
            progress_bar.setMinimum(1)
            progress_bar.setMaximum(gdata.files_amount+1)
        for count, i in enumerate(ustrings[:gdata.files_amount]):
            reader = PdfFileReader(gdata.pdf_pattern_name)
            writer = PdfFileWriter()
            pages = reader.pages
            # TODO написать генерацию для всех PDF страниц а не только для 1-ой.
            #  Кстати, если поле не на первой стрранице, придётся переписывать ListWidget (добавить инфо о странице)
            #  и потом учитывать это при генерации, на какой странице вставлять данные
            page = pages[0]
            fields = reader.getFields()
            writer.addPage(page)
            with open(f"{gdata.output_dir}/{i}.pdf", "wb") as output_stream:
                writer.updatePageFormFieldValues(page, {gdata.pdf_field: i})
                writer.write(output_stream)
            if progress_bar: progress_bar.setValue(count+1)

        update_uniq_numbers(FILE_UNIQ_NUMBERS, set(ustrings[:gdata.files_amount]) | strings_from_file)
        if progress_bar: progress_bar.setValue(count + 2)
        return True, f"Сгенерировано файлов: {gdata.files_amount} "
    else:
        return False, "Число файлов больше количества уникальных номеров"
if __name__ == '__main__':
    pass


