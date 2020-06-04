#Image Processing

from PIL import Image, ImagePath, ImageDraw
import sys
#import pillow

try:
    tatras = Image.open('C:\\Users\\Ashish\\Desktop\\SkillUpgrade\\python_ML_Project\\Test.jpg')
   

except IOError:
    print("Unable to load image")
    sys.exit(1)
tatras.show()

box = (100, 100, 400, 400)
region = tatras.crop(box)
region = region.transpose(Image.ROTATE_180)
region.show()

