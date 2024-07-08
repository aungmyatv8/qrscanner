from pyzbar import pyzbar
from PIL import Image
print(pyzbar.decode(Image.open('./tele.jpg')))