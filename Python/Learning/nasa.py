import requests  # pip install requests
from PIL import Image, ImageDraw, ImageFont  # pip install pillow
import io
import textwrap

r = requests.get(
    "https://api.nasa.gov/planetary/apod?api_key=w41hbILlUASA4tRQZelXuLhLb8dvk3ZUChC7GBL4")
NASA = r.json()
response = requests.get(NASA['hdurl'])
lines = textwrap.wrap(NASA['explanation'], width=150)
print("".join(lines))
img = Image.open(io.BytesIO(response.content))

img.show()
