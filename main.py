import PyPDF2

# Open the PDF file in read-binary mode
with open('07_2023.pdf', 'rb') as file:
    # Initialize PdfReader object with the password
    pdf_reader = PyPDF2.PdfReader(file, password='5521')

    # Check if the PDF is encrypted (to double-check if the password is correct)
    if not pdf_reader.is_encrypted:
        raise Exception("Decryption failed. Check the password.")

    # Now, create a PdfWriter object and add the decrypted pages
    pdf_writer = PyPDF2.PdfWriter()
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)  # Using the updated method name

    # Create a new PDF file with the decrypted content
    with open('unprotected.pdf', 'wb') as output_file:
        pdf_writer.write(output_file)



