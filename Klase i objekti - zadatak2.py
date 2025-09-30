# Zadatak 2: Bankovni račun

class BankovniRacun:
    """Klasa koja modelira jednostavan bankovni račun."""
    def __init__(self, ime_prezime, broj_racuna):
        """Konstruktor za BankovniRačun."""
        self.ime_prezime = ime_prezime
        self.broj_racuna = broj_racuna
        self.stanje = 0.0

    def uplati (self, iznos):
        """Metoda za uplatu novca na račun."""
        if iznos > 0:
            self.stanje += iznos
            print(f"Uplata od {iznos:.2f} € na račun {self.broj_racuna} je uspješna.")
        else:
            print("Neispravan iznos za uplatu. Iznos mora biti pozitivan.")

    def isplati(self, iznos):
        """Smanjuje stanje na računu ako ima dovoljno sredstava."""
        if iznos <= 0:
            print("Greška: Iznos za isplatu mora biti pozitivan.")
        elif self.stanje >= iznos:
            self.stanje -= iznos
            print(f"Isplata od {iznos:.2f} € uspješna. Novo stanje: {self.stanje:.2f} €.")
        else:
            print(f"Isplata nije moguća. Nedovoljno sredstava (Stanje: {self.stanje:.2f} €).")
    
    #Ispis podataka o računu.
    def info(self):
        """Ispisuje informacije o računu."""
        print("-" * 25)
        print(f"Vlasnik: {self.ime_prezime}")
        print(f"Broj računa: {self.broj_racuna}")
        print(f"Stanje: {self.stanje:.2f} €")
        print("-" * 25)

# Testiranje klase
racun1 = BankovniRacun("Pero Perić", "HR123456789")
print("Ispis podataka o računu:")
racun1.info()
print("Uplata na račun. 1000€")
racun1.uplati(1000)
print("Uplata na račun. 500€")
racun1.uplati(500)
print("Isplata od 250€")
racun1.isplati(250)
print("Isplata od 1800€ (Pokušaj isplate prevelikog iznosa)")
racun1.isplati(1800) # Pokušaj isplate prevelikog iznosa
print("Uplata od -50€. Pokušaj uplate negativnog iznosa")
racun1.uplati(-50) # Pokušaj uplate negativnog iznosa
print("\n" + "="*30 + "\n")
print("Informacija o računu nakon izvršenih operacija:")
racun1.info()
print("\n" + "="*30 + "\n")
