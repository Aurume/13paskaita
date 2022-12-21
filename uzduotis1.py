from PIL import Image, ImageEnhance

foto = Image.open("logo.png")
nauja_foto = foto.crop((0, 28, 128, 100))  # tuple masyvo cia reikia, todel dvigubi skliaustai
#nauja_foto = nauja_foto.convert("RGB")
nauja_foto.save("nauja_foto.png") # nepamirsti cia kabuciu!!!!!
#nauja_foto.show()
#print(foto.format, foto.size, foto.mode) # originalo formatas, dydis, tipas
#print(nauja_foto.format, nauja_foto.size, nauja_foto.mode)

#.thumbnail, kitaip miniatiūra, išlaiko proporcijas
#dydis = 128, 128
#foto = Image.open("logo.png")
#foto.thumbnail(dydis)
#foto.show()

# .convert()

#suo = Image.open('dog.jpg')
#suo_bespalvis = suo.convert("L")
#suo_bespalvis.show()

# ImageEnchance modulis

suo = Image.open('dog.jpg')
#enh = ImageEnhance.Contrast(suo) # kontrastas
#enh = ImageEnhance.Color(suo)  # spalvos
#enh = ImageEnhance.Sharpness(suo) # astrumas
#enh = ImageEnhance.Brightness(suo) # ryskumas

#enh.enhance(1.2).show()

#jeigu išsaugoti:
#enh.enhance(1.8).save('bandom.png')

# .transpose - pasukti, paversti

#suo = Image.open("dog.jpg")
#suo.transpose(Image.FLIP_TOP_BOTTOM).show()

# .paste() - uzdeda viena foto ant kitos

#suo = Image.open('dog.jpg')
#foto = Image.open('logo.png')
#logo_location = (0, 0, foto.size[0], foto.size[1]) # uzdejo kairiam kanpe virsuje logo
#suo.paste(foto, logo_location, foto)
#suo.show()


