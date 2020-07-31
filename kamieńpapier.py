from random import randint
o = ["papier", "kamień", "nożyce"] #opcje
gracz = False #warunek
komputer = o[randint(0,2)] #losowanie
gracz = input("kamień, papier, nożyce?") #wprowadzanie
print(gracz, "vs", komputer) #informacja dla użytkownika
if gracz == komputer: #pętla
        print('remis')
elif gracz == "kamień":
    if komputer == "papier":
        print("papier pokrywa kamień, przegrałeś!")
    if komputer == "nożyce":
        print("kamień bije nożyczki, wygrałeś!")
elif gracz == "papier":
    if komputer == "kamień":
        print("papier kryje kamień, wygrałeś!")
    if komputer == "nożyce":
        print("nożyce rozcinają papier, przegrałeś!")
elif gracz == "nożyce":
    if komputer == "kamień":
        print("kamień niszczy nożyczki, przegrałeś!")
    if komputer == "papier":
        print("nożyce rozcinają papier, wygrywasz!")
else:
    print("to nie jest opcja!")