from PIL import Image

img = Image.open("kareenaa.jpeg")
print(f"Mode: {img.mode}, Size: {img.size}, Format: {img.format}")