import random

stavke_menija = [
    "Pileća čorba", "Cezar salata", "Pizza Margarita", "Pasta Carbonara", 
    "Grilovani biftek", "Pileći file", "Sushi komplet", "Losos na žaru", 
    "Hamburger", "Riblja čorba", "Sote od povrća", "Vegetarijanska pizza", 
    "Tiramisu", "Cheesecake", "Palačinke sa Nutellom", "Čokoladni sufle", 
    "Salata Caprese", "Rižoto sa plodovima mora", "Grčka salata", "Svinjski file"
]

for _ in range(100):
    sadrzaj_menija = random.choice(stavke_menija)
    cena_menija = random.randint(1000, 5000)
    print(f"INSERT INTO MENI (SADRZAJ, CENA_MENIJA) VALUES ('{sadrzaj_menija}', {cena_menija});")
