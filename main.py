from PIL import Image
me= Image.open()
bg= Image.open()
bg.paste(me, (0,0), me)
bg.show()