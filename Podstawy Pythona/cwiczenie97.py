from PIL import Image

nazwaPliku = "Sample.jpg"

image = Image.open(nazwaPliku)

width, height = image.size

print("Szerokość obrazka:",width)
print("Wysokość obrazka:",height)
