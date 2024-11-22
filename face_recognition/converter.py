from PIL import Image

# Open the image and convert it to RGB format
img = Image.open("kareenaa.jpg").convert("RGB")
img.save("kareena.jpg")  # Save the converted image


