# pip install qrcode[pil] reportlab

import qrcode
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
# Configuration
labels_per_page = 60
label_width = (2.625/2) * inch  # Width of a label
label_height = 1 * inch      # Height of a label
rows_per_page = 20           # 20 labels per column
cols_per_page = 6            # 6 labels per row
spacing_x = 0.118 * inch     # Horizontal spacing between labels
spacing_y = 0.0 * inch # 0.125 * inch     # Vertical spacing between labels
output_file = "labels.pdf"

def generate_qr_code(data, i):
    """ Generate a QR code image and return its path """
    qr = qrcode.QRCode(version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L ,
        box_size=5, 
        border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_path = f"./img_files/{i}.png"  # Save as PNG using the data index as filename
    img.save(img_path)
    return img_path

def create_labels(data_list):
    """ Create a PDF with QR code labels """
    c = canvas.Canvas(output_file, pagesize=letter)
    
    # Set the position (starting point for labels)
    x_start = 0.13 * inch
    y_start = letter[1] - (0.49 * inch + label_height)
    
    for i, data in enumerate(data_list):
        img_path = generate_qr_code(data, i)  # Generate QR code
        x = x_start + 0.125 * inch + (i % cols_per_page) * (label_width + spacing_x)
        y = y_start - (i // cols_per_page) * (label_height + spacing_y)
        
        # Draw QR code image onto the canvas
        c.drawImage(img_path, x, y, width=label_height, height=label_height)
        # Draw data text below the QR code
        c.setFont("Helvetica", 4)
        c.drawString(x+5, y +1, data)  # Adjusting y for text below the image
    
        # When the last label of the page is reached, create a new page
        if (i + 1) % labels_per_page == 0:
            c.showPage()  # Start a new page
    
    c.save()  # Save the canvas to the file

if __name__ == "__main__":
    # Example data for QR codes
    data_list = [f'http://svpserver5.ddns.net:8082/{i}' for i in range(1, 61)]
    
    # Create labels with the specified data
    create_labels(data_list)
    print(f'Labels have been created and saved as: {output_file}')