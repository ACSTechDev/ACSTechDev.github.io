#!pip install qrcode

import qrcode

# Data to be encoded in the QR code
data = "https://www.acstech.dev/"

# Create a QR code object
'''
ERROR_CORRECT
Level	Correction	Typical Use
L	    ~7%	        Clean, digital display
M	    ~15%	    General-purpose
Q	    ~25%	    Print with possible smudges
H	    ~30%	    Logos or decorations over the QR
'''
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L, # Error correction level (L, M, Q, H)
    box_size=10, # Size of each box (pixel) in the QR code
    border=4, # Thickness of the border
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code data
# Removing back_color parameter will generate transparent qrcode
#img = qr.make_image(fill_color="black")
img = qr.make_image(fill_color="black", back_color="white")


# Save the image
img.save("my_qrcode.png")

print("QR code generated successfully and saved as my_qrcode.png")

'''
from PIL import Image

# Add logo in the center of the QR code
logo = Image.open("logo.png")
logo.thumbnail((60, 60))
qr_width, qr_height = img.size
pos = ((qr_width - logo.width) // 2, (qr_height - logo.height) // 2)
img.paste(logo, pos, mask=logo)
img.save("my_qrcode_with_logo.png")
'''
