import random

imena_fotografa = ["Lena Canon", "Nikola Kodak", "Ana Leica", "Stefan Fujifilm", "Jelena Olympus", "Marko Pentax"]
cene_fotografa = [3000, 3500, 4000, 4500, 5000]
vreme_slikanja = [2, 3, 4, 5, 6]

for _ in range(100):
    ime_fotografa = random.choice(imena_fotografa)
    cena_fotografa = random.choice(cene_fotografa)
    vreme = random.choice(vreme_slikanja)
    print(f"INSERT INTO FOTOGRAF (FOTOGRAF, CENA_FOTOGRAFA, VREME_SLIKANJA) VALUES ('{ime_fotografa}', {cena_fotografa}, {vreme});")
