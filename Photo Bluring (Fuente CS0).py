from PIL import Image, ImageFilter

before=Image.open("casaokis.png")
after =before.filter(ImageFilter.BoxBlur(1))
after.save("casablur.png")