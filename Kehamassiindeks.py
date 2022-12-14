print("Tere! Olen sinu uus sõber - Python!")
nimi=str(input("Mis su nimi on? "))
print(f"{nimi}, oi kui ilus nimi!")
a=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))

if a==1:
    pikkus=int(input("Mis on sinu pikkus? "))
    mass=float(input("Mis on sinu mass? "))
    if pikkus>100 and pikkus<220 and mass>30 and mass<200:
        indeks=round(mass/(0.01*pikkus)**2)
        print(f"{nimi}! Sinu keha indeks on: {indeks}")
        if indeks<=16:
            print("See on tervisele ohtlik alakaal")
        elif indeks>=16 and indeks<19:
            print("See on alakaal")
        elif indeks>=19 and indeks<25:
            print("See on normaalkaal")
        elif indeks>=25 and indeks<30:
            print("See on ülekaal")
        elif indeks>=30 and indeks<35:
            print("See on rasvumine")
        elif indeks>=35 and indeks<40:
            print("See on tugev rasvumine")
        elif indeks>40:
            print("See on tervisele ohtlik rasvumine")
    else:
        print("Sisestage mõistlikud andmed")
else:
    print("Kahju! See on väga kasulik info!")
    print()
print("Kohtumiseni,{nimi}! Igavesti Sinu, Python!")