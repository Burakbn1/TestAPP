from PIL import Image

def image_rotate(img_path):

    img= Image.open(img_path)

    img= img.rotate(angle=270, expand=True)

    img.save(img_path)