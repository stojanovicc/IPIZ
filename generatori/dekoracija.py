import random

cvece = ["Ruže", "Ljiljani", "Tulipani", "Orhideje", "Krizanteme", "Magnolije"]
boje = ["Crvene", "Beli", "Žute", "Roze", "Ljubičaste", "Narandžaste"]
kolicina = [50, 100, 150, 200, 250]
cene_po_komadu = [80, 100, 120, 150, 200]

for _ in range(100):
    naziv_cveca = random.choice(cvece)
    boja = random.choice(boje)
    kolicina_komada = random.choice(kolicina)
    cena_po_komadu = random.choice(cene_po_komadu)
    print(f"INSERT INTO DEKORACIJA (NAZIV_CVECA, BOJA, KOLICINA, CENA_PO_KOMADU) VALUES ('{naziv_cveca}', '{boja}', {kolicina_komada}, {cena_po_komadu});")
