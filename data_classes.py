class GData:
    def __init__(self):
        self.creds = None
        self.spreadsheet_id = None
        self.range=''
        self.pdf_pattern_name=''
        self.pdf_field = ''
        self.files_amount=None
        self.output_dir=''

if __name__ == '__main__':
    x = GData()
    print(x.__dir__())
    print(x.__getattribute__('creds'))

