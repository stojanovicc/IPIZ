import random

nazivi_torti = [
    "Kinder", "Labudovo jezero", "Čoko Moko", "Puslica", "Banana Split",
    "Jagoda Krem", "Kroasan torta", "Vanila Slatka", "Karamel Fantazija", 
    "Limun kolač", "Krem torta", "Nutella Slatka", "Oreo čudo", 
    "Čokoladna bomba", "Malina Čarolija", "Bela Čokolada", "Lavanda San",
    "Kokos Snovi", "Pistacija Ljubav", "Šumsko Voće", "Medena Kraljica",
    "Tiramisu Sreća", "Koktel Torta", "Španska Klasika", "Jagoda Raj",
    "Lubenica Fantazija", "Jaffa Magic", "Biskvitna Oaza", "Keks Čarolija",
    "Tropska Zabava", "Čokoladna Laguna", "Vanila Uživanje", "Naranča Snova",
    "Mango Raj", "Voćna Salata", "Šumski Plodovi", "Lešnik Čudo",
    "Dinja Osveženje", "Ciklama Ples", "Menta Slatka", "Španska Torta",
    "Kokos Ljubav", "Beli Lava Kolač", "Čokoladna Reka", "Brusnica Čarolija",
    "Kikiriki Snaga", "Trešnja San", "Jogurt Torta", "Crvena Velvet",
    "Karamele Sreće", "Puding Slasno", "Pirinčana Čarolija", "Pirinačni Snovi",
    "Zelena Oaza", "Papaja Uživanje", "Kivi Čudo", "Rum Kolač",
    "Sultan Drupe", "Mint Mojito", "Lubenica Snovi", "Banana Oaza",
    "Mandarina Magija", "Tikva Osveženje", "Šljiva Slasna", "Zvezda Slatkiša",
    "Mango Maska", "Puding Fantazija", "Zeleni Koktel", "Lešnik Uživanje",
    "Pistaći Raj", "Karamel Nostalgija", "Voćna Čarolija", "Šumski Vrt",
    "Ananas Sreća", "Nuga Slatka", "Pirinčana Tama", "Jabuka Slatka",
    "Kafa Torta", "Badem Torta", "Kesten Kolač", "Pistacija Slasna",
    "Višnja Oaza", "Kajsija Klasika", "Slatka Dinja", "Brusnica Blaga",
    "Jagoda Slasna", "Mango Monarh", "Oraščić Kralj", "Pirinačna Osveženje",
    "Vanila Raj", "Borovnica Uživanje", "Lubenica Ljubav", "Limun Raj",
    "Banana Krem", "Kolač od Maline", "Šumska Magija", "Kolač od Jagode",
    "Karamela Uživanje", "Čokoladni Prizor", "Mlečna Čokolada", "Kikiriki Sreća"
]

for _ in range(100):
    naziv_torte = random.choice(nazivi_torti)
    tezina = random.randint(1, 10)
    cena_po_kg = random.randint(500, 1500)
    print(f"INSERT INTO TORTA (NAZIV_TORTE, TEZINA, CENA_PO_KG) VALUES ('{naziv_torte}', {tezina}, {cena_po_kg});")
