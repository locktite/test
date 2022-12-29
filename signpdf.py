# digital sign pdf files that stored in /home/user1/pdf/in/ and use pkcs file as certificate 
# and add stamp overlay file called sign.png
#

# Import required libraries
import io
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Define function to digitally sign PDF
def sign_pdf(input_pdf, output_pdf, pkcs_file, sign_image):
    # Read input PDF
    input_pdf = PdfFileReader(open(input_pdf, "rb"))

    # Create output PDF
    output_pdf = PdfFileWriter()

    # Loop through pages of input PDF
    for i in range(input_pdf.getNumPages()):
        # Get page
        page = input_pdf.getPage(i)

        # Create PDF watermark
        packet = io.BytesIO()
        watermark = canvas.Canvas(packet, pagesize=letter)
        watermark.drawImage(sign_image, 0, 0, width=100, height=100, mask='auto')
        watermark.save()

        # Move to beginning of the file
        packet.seek(0)

        # Add watermark to page
        new_pdf = PdfFileReader(packet)
        page.mergePage(new_pdf.getPage(0))

        # Add page to output PDF
        output_pdf.addPage(page)

    # Use PKCS file to digitally sign output PDF
    output_pdf.sign(pkcs_file)

    # Write output PDF to file
    with open(output_pdf_file, "wb") as f:
        output_pdf.write(f)

# Set input directory and output directory
input_dir = "/home/user1/pdf/in/"
output_dir = "/home/user1/pdf/out/"

# Set PKCS file and sign image file
pkcs_file = "pkcs.file"
sign_image = "sign.png"

# Loop through files in input directory
for file in os.listdir(input_dir):
    # Check if file is PDF
    if file.endswith(".pdf"):
        # Set input and output file paths
        input_file = os.path.join(input_dir, file)
        output_file = os.path.join(output_dir, file)

        # Digitally sign PDF
        sign_pdf(input_file, output_file, pkcs_file, sign_image)