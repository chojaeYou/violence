
import base64
def divide(imgstring):
    imgdata = base64.b64decode(imgstring)
    filename = 'image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
