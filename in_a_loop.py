import PyPDF2
import os

# List of PDF filenames to process
pdf_filenames = ['11_2022.pdf', '12_2022.pdf', '11_2023.pdf']

# Loop over each filename
for filename in pdf_filenames:
    try:
        # Open the current PDF file in read-binary mode
        with open(filename, 'rb') as file:
            # Initialize PdfReader object with the password
            pdf_reader = PyPDF2.PdfReader(file, password='5521')

            # Check if the PDF is encrypted
            if not pdf_reader.is_encrypted:
                raise Exception("Decryption failed. Check the password for file:", filename)

            # Create a PdfWriter object and add the decrypted pages
            pdf_writer = PyPDF2.PdfWriter()
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            # Create a new filename for the output
            output_filename = os.path.splitext(filename)[0] + '_no_pass.pdf'

            # Create a new PDF file with the decrypted content
            with open(output_filename, 'wb') as output_file:
                pdf_writer.write(output_file)

    except Exception as e:
        print("An error occurred:", e)
