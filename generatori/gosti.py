import random

imena = ["Ana", "Marko", "Jelena", "Stefan", "Mina", "Nikola", "Sara", "Luka", "Milica", "Vuk"]
prezimena = ["Petrović", "Jovanović", "Nikolić", "Stojanović", "Ilić", "Đorđević", "Kovačević", "Simić", "Stanković", "Marković"]
adrese = ["Knez Mihailova 5", "Cara Dušana 15", "Bulevar Kralja Petra 20", "Trg Republike 10", "Nemanjina 2", "Vuka Karadžića 8"]
kontakti = [str(random.randint(600000000, 699999999)) for _ in range(1000)]  
email_domeni = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]

for _ in range(500):
    ime = random.choice(imena)
    prezime = random.choice(prezimena)
    adresa = random.choice(adrese)
    kontakt = kontakti.pop(random.randint(0, len(kontakti)-1))  
    email_domen = random.choice(email_domeni)
    email = f"{ime.lower()}.{prezime.lower()}@{email_domen}"
    print(f"INSERT INTO GOSTI (IME_GOSTA, PREZIME_GOSTA, ADRESA_GOSTA, KONTAKT_GOSTA, EMAIL_GOSTA) VALUES ('{ime}', '{prezime}', '{adresa}', '{kontakt}', '{email}');")
