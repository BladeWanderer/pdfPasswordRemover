import PyPDF2
import os
import glob

# Original directory containing encrypted PDF files
pdf_directory = '/Users/lenameer/Documents/01_from_last_place/PycharmProjects/pdfPasswordRemover/encrypted'

# New directory for unencrypted files
unencrypted_directory = '/Users/lenameer/Documents/01_from_last_place/PycharmProjects/pdfPasswordRemover/unencrypted'

# Create the directory for unencrypted files if it does not exist
if not os.path.exists(unencrypted_directory):
    os.makedirs(unencrypted_directory)

# Find all PDF files in the original directory
pdf_filenames = glob.glob(os.path.join(pdf_directory, '*.pdf'))

# Loop over each filename
for filename in pdf_filenames:
    try:
        with open(filename, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file, password='5521')

            if not pdf_reader.is_encrypted:
                raise Exception(f"Decryption failed. Check the password for file: {filename}")

            pdf_writer = PyPDF2.PdfWriter()
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            base_name = os.path.basename(filename)
            output_filename = os.path.join(unencrypted_directory, os.path.splitext(base_name)[0] + '_no_pass.pdf')

            with open(output_filename, 'wb') as output_file:
                pdf_writer.write(output_file)

    except Exception as e:
        print("An error occurred:", e)
