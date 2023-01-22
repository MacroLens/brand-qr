"""AWS Lambda to create QR codes with centered logo.
"""
from __future__ import annotations
import logging
import sys

import qrcode
from PIL import Image

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

def paste_centered(bg:Image, fg:Image) -> Image:
    """takes fg and centers it on bg.
    Assumes that bg has larger or equal dimensions than fg
    Returns a new Image
    """
    bg = bg.copy()
    fg = fg.copy()
    bg_width, bg_height = bg.size
    fg_width, fg_height = fg.size

    offset = ((bg_width - fg_width)//2,
              (bg_height - fg_height)//2)
    
    bg.paste(im=fg, box=offset, mask=fg)
    return bg

def place_logo(qr_code:Image, logo:Image, logo_scale:float=0.4) -> Image:
    """Creates a composite image of the qr_code and logo.
    Creates copies of images and does not transform original.
    The logo will be scaled to logo_scale*qr_code.size.
    Expects that both images can be converted to RGBA.
    Expects that qr_code and logo are square.
    """
    qr_code = qr_code.copy()
    qr_code = qr_code.convert(mode="RGBA")
    logging.debug("QR_Code size {}".format(qr_code.size))

    logo = logo.copy()
    logo = logo.convert(mode="RGBA")
    logo = logo.resize(tuple(int(dim*logo_scale) for dim in qr_code.size))

    transparent = Image.new(mode="RGBA", size=qr_code.size, color="#00000000")
    resized_logo = paste_centered(transparent, logo)
    logging.debug("Logo size {}".format(logo.size))
    logging.debug("Logo size {}".format(logo.mode))
    qr_code.paste(im=resized_logo, mask=resized_logo)

    return qr_code

def main() -> None:
    """Create a QR code and saves it to qr.png.
    """
    url="http://youtube.com"
    logging.basicConfig(level=logging.DEBUG)
    img = create_qr(url)
    if not img:
        logging.error("No QR code image was created.")
        sys.exit(1)
    img = img.copy() # Explicit way of casting to PIL Image
    with Image.open("logo.png") as logo:
        qr_code = place_logo(img,logo)
        qr_code.save("qr.png")

if __name__ == "__main__":
    main()
