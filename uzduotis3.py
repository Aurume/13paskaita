from PIL import Image
import os

aukstis = 1000
logo = Image.open('logo.png')

def tvarkyti_foto(kur, aukstis):
   # logo = Image.open('logo.png')
    #os.chdir(kur)
    #print(os.getcwd())  # isitikinti kad esu tinkamoj direktorijoj
    os.mkdir("sutvarkyta")

fotkes = os.listdir()

for pav in fotkes:
    if pav.endswith((".jpg", ".png")):
        nuotrauka = Image.open(pav)
        nuotrauka = nuotrauka.resize((round(nuotrauka.size[0]/nuotrauka.size[1]*aukstis), aukstis))
        nuotrauka.paste(logo, (nuotrauka.size[0] - logo.size[0], nuotrauka.size[1] - logo.size[1], nuotrauka.size[0], nuotrauka.size[1]), logo)

        pavadinimas = os.path.splitext(pav)[0]
        galune = os.path.splitext(pav)[1]
        nuotrauka.save(f"{pavadinimas}_pakeista{galune}") # pries slash jokiu kitu zenklu, nes viska gadina.
        nuotrauka.show()

tvarkyti_foto(r'C:\Users\aurel\PycharmProjects\pythonProject13', 100)