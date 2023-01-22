"""AWS Lambda to create QR codes with centered logo.
"""
from __future__ import annotations
import logging
import sys

import qrcode
#from PIL import Image

def create_qr(url:str) -> qrcode.image.pil.PilImage | None:
    """Takes an http URL and returns a high error correction
    QR code. Version is forced to enforce size. Returns None
    if an error occurs.
    """
    qr_code = qrcode.QRCode(
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
            )
    qr_code.add_data(url)
    try:
        qr_code.make(fit=False)
    except qrcode.exceptions.DataOverflowError:
        logging.error("URL is too long.")
        return None
    img = qr_code.make_image(fill_color="black", back_color="white")
    return img

def main() -> None:
    """Create a QR code and saves it to qr.png.
    """
    img = create_qr(url)
    if not img:
        logging.error("No QR code image was created.")
        sys.exit(1)

    img.save("qr.png")

if __name__ == "__main__":
    main()
