import qrcode
import os

def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(fill="black", back_color="white")

    # Ensure 'static' folder exists
    if not os.path.exists("static"):
        os.makedirs("static")

    qr_path = "static/qrcode.jpg"
    qr_image.save(qr_path)

    return qr_path  # Return the file path to be displayed in Flask
