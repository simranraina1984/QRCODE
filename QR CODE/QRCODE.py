import qrcode
from PIL import Image, ImageDraw

data = "https://results.vtu.ac.in/"  # The data you want to encode in the QR code

# Create an instance of the QRCode class
qr = qrcode.QRCode(
    version=1,  # QR code version (integer from 1 to 40, higher means more data capacity)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H)
    box_size=10,  # Size of each box (in pixels)
    border=4,  # Size of the border (in boxes)
)

# Add the data to the QR code
qr.add_data(data)

# Generate the QR code
qr.make(fit=True)

# Create an image from the QR code
image = qr.make_image(fill_color="black", back_color="white")

# Convert the image to RGBA
image = image.convert("RGBA")

# Create a circular mask
mask = Image.new("L", image.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)

# Apply the mask to the QR code image
masked_image = Image.new("RGBA", image.size)
masked_image.paste(image, (0, 0), mask=mask)

# Save the masked image or display it
masked_image.save("qr_code_circle.png")  # Save the image to a file
masked_image.show()  # Display the image
