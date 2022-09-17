import bs4
import requests
import time
import pandas as pd
from pygame import mixer
import sys


def flat_or_room(place):
    choice = input("Jeśli szukasz mieszkania wybierz 1\nJeśli szukasz pokoju wybierz 2\nMój wybór to: ")

    if choice == '1':
        return "https://www.olx.pl/d/nieruchomosci/mieszkania/wynajem/" + place
    elif choice == '2':
        return "https://www.olx.pl/d/nieruchomosci/stancje-pokoje/" + place
    else:
        print("Nie było takiego wyboru")
        sys.exit(1)


def olx_or_otodom():
    # the first three offers are promoted
    if 'otodom.pl' in soup.select('a.css-1bbgabe')[3]['href']:
        return soup.select('a.css-1bbgabe')[3]['href']
    else:
        return 'http://olx.pl' + soup.select('a.css-1bbgabe')[3]['href']


def alarm_on_or_off():
    choice = input("Czy chcesz włączyć powiadomienia głosowe o nowych ogłoszeniach tak/nie?\nMój wybór to: ")
    if choice.lower() == 'tak':
        return True
    elif choice.lower == 'nie':
        return False
    else:
        print("Nie było takiego wyboru")
        sys.exit(2)


def voice_notification():
    mixer.init()
    alert = mixer.Sound(r'alert.wav')
    alert.play()


city = input("Podaj Miasto. Na przyklad Krakow: ")
max_price = int(input("Podaj maksymalna cene. Na przykład 1200: "))
min_price = int(input("Podaj minimalna cene. Na przykład 500: "))
my_choice = flat_or_room(city)
voice_alert = alarm_on_or_off()
req = requests.get(my_choice)
soup = bs4.BeautifulSoup(req.text, 'lxml')
offer = olx_or_otodom()
print(offer)

while True:
    # refreshing the page
    req = requests.get(my_choice)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    dumpster = olx_or_otodom()
    print(dumpster)
    price = soup.select('.css-wpfvmn-Text.eu5v0x0')[3].text
    price = int(price.replace(' ', '').replace(',', '.').replace('zł', '').replace('donegocjacji', ''))

    if offer != dumpster and max_price >= price >= min_price:
        offer = dumpster
        print(offer)
        if voice_alert:
            voice_notification()

    time.sleep(60)
