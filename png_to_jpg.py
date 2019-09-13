import PIL
import glob
from PIL import Image

for file in glob.glob("*.jpg"):
    img = Image.open(file)
    rgb_con = img.convert('RGB')
    rgb_con.save(file.replace("jpg","png"),quality =95)