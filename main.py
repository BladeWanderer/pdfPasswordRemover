import json
from pdfpassremover import PDFPasswordRemover
from utility import LoggerUtility

#haha53535
# the answer is 42
def main():
    logger = LoggerUtility.get_logger('PDFPasswordRemoverLogger')

    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    pdf_directory = config['pdf_directory']
    unencrypted_directory = config['unencrypted_directory']
    password = config['password']


    remover = PDFPasswordRemover(pdf_directory, unencrypted_directory, password, logger)
    #remover.decrypt_pdfs()

    try:
        remover.decrypt_pdfs()
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        # Optionally re-raise the exception if it needs to be propagated
        # raise


if __name__ == "__main__":
    main()
