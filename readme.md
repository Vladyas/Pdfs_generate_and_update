![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# PDF files generator and updater project
The project is one window desktop app done with PySide6 and allows a user:
- Login to his Google Drive account
- Select a specific Google Sheet file and worksheet in it.
- Select a template PDF file, which has a set of pdf fields. 
- Select on of the fields 
- Select a directory for PDF files generation
- Input a number PDF files which should be generated

and press **Generate** button.
### What will the app do if press **Generate** button?
- Finds A column in the selected google worksheet
- Prepares a list of uniq values from the selected column. The list will exclude all values, which were used in previous generations. The list of used values is stored in **uniq_numbers.csv** file in the project directory.
- Generates specified number PDF files as:
  * PDF file name is constructed as uniq value from the list + '.pdf'
  * The selected PDF field is initialized with the uniq value used for the file name 

### Requirements

Python 3.9; PySide6

A user should register the app by https://console.cloud.google.com/apis/credentials in order to allow the app communicate with Google Drive services.
- Register the app as Desktop app 
- Download API credentials in json file (with very long name) and rename to **credentials.json**
- Save **credentials.json** to the app directory before the first start.

### License

**MIT**
