import random

# Generisanje vrednosti za GOSTI_ID od 1 do 500 i VENCANJE_ID od 1 do 300
gosti_ids = list(range(1, 501))
vencanje_ids = list(range(1, 301))

for vencanje_id in vencanje_ids:
    # Generisanje 200 gostiju za svako venčanje
    for _ in range(200):
        gosti_id = random.choice(gosti_ids)
        print(f"INSERT INTO IMA (GOSTI_ID, VENCANJE_ID) VALUES ({gosti_id}, {vencanje_id});")
