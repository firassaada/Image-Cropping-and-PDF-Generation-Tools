from reportlab.pdfgen import canvas
from PIL import Image

def create_pdf(image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    
    # Get the dimensions of the image
    width, height = image.size
    
    # Choose the appropriate PDF page size based on the image dimensions
    pdf_canvas = canvas.Canvas(output_path, pagesize=(width, height))
    
    # Draw the image onto the PDF canvas, maintaining aspect ratio
    pdf_canvas.drawImage(image_path, 0, 0, width, height, preserveAspectRatio=True)
    
    # Save the PDF
    pdf_canvas.save()
