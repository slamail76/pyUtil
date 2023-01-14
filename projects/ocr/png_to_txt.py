import pytesseract
from PIL import Image

# Open the image file
image = Image.open('fino0025.png')

# Perform OCR using PyTesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)