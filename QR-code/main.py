# converting text to QR-code

import qrcode


def generate_qrcode(text):
    qr = qrcode.QRCode(
        version= 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="White", back_color="Black")
    img.save("qrimg.png")

url = input("Url: ")
generate_qrcode(url)