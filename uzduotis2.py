# funkcija,  kuri priimtu paveikslėlį
# funkcija, kuri priimtu kontrasto, spalvingumo, aštrumo ir ryškumo reikšmes
# funkcija,  kuri išsaugoti ar ne reikšmę ir  pakoreguotų paveikslėlio nustatymus. Parodytų nuotrauką ekrane.
import os.path
from PIL import ImageEnhance, Image

# Priklausomai nuo pasirinkimo, išsaugotų arba ne.
# Išsaugoti faile, prie originalaus pavadinimo pridėję pvz. '_modified', tarkime dog_modified.jpg.
def super_foto(fotke, kontrastas, spalva, astrumas, ryskumas, ar_noriu_issaugoti=False):
    foto = Image.open(fotke)

    nuotr = ImageEnhance.Contrast(foto) # kontrastas
    foto = nuotr.enhance(kontrastas)

    nuotr = ImageEnhance.Color(foto) # spalva
    foto = nuotr.enhance(spalva)

    nuotr = ImageEnhance.Brightness(foto) # ryskumas
    foto = nuotr.enhance(ryskumas)

    nuotr = ImageEnhance.Sharpness(foto) # astrumas
    foto = nuotr.enhance(astrumas)

    if ar_noriu_issaugoti:
        pavadinimas = os.path.splitext(fotke)[0]
        galune = os.path.splitext(fotke)[1]
        foto.save(f"{pavadinimas}_modified{galune}")
    foto.show()

super_foto('dog.jpg', 3.8, 0.6, 1, 1.2, True) # foto pavad, kontr, spalva, rysk, astr, True/false,saugoti ar ne su modified prierasu?







