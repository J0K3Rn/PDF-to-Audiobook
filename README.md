# PDF-to-Audiobook

Who needs reading anyways? Convert PDF documents to Audiobooks!

How to run:

- Download repository
- Open downloaded repository with a command line interface
- Install Google cloud sdk https://cloud.google.com/sdk/docs/install
- Set up a project and enable Text-to-Speech AI module for your project
- Add your Google cloud credentials to your local cli https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev
- run `pip install google-cloud-texttospeech PyPDF2`
- run `python main.py`
- App window will open prompting you to locate the pdf document you want to convert to a mp3 file
- Generated file will be named output.mp3

Opened file explorer:

![alt text](https://github.com/J0K3Rn/PDF-to-Audiobook/blob/main/screenshots/file_explorer.png?raw=true) 
