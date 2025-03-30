import qrcode
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
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(f"{ssid}_wifi_qr.png")
    print(f"QR Code for Wi-Fi '{ssid}' saved as '{ssid}_wifi_qr.png'.")
# Example usage
if __name__ == "__main__":
    ssid = input("Enter the Wi-Fi SSID: ")
    password = input("Enter the Wi-Fi password: ")
    encryption = input("Enter the encryption type (WPA/WEP): ")
    create_wifi_qr(ssid, password, encryption.upper())