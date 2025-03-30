import qrcode
from PIL import Image, ImageDraw, ImageFont
def create_wifi_qr(ssid, password, encryption='WPA'):
    # Create the QR code data string
    qr_data = f"WIFI:S:{ssid};T:{encryption};P:{password};;"
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Create a new image to hold the text and QR code
    img_width, img_height = qr_img.size
    text_height = 40  # Height for the text area
    new_img = Image.new('RGB', (img_width, img_height + text_height), 'white')
    
    # Add the text to the new image
    draw = ImageDraw.Draw(new_img)
    try:
        # Load a font
        font = ImageFont.truetype("arial.ttf", 20)  # Adjust the font size accordingly
    except IOError:
        font = ImageFont.load_default()  # Load default font if the specified font is not found
    
    text = f"SSID: {ssid} PASSWORD: {password}\n"
    text_width, text_height = draw.textsize(text, font=font)
    draw.text(((img_width - text_width) // 2, 10), text, fill="black", font=font)
    # Paste QR code into the new image
    new_img.paste(qr_img, (0, text_height))
    # Save the image
    new_img.save(f"{ssid}_wifi_qr.png")
    print(f"QR Code for Wi-Fi '{ssid}' saved as '{ssid}_wifi_qr.png'.")
# Example usage
if __name__ == "__main__":
    ssid = input("Enter the Wi-Fi SSID: ")
    password = input("Enter the Wi-Fi password: ")
    encryption = input("Enter the encryption type (WPA/WEP): ")
    create_wifi_qr(ssid, password, encryption.upper())