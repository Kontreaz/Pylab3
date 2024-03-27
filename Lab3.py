#2️⃣ Napisz skrypt wypełniający tablicę znakami, a następnie wyświetl znaki w kolejności odwrotnej do wprowadzania. Dane wprowadzane z klawiatury.

# Inicjalizacja pustej listy
znaki = []

# Ilość znaków do wprowadzenia
ilosc_znakow = int(input("Podaj ilość znaków do wprowadzenia: "))

# Wprowadzanie znaków
for i in range(ilosc_znakow):
    znak = input(f"Podaj znak nr {i+1}: ")
    znaki.append(znak)

# Wyświetlenie znaków w odwrotnej kolejności
print("Znaki w kolejności odwrotnej:")
for znak in reversed(znaki):
    print(znak)

# 3️⃣ Wypełniający tablicę liczbami losowymi rzeczywistymi z przedziału (-5,5). Wartość tablicy zapisz do pliku result.txt

import random

# Określenie wielkości tablicy
rozmiar_tablicy = 10  # Możesz zmienić na inną wartość odpowiadającą ilości liczb

# Wypełnienie tablicy liczbami losowymi z przedziału (-5,5)
tablica_liczb = [random.uniform(-5, 5) for _ in range(rozmiar_tablicy)]

# Zapisanie wartości tablicy do pliku 'result.txt'
with open('result.txt', 'w') as plik:
    for liczba in tablica_liczb:
        plik.write(f"{liczba}\n")

print("Tablica liczb została zapisana do pliku 'result.txt'.")

# 4️⃣ Napisz funkcję tworzącą tablicę dwuwymiarową (5x5) która zostanie wypełniona kwadratami liczb z komórek z wiersza wcześniejszego. Pierwszy wiersz wypełniony wartościami 2,3,4,5,6. Do utworzenia tablicy dwuwymiarowej wykorzystaj bibiotekę NumPy. Bibliotekę można zainstalować przy pomocy polecenia:

import numpy as np

def stworz_tablice():
    # Tworzenie pustej tablicy 5x5
    tablica = np.zeros((5, 5), dtype=int)

    # Wypełnienie pierwszego wiersza wartościami 2, 3, 4, 5, 6
    tablica[0] = [2, 3, 4, 5, 6]

    # Wypełnianie pozostałych wierszy kwadratami liczb z wiersza poprzedniego
    for i in range(1, 5):
        tablica[i] = tablica[i-1] ** 2

    return tablica

# Utworzenie i wyświetlenie tablicy
tablica_dwuwymiarowa = stworz_tablice()
print(tablica_dwuwymiarowa)

# 5️⃣ Napisz funkcję, która jako parametr przyjmuje lokalizację pliku tekstowego który zawiera dowolny tekst i zwraca histogram znaków występujących w tym napisie (czyli pary znak-liczba wystąpień). Wynikiem powinien być słownik.

def histogram(sciezka_pliku):
    # Inicjalizacja pustego słownika na histogram
    histogram_znakow = {}

    # Otwarcie pliku i przeczytanie zawartości
    with open(sciezka_pliku, 'r', encoding='utf-8') as plik:
        tekst = plik.read()

        # Przejście po każdym znaku w tekście i zaktualizowanie histogramu
        for znak in tekst:
            if znak not in histogram_znakow:
                histogram_znakow[znak] = 1
            else:
                histogram_znakow[znak] += 1

    # Usunięcie znaków białych, jeśli to konieczne
    histogram_znakow.pop('\n', None)
    histogram_znakow.pop(' ', None)

    return histogram_znakow

import os

sciezka_pliku = "document.txt"

# Sprawdzenie, czy plik istnieje
if os.path.isfile(sciezka_pliku):
    print(histogram(sciezka_pliku))
else:
    print(f"Plik {sciezka_pliku} nie istnieje w podanej lokalizacji.")

# 6️⃣ Napisz następujące funkcje niezbędne do implementacji gry w pokera pięciokartowego dobieranego:

import random

def deck():
    ranga = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    kolory = ['trefl', 'karo', 'kier', 'pik']
    return [(rank, suit) for suit in kolory for rank in ranga]

def shuffle_deck(deck):
    shuffled_deck = deck[:]  # Utworzenie kopii talii
    random.shuffle(shuffled_deck)  # Potasowanie talii
    return shuffled_deck

def deal(deck, n):
    return [deck[i*5:(i+1)*5] for i in range(n)]

def sort_cards(cards):
    rank_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    cards.sort(key=lambda card: (rank_order[card[0]], card[1]))
    return cards

# Przykład użycia:
# Utworzenie i potasowanie talii
talia = deck()
talia_potasowana = shuffle_deck(talia)

# Rozdanie kart dla 4 graczy
karty_graczy = deal(talia_potasowana, 4)

for i, karty_gracza in enumerate(karty_graczy, start=1):
    posortowane_karty_gracza = sort_cards(karty_gracza)
    print(f"Gracz {i}: {posortowane_karty_gracza}")
