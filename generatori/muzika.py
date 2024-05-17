import random

nazivi_bendova = [
    "Magični Mramor", "Vrtlog Senki", "Zvukovi Zvezdane Prašine", 
    "Lutalice iz Luminije", "Eho Nebeskih Talasa", "Sjajni Sokoli", 
    "Aroma Staklenog Srca", "Harmonija Hladnih Plamena", "Vrt Oštrih Misli", 
    "Sanjari sa Saturna", "Misteriozni Mesečari", "Tajanstveni Tvorci", 
    "Duhovi Drevnog Dunava", "Svemirska Sinfonija", "Nebeski Nemiri", 
    "Fantomski Fenjeri", "Zvezdani Zujalci", "Sjajna Senka", 
    "Galaktički Gudači", "Miris Magle", "Zvukovi Zaboravljenih",
    "Pulsirajuće Planete", "Senke Svetlosnih Godina", "Mesečevi Mačevi",
    "Kraljevski Kameni", "Mistični Meteoriti", "Nebeska Noćna Muzika",
    "Holografski Harmonizeri", "Šapat Zvijezda", "Vulkan Vizije",
    "Senke Saturnovog Sjaja", "Zvuci Zalutalih", "Osvetljeni Oblaci",
    "Tajne Tonaliteta", "Svetlost Senzacija", "Nepoznati Napevi"
]

for _ in range(100):
    naziv_benda = random.choice(nazivi_bendova)
    cena_muzike = random.randint(10000, 100000)
    print(f"INSERT INTO MUZIKA (NAZIV_BENDA, CENA_MUZIKE) VALUES ('{naziv_benda}', {cena_muzike});")
