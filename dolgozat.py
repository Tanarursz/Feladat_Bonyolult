"""

MINDEN OSZTÁLY MÁSIK python FÁJLBAN LEGYEN


1. JSON adatok létrehozása és betöltése
Feladat:
Készítsd el a játék kezdeti adatait egy JSON fájlban, és töltsd be azokat a programba.

Tennivalók:
Hozz létre egy JSON fájlt, amely tartalmazza:
Harcos adatait: név, életerő, kezdő inventory.
Ellenségek listáját: név, életerő, loot.
A program indításakor olvassa be a JSON adatokat.

---------------------------------------------------------------------------

2. Harcos osztály megírása
Feladat:
Hozd létre a harcost egy Python osztály segítségével, amely tartalmazza az alapvető funkciókat.

Tennivalók:
__init__ metódus: Kezeld a harcos nevét, életerejét és inventory-ját.
tamad metódus: Támadd meg az ellenséget, és csökkentsd annak életerejét.
gyogyulas metódus: Fogyassz inventory-ban lévő gyógyító tárgyakat, amelyek növelik az életerőt.
loot_felvetele metódus: Adj új tárgyat az inventory-hoz az ellenség legyőzése után.

---------------------------------------------------------------------------


3. Ellenség osztály megírása
Feladat:
Hozd létre az ellenségek osztályát, amely lehetővé teszi a harcot a harcos és az ellenség között.

Tennivalók:
__init__ metódus: Kezeld az ellenség nevét, életerejét és lootját.
tamad metódus: Sebezd meg a harcost, ha az ellenség támad.

---------------------------------------------------------------------------


4. Harci mechanizmus megvalósítása
Feladat:
Valósítsd meg a harcot körökre bontva, ahol a harcos és az ellenség váltakozva támadnak.

Tennivalók:
A harcos és az ellenség támadjon egymásra egy körben.
A harcos győz, ha az ellenség életereje 0 vagy kevesebb.
Az ellenség győz, ha a harcos életereje 0 vagy kevesebb.

---------------------------------------------------------------------------


5. Loot rendszer implementálása
Feladat:
Valósítsd meg, hogy az ellenségek lootot ejtenek, amelyet a harcos felvehet.

Tennivalók:
Az ellenség legyőzése után a loot automatikusan bekerül a harcos inventory-jába.
A loot különböző típusú tárgyakat tartalmazhat (pl. gyógyital, pajzs).

---------------------------------------------------------------------------


6. Inventory kezelés
Feladat:
Biztosíts inventory-kezelést a harcos számára.

Tennivalók:
Listázd ki az inventory tartalmát.
Tegyél lehetővé gyógyító tárgyak használatát, amelyek növelik az életerőt.
A tárgyak használat után kerüljenek eltávolításra az inventory-ból.

---------------------------------------------------------------------------


7. Játékvezérlés (interaktív mód)
Feladat:
Tedd a játékot interaktívvá, hogy a játékos döntéseket hozhasson.

Tennivalók:
A játékos választhat, hogy támad, gyógyul, vagy inventory-t kezel.
A választástól függően hajtsa végre a program a megfelelő akciót.

---------------------------------------------------------------------------


8. Játék vége feltételek
Feladat:
Hozz létre feltételeket a játék befejezésére.

Tennivalók:
A játék akkor ér véget, ha:
A harcos életereje 0 vagy kevesebb (veszített).
Minden ellenség legyőzésre került (győzött).
A játék végén jelenítsd meg az eredményt.
Extra: Egyszerű mentés funkció
Feladat:
Adj lehetőséget a játék állapotának mentésére és betöltésére JSON fájl segítségével.

Tennivalók:
A játék során a harcos aktuális állapotát (életerő, inventory) és a legyőzött ellenségeket mentsd el egy külön JSON fájlba.
A játék indításakor olvass be egy mentett állapotot, ha létezik.



"""



import json
import random

#---------------------------------------------------------


class Harcos:
    def __init__(self, nev, hp, inventory=None):
        pass

    def tamad(self, ellenseg):
        pass

    def gyogyulas(self, targy):
        pass

    def loot_felvetele(self, targy):
        pass
    
#---------------------------------------------------------


class Ellenseg:
    def __init__(self, nev, hp, loot):
        pass

    def tamad(self, harcos):
        pass
    
#---------------------------------------------------------
class Loot:
    def __init__(self, nev, tipus, hatas, ritkasag="közönséges"):
        pass
    

    def __str__(self):
        pass

    def hasznal(self, harcos):
        pass




