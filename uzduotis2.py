# funkcija,  kuri priimtu paveikslėlį
# funkcija, kuri priimtu kontrasto, spalvingumo, aštrumo ir ryškumo reikšmes
# funkcija,  kuri išsaugoti ar ne reikšmę ir  pakoreguotų paveikslėlio nustatymus. Parodytų nuotrauką ekrane.
import os.path
from PIL import ImageEnhance, Image

#path = 'C:\Users\aurel\PycharmProjects\pythonProject13'
# Priklausomai nuo pasirinkimo, išsaugotų arba ne.
# Išsaugoti faile, prie originalaus pavadinimo pridėję pvz. '_modified', tarkime dog_modified.jpg.
def super_foto(fotke, kontrastas, spalva, astrumas, ryskumas, save=False):
    foto = Image.open(fotke)

    nuotr = ImageEnhance.Contrast(foto) # kontrastas
    foto = nuotr.enhance(kontrastas)

    nuotr = ImageEnhance.Color(foto) # spalva
    foto = nuotr.enhance(spalva)

    nuotr = ImageEnhance.Brightness(foto) # ryskumas
    foto = nuotr.enhance(ryskumas)

    nuotr = ImageEnhance.Sharpness(foto) # astrumas
    foto = nuotr.enhance(astrumas)

    if save:
        loc = os.path.splitext(fotke)[0] # kodel cia taip rasom?
        ext = os.path.splitext(fotke)[1] #ir cia?
        foto.save(f"{loc}_modified{ext}")
    foto.show()

super_foto('dog.jpg', 2, 0.6, 1, 1.2, True) # foto pavad, kontr, spalva, rysk, astr, True/false,saugoti ar ne su modified prierasu?







