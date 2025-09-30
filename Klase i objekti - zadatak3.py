# --- Zadatak 3: Recept i Kuharica (Napredni) ---
print("--- Rješenje zadatka 3 ---")

class Recept:
    """Klasa koja modelira recept sa sastojcima."""
    def __init__(self, naziv):
        self.naziv = naziv
        self.sastojci = []

    def dodaj_sastojak(self, sastojak, kolicina):
        """Dodaje sastojak (kao rječnik) u listu sastojaka."""
        self.sastojci.append({'naziv': sastojak, 'količina': kolicina})
        print(f"Dodan sastojak '{sastojak}' u recept '{self.naziv}'.")

    def prikazi(self):
        """Ispisuje naziv recepta i sve njegove sastojke."""
        print(f"\n--- RECEPT: {self.naziv.upper()} ---")
        for sastojak in self.sastojci:
            print(f"- {sastojak['naziv']}: {sastojak['količina']}")
        print("-" * (20 + len(self.naziv)))

class Kuharica:
    """Klasa koja sadrži listu objekata tipa Recept."""
    def __init__(self, naziv):
        self.naziv = naziv
        self.recepti = []

    def dodaj_recept(self, recept_objekt):
        """Dodaje objekt klase Recept u kuharicu."""
        self.recepti.append(recept_objekt)
        print(f"Recept '{recept_objekt.naziv}' dodan u kuharicu '{self.naziv}'.")

    def pronadi_recept(self, naziv_recepta):
        """Pretražuje i prikazuje recept po nazivu."""
        pronaden = False
        for recept in self.recepti:
            if recept.naziv.lower() == naziv_recepta.lower():
                recept.prikazi()
                pronaden = True
                break
        if not pronaden:
            print(f"\nRecept '{naziv_recepta}' nije pronađen u kuharici.")

# Testiranje
# 1. Kreiraj kuharicu
moja_kuharica = Kuharica("Moja najbolja kuharica")

# 2. Kreiraj recepte
palacinke = Recept("Palačinke")
juha = Recept("Juha od rajčice")

# 3. Dodaj sastojke u recepte
palacinke.dodaj_sastojak("Brašno", "250g")
palacinke.dodaj_sastojak("Mlijeko", "500ml")
palacinke.dodaj_sastojak("Jaja", "2 kom")

juha.dodaj_sastojak("Pasirana rajčica", "500g")
juha.dodaj_sastojak("Voda", "500ml")
juha.dodaj_sastojak("Tjestenina za juhu", "50g")

# 4. Dodaj recepte u kuharicu
moja_kuharica.dodaj_recept(palacinke)
moja_kuharica.dodaj_recept(juha)

# 5. Pronađi i prikaži recepte
moja_kuharica.pronadi_recept("Palačinke")
moja_kuharica.pronadi_recept("Juha od rajčice")
moja_kuharica.pronadi_recept("Gulaš") # Recept koji ne postoji

