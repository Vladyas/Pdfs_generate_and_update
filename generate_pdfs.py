from config import *

def generate_pdfs(window):
    print(f'spreadsheet_id:{window.treeWidget.currentItem().id}')
    print(f'range:{window.treeWidget.currentItem().text(1) + RANGE}')
    print(f'PDF pattern: {window.pdfPattern.text()}')
    print(f'PDF field: {window.listWidgetPdfFields.currentItem().name}')
    print(f'Number of generated files: {window.copyNumber.text()}')
    print(f'Output dir: {window.outputDir.text()}')