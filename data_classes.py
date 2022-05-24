class GData:
    def __init__(self):
        self.creds = None
        self.spreadsheet_id = None
        self.sheet_name=''
        self.pdf_pattern_name=''
        self.pdf_field = ''
        self.uniq_vals=None
        self.output_dir=''

if __name__ == '__main__':
    x = GData()
    print(x.__dir__())
    print(x.__getattribute__('creds'))

