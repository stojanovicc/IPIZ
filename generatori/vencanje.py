import random

lokacija_ids = list(range(1, 101))
dekoracija_ids = list(range(1, 101))
torta_ids = list(range(1, 101))
muzika_ids = list(range(1, 101))
fotograf_ids = list(range(1, 101))

for _ in range(300):
    datum_vencanja = f"TO_DATE('{random.randint(2024, 2025)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}', 'YYYY-MM-DD')"
    vreme_pocetka = f"'{random.choice(['12h', '13h', '14h', '15h', '16h']):s}'"
    vreme_zavrsetka = random.randint(13, 17)
    vreme_zavrsetka_str = f"{vreme_zavrsetka if vreme_zavrsetka < 17 else 16}:{random.randint(0, 59):02d}:00"
    
    lokacija_id = random.choice(lokacija_ids)
    dekoracija_id = random.choice(dekoracija_ids)
    torta_id = random.choice(torta_ids)
    muzika_id = random.choice(muzika_ids)
    fotograf_id = random.choice(fotograf_ids)
    print(f"INSERT INTO VENCANJE (DATUM_VENCANJA, VREME_POCETKA, VREME_ZAVRSETKA, LOKACIJA_ID, DEKORACIJA_ID, TORTA_ID, MUZIKA_ID, FOTOGRAF_ID) VALUES ({datum_vencanja}, {vreme_pocetka}, '{vreme_zavrsetka_str}', {lokacija_id}, {dekoracija_id}, {torta_id}, {muzika_id}, {fotograf_id});")
