import PyPDF2
import os
import glob


from functools import wraps
from utility import LoggerUtility

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = LoggerUtility.get_logger("PDFPasswordRemoverLogger")
        try:
            logger.info(f"Starting {func.__name__}")
            result = func(*args, **kwargs)
            logger.info(f"Finished {func.__name__}")
            return result
        except Exception as e:
            #logger.error(f"An error occurred in {func.__name__}: {e}")
            raise Exception("No pdf files in the encrypted folder, please add them and run again")
    return wrapper

# test42

class PDFPasswordRemover:
    def __init__(self, input_dir, output_dir, password, logger):
        self.logger = logger
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.password = password
        self.ensure_input_dir()
        self.ensure_output_dir()

    @log_decorator
    def ensure_input_dir(self):
        if not os.path.exists(self.input_dir):
            os.makedirs(self.input_dir)

    @log_decorator
    def ensure_output_dir(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    @log_decorator
    def decrypt_pdfs(self):
        pdf_filenames = glob.glob(os.path.join(self.input_dir, '*.pdf'))
        if not pdf_filenames:
            raise Exception(f"No PDF files found in the directory: {self.input_dir}")
        for filename in pdf_filenames:
            self.decrypt_each_pdf(filename)

    @log_decorator
    def decrypt_each_pdf(self, filename):
        try:
            with open(filename, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file, password=self.password)

                if not pdf_reader.is_encrypted:
                    raise Exception(f"Decryption failed. Check the password for file: {filename}")

                pdf_writer = PyPDF2.PdfWriter()
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)

                base_name = os.path.basename(filename)
                output_filename = os.path.join(self.output_dir, os.path.splitext(base_name)[0] + '_no_pass.pdf')

                with open(output_filename, 'wb') as output_file:
                    pdf_writer.write(output_file)
                    self.logger.info(f"Successfully decrypted: {filename}")

        except Exception as e:
            print("An error occurred:", e)
