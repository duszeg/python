from PIL import Image
from io import BytesIO
from PyPDF2 import PdfFileWriter, PdfFileReader

def jpg_to_pdf(jpg_path, pdf_path):
    # Open the JPG image using PIL
    with Image.open(jpg_path) as img:
        # Create a PDF writer
        pdf_writer = PdfFileWriter()

        # Convert the image to PDF
        with BytesIO() as f:
            img.save(f, format='PDF')
            pdf_writer.addPage(PdfFileReader(f).getPage(0))

        # Write the PDF to a file
        with open(pdf_path, 'wb') as f:
            pdf_writer.write(f)

# Usage example
jpg_to_pdf('image.jpg', 'image.pdf')
