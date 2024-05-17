import random

nazivi_lokacija = ["Restoran Dunav", "Vila Panorama", "Pansion Sunčani Breg", "Hotel Park", "Sala Bela Vista", "Etno selo Drinska kuća"]
adrese_lokacija = ["Bulevar Cara Lazara 15", "Jovana Cvijića 10", "Kneza Miloša 20", "Nemanjina 5", "Trg Republike 3", "Braće Jugovića 8"]
kontakti_lokacija = ["0641234567", "0652345678", "0663456789", "0634567890", "0625678901", "0616789012"]
email_domeni_lokacija = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
cena_iznajmljivanja = [2000, 2500, 3000, 3500, 4000]
cena_usluge = [500, 1000, 1500, 2000, 2500]

for meni_id in range(1, 101):
    naziv_lokacije = random.choice(nazivi_lokacija)
    adresa_lokacije = random.choice(adrese_lokacija)
    kontakt_lokacije = random.choice(kontakti_lokacija)
    email_lokacije = f"{naziv_lokacije.lower().replace(' ', '_')}_{meni_id}@{random.choice(email_domeni_lokacija)}"
    cena_iznajmljivanja_lokacije = random.choice(cena_iznajmljivanja)
    cena_usluge_lokacije = random.choice(cena_usluge)
    print(f"INSERT INTO LOKACIJA (NAZIV_LOKACIJE, ADRESA_LOKACIJE, KAPACITET, KONTAKT_LOKACIJE, EMAIL_LOKACIJE, CENA_IZNAJMLJIVANJA, CENA_USLUGE, MENI_ID) VALUES ('{naziv_lokacije}', '{adresa_lokacije}', {random.randint(50, 200)}, '{kontakt_lokacije}', '{email_lokacije}', {cena_iznajmljivanja_lokacije}, {cena_usluge_lokacije}, {meni_id});")
