import json
from pdfpassremover import PDFPasswordRemover
from utility import LoggerUtility

#haha53535
def main():
    logger = LoggerUtility.get_logger('PDFPasswordRemoverLogger')

    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    pdf_directory = config['pdf_directory']
    unencrypted_directory = config['unencrypted_directory']
    password = config['password']


    remover = PDFPasswordRemover(pdf_directory, unencrypted_directory, password, logger)
    remover.decrypt_pdfs()

if __name__ == "__main__":
    main()
