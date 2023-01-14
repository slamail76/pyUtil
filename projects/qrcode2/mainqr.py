import os
import qrcode
from PIL import Image


VCARD = """
BEGIN:VCARD
VERSION:3.0
FN;CHARSET=UTF-8:John Smith
N;CHARSET=UTF-8:smith;john;;mr;
EMAIL;CHARSET=UTF-8;type=HOME,INTERNET:home@textilecompany.com
TEL;TYPE=HOME,VOICE:+4472928372
ROLE;CHARSET=UTF-8:ceo
ORG;CHARSET=UTF-8:Textile Company
REV:2023-07-05T15:03:18.704Z
END:VCARD
"""

def create_qr_code(content: str,  output_path: str):
    # create qrcode image
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_H,
    box_size=10,
    border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    # resize logo
    """logo = Image.open(logo_path).convert("RGBA")
    logo_width, logo_height = logo.size
    img_width, img_height = img.size
    scale_factor = min(img_width // 3, img_height // 3, logo_width, logo_height)
    logo.thumbnail((scale_factor, scale_factor))
    logo_pos = ((img_width - logo.width) // 2, (img_height - logo.height) // 2)

    logo_no_alpha = Image.new("RGB", logo.size, (255, 255, 255))
    logo_no_alpha.paste(logo, mask=logo.split()[3])

    # position logo
    img.paste(logo_no_alpha, logo_pos, mask=logo.split()[3])"""

    # save image
    img.save(output_path)


if __name__ == "__main__":
    create_qr_code(VCARD,  "qrcode_with_logo.png")