from PIL import Image
#use this file if the image is not in RGB or formatted according to the proogram

# Open the image and convert it to RGB format
img = Image.open("Ruchika.jpg").convert("RGB")
img.save("Ruchika.jpg")  # Save the converted image


