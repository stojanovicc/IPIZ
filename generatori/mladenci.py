import random

vencanje_ids = list(range(1, 301))

imena_mladenci = ["Ana", "Milica", "Jovana", "Marija", "Ivana", "Nikola", "Marko", "Stefan", "Petar", "Luka"]
prezimena_mladenci = ["Petrović", "Jovanović", "Nikolić", "Kovačević", "Stojanović", "Marković", "Đorđević", "Vasić", "Stanković", "Đorđević"]

kontakti_mladenci = ['065', '066', '069', '060', '061', '062', '063', '064']
kontakti_mladenci.extend([f'{prefix}{random.randint(100000, 999999)}' for prefix in kontakti_mladenci])

gradovi = ["Beograd", "Novi Sad", "Niš", "Kragujevac", "Subotica", "Čačak", "Leskovac", "Zrenjanin", "Pančevo", "Kraljevo"]
ulice = ["Bulevar", "Ulica", "Trg", "Aleja", "Naselje", "Prolaz", "Put"]
adrese = [f"{random.choice(gradovi)}, {random.choice(ulice)} {random.randint(1, 100)}"]

for _ in range(300):
    ime_mladosti = random.choice(imena_mladenci)
    prezime_mladosti = random.choice(prezimena_mladenci)
    kontakt_mladosti = random.choice(kontakti_mladenci)
    email_mladosti = f"{ime_mladosti.lower()}.{prezime_mladosti.lower()}@example.com"
    adresa_mladosti = random.choice(adrese)
    vencanje_id = random.choice(vencanje_ids)
    
    ime_mladozenje = random.choice(imena_mladenci)
    prezime_mladozenje = random.choice(prezimena_mladenci)
    kontakt_mladozenje = random.choice(kontakti_mladenci)
    email_mladozenje = f"{ime_mladozenje.lower()}.{prezime_mladozenje.lower()}@example.com"
    adresa_mladozenje = random.choice(adrese)
    
    print(f"INSERT INTO MLADENCI (IME_PREZIME_MLADE, IME_PREZIME_MLADOZENJE, KONTAKT_MLADENACA, EMAIL_MLADENACA, ADRESA_MLADENACA, VENCANJE_ID) VALUES ('{ime_mladosti} {prezime_mladosti}', '{ime_mladozenje} {prezime_mladozenje}', '{kontakt_mladosti}', '{email_mladosti}', '{adresa_mladosti}', {vencanje_id});")
