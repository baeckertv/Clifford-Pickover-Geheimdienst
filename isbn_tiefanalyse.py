"""
TIEFGEHENDE ISBN-ANALYSE
Sämtliche ISBNs auf Zahlenmuster, Rätsel und versteckte Sequenzen prüfen
"""

print("="*80)
print("TIEFGEHENDE ISBN-ANALYSE")
print("Sämtliche ISBNs auf Muster, Rätsel und versteckte Sequenzen")
print("="*80)

# Alle bekannten Pickover-ISBNs (aus Wikipedia und OEIS)
isbn_liste = [
    # The Math Book
    ("978-1-4027-5796-9", "The Math Book (Hardcover)"),
    ("978-1-4027-8829-1", "The Math Book (Paperback)"),
    
    # The Physics Book
    ("978-1-4027-7861-2", "The Physics Book (Hardcover)"),
    ("978-1-4027-7862-9", "The Physics Book (Paperback)"),
    
    # The Medical Book
    ("978-1-4027-8585-7", "The Medical Book (Hardcover)"),
    ("978-1-4317-0102-4", "The Medical Book (SA Edition)"),
    
    # The Science Book
    ("978-1-4027-8961-9", "The Science Book (Hardcover)"),
    ("978-1-4027-8962-6", "The Science Book (Paperback)"),
    
    # Computers, Pattern, Chaos and Beauty
    ("978-0-486-40909-3", "Computers, Pattern, Chaos and Beauty (Dover)"),
    ("978-0-718-50307-9", "Computers, Pattern, Chaos and Beauty (UK)"),
    ("978-0-312-06162-1", "Computers, Pattern, Chaos and Beauty (St. Martin's)"),
    
    # Mazes for the Mind
    ("978-0-312-10593-6", "Mazes for the Mind (St. Martin's)"),
    ("978-0-718-50359-8", "Mazes for the Mind (UK)"),
    
    # Chaos in Wonderland
    ("978-0-312-10643-8", "Chaos in Wonderland (St. Martin's)"),
    ("978-0-718-50432-8", "Chaos in Wonderland (UK)"),
    
    # Keys to Infinity
    ("978-0-471-11857-2", "Keys to Infinity (Wiley)"),
    ("978-0-471-19334-0", "Keys to Infinity (Wiley Paper)"),
    
    # Black Holes
    ("978-0-471-19704-1", "Black Holes (Wiley)"),
    ("978-0-471-25122-4", "Black Holes (Wiley Paper)"),
    
    # Surfing Through Hyperspace
    ("978-0-19-513006-5", "Surfing Through Hyperspace (Oxford)"),
    ("978-0-19-514241-9", "Surfing Through Hyperspace (Oxford Paper)"),
    
    # The Stars of Heaven
    ("978-0-19-514874-9", "The Stars of Heaven (Oxford)"),
    ("978-0-19-517021-4", "The Stars of Heaven (Oxford Paper)"),
    
    # The Zen of Magic Squares
    ("978-0-691-11597-9", "The Zen of Magic Squares (Princeton)"),
    ("978-0-691-11598-6", "The Zen of Magic Squares (Princeton Paper)"),
    
    # Wonders of Numbers
    ("978-0-19-514501-4", "Wonders of Numbers (Oxford)"),
    
    # A Passion for Mathematics
    ("978-0-471-69098-6", "A Passion for Mathematics (Wiley)"),
    
    # The Mobius Strip
    ("978-1-4008-3026-5", "The Mobius Strip (Thunder's Mouth)"),
    ("978-0-571-21679-8", "The Mobius Strip (UK)"),
    
    # A Beginner's Guide to Immortality
    ("978-1-56025-984-8", "A Beginner's Guide to Immortality (Thunder's Mouth)"),
    
    # Archimedes to Hawking
    ("978-0-19-533611-5", "Archimedes to Hawking (Oxford)"),
    ("978-0-19-979268-6", "Archimedes to Hawking (Oxford Paper)"),
    
    # The Book of Black
    ("978-1-4027-8826-0", "The Book of Black (Sterling)"),
    ("978-1-4027-8827-7", "The Book of Black (Sterling Paper)"),
    
    # Death and the Afterlife
    ("978-1-63220-454-2", "Death and the Afterlife (Sterling)"),
    ("978-1-4027-9128-4", "Death and the Afterlife (Sterling Alt)"),
    
    # Artificial Intelligence
    ("978-1-4027-9567-1", "Artificial Intelligence (Sterling)"),
    ("978-1-4027-9568-8", "Artificial Intelligence (Sterling Paper)"),
]

# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def bereinige_isbn(isbn):
    """Entfernt Bindestriche und 'X' aus ISBN"""
    return isbn.replace("-", "").replace("X", "10")

def digit_sum(n):
    """Kreuzsumme berechnen"""
    return sum(int(d) for d in str(abs(n)) if d.isdigit())

def digital_root(n):
    """Digitale Wurzel berechnen"""
    while n >= 10:
        n = digit_sum(n)
    return n

def validate_isbn10(isbn):
    """ISBN-10 Prüfsumme validieren"""
    clean = isbn.replace("-", "")
    if len(clean) != 10:
        return None
    
    try:
        total = 0
        for i, char in enumerate(clean[:9]):
            total += int(char) * (10 - i)
        
        # Prüfziffer
        check = clean[9]
        if check.upper() == 'X':
            check_val = 10
        else:
            check_val = int(check)
        
        total += check_val
        return total % 11 == 0
    except:
        return None

def validate_isbn13(isbn):
    """ISBN-13 Prüfsumme validieren"""
    clean = isbn.replace("-", "")
    if len(clean) != 13:
        return None
    
    try:
        total = 0
        for i, char in enumerate(clean[:12]):
            if i % 2 == 0:
                total += int(char)
            else:
                total += int(char) * 3
        
        # Prüfziffer
        check = int(clean[12])
        calculated = (10 - (total % 10)) % 10
        return check == calculated
    except:
        return None

def finde_sequenzen(text, laenge=3):
    """Findet aufsteigende/absteigende Sequenzen"""
    ziffern = [int(c) for c in text if c.isdigit()]
    sequenzen = []
    
    for i in range(len(ziffern) - laenge + 1):
        teil = ziffern[i:i+laenge]
        # Aufsteigend
        if all(teil[j] + 1 == teil[j+1] for j in range(laenge-1)):
            sequenzen.append((i, teil, "aufsteigend"))
        # Absteigend
        if all(teil[j] - 1 == teil[j+1] for j in range(laenge-1)):
            sequenzen.append((i, teil, "absteigend"))
    
    return sequenzen

def finde_wiederholungen(text):
    """Findet wiederholte Ziffern"""
    ziffern = [int(c) for c in text if c.isdigit()]
    wiederholungen = []
    
    i = 0
    while i < len(ziffern):
        count = 1
        while i + count < len(ziffern) and ziffern[i] == ziffern[i + count]:
            count += 1
        if count >= 3:
            wiederholungen.append((ziffern[i], count, i))
        i += count
    
    return wiederholungen

def finde_palindrome(text, min_len=4):
    """Findet Palindrome in der Ziffernfolge"""
    ziffern = [c for c in text if c.isdigit()]
    palindrome = []
    
    for i in range(len(ziffern)):
        for j in range(i + min_len, min(i + 15, len(ziffern) + 1)):
            teil = ziffern[i:j]
            if teil == teil[::-1] and len(teil) >= min_len:
                palindrome.append((i, ''.join(teil)))
    
    return palindrome

def analyse_isbn(isbn, titel):
    """Umfassende Analyse einer einzelnen ISBN"""
    clean = bereinige_isbn(isbn)
    
    print(f"\n{'='*70}")
    print(f"ISBN: {isbn}")
    print(f"Buch: {titel}")
    print(f"{'='*70}")
    
    # Grunddaten
    print(f"\n[STRUKTUR]")
    print(f"  Bereinigt: {clean}")
    print(f"  Länge: {len(clean)} Zeichen")
    
    # Validierung
    isbn10_valid = validate_isbn10(isbn)
    isbn13_valid = validate_isbn13(isbn)
    
    if isbn13_valid is not None:
        status = "GUELTIG" if isbn13_valid else "UNGÜLTIG"
        print(f"  ISBN-13 Prüfsumme: {status}")
    if isbn10_valid is not None:
        status = "GUELTIG" if isbn10_valid else "UNGÜLTIG"
        print(f"  ISBN-10 Prüfsumme: {status}")
    
    # Numerische Analyse
    if clean.isdigit():
        zahl = int(clean)
        ks = digit_sum(zahl)
        w = digital_root(zahl)
        
        print(f"\n[NUMERISCHE ANALYSE]")
        print(f"  Als Zahl: {zahl}")
        print(f"  Kreuzsumme: {ks}")
        print(f"  Digitale Wurzel: {w}")
        
        if w == 7:
            print(f"  *** HEILIGE 7 (Wurzel)! ***")
        elif w == 6:
            print(f"  *** 666-RESONANZ (Wurzel 6)! ***")
        elif w == 9:
            print(f"  *** VOLLKOMMENHEIT (Wurzel 9)! ***")
        
        # Modulo-Analyse
        print(f"\n[MODULO-ANALYSE]")
        print(f"  mod 666: {zahl % 666}")
        print(f"  mod 13: {zahl % 13} {'(HEILIGE 7!)' if zahl % 13 == 7 else '(666-Resonanz)' if zahl % 13 == 6 else ''}")
        print(f"  mod 7: {zahl % 7} {'(TEILBAR!)' if zahl % 7 == 0 else ''}")
    
    # Muster-Suche
    print(f"\n[MUSTER-SUCHE]")
    
    # Sequenzen
    sequenzen = finde_sequenzen(clean)
    if sequenzen:
        print(f"  Gefundene Sequenzen:")
        for pos, seq, typ in sequenzen:
            print(f"    Position {pos}: {''.join(map(str, seq))} ({typ})")
    else:
        print(f"  Keine 3+ Ziffern-Sequenzen gefunden")
    
    # Wiederholungen
    wiederholungen = finde_wiederholungen(clean)
    if wiederholungen:
        print(f"  Wiederholungen (3+ gleiche Ziffern):")
        for ziffer, count, pos in wiederholungen:
            print(f"    Position {pos}: {ziffer} wiederholt {count}x")
    else:
        print(f"  Keine 3+ Wiederholungen gefunden")
    
    # Palindrome
    palindrome = finde_palindrome(clean)
    if palindrome:
        print(f"  Palindrome (4+ Ziffern):")
        for pos, pal in palindrome:
            print(f"    Position {pos}: {pal}")
    else:
        print(f"  Keine Palindrome gefunden")
    
    # Spezielle Muster
    print(f"\n[SPEZIELLE MUSTER]")
    
    # Enthält 666?
    if "666" in clean:
        print(f"  *** ENTHÄLT 666! ***")
    
    # Enthält 777?
    if "777" in clean:
        print(f"  *** ENTHÄLT 777 (heilig)! ***")
    
    # Enthält 13?
    if "13" in clean:
        pos = clean.find("13")
        print(f"  Enthält 13 (Unglückszahl) an Position {pos}")
    
    # Enthält 166?
    if "166" in clean:
        pos = clean.find("166")
        print(f"  *** ENTHÄLT 166 (Belphegor-Basis) an Position {pos}! ***")
    
    # Spiegelung
    if len(clean) >= 4:
        first_half = clean[:len(clean)//2]
        second_half = clean[len(clean)//2:]
        if first_half == second_half[::-1]:
            print(f"  *** SPIEGELUNG gefunden! {first_half} | {second_half} ***")
    
    return {
        'isbn': isbn,
        'clean': clean,
        'wurzel': w if clean.isdigit() else None,
        'mod_13': zahl % 13 if clean.isdigit() else None,
        'mod_7': zahl % 7 if clean.isdigit() else None,
        'hat_666': "666" in clean,
        'hat_166': "166" in clean,
        'hat_777': "777" in clean,
        'sequenzen': sequenzen,
        'wiederholungen': wiederholungen,
        'palindrome': palindrome
    }

# ============================================================
# HAUPTANALYSE
# ============================================================

print("\n" + "="*80)
print("ANALYSE ALLER ISBNs")
print("="*80)

ergebnisse = []
for isbn, titel in isbn_liste:
    ergebnis = analyse_isbn(isbn, titel)
    ergebnisse.append(ergebnis)

# ============================================================
# KREUZANALYSE
# ============================================================

print("\n" + "="*80)
print("KREUZANALYSE ALLER ISBNs")
print("="*80)

# Zähle spezielle Eigenschaften
print("\n[STATISTIK ÜBER ALLE ISBNs]")

mit_666 = [e for e in ergebnisse if e['hat_666']]
mit_166 = [e for e in ergebnisse if e['hat_166']]
mit_777 = [e for e in ergebnisse if e['hat_777']]
wurzel_7 = [e for e in ergebnisse if e['wurzel'] == 7]
wurzel_6 = [e for e in ergebnisse if e['wurzel'] == 6]
mod_13_7 = [e for e in ergebnisse if e['mod_13'] == 7]
mod_13_6 = [e for e in ergebnisse if e['mod_13'] == 6]

print(f"\n  Gesamtanzahl ISBNs: {len(ergebnisse)}")
print(f"  Mit '666': {len(mit_666)} ({len(mit_666)/len(ergebnisse)*100:.1f}%)")
print(f"  Mit '166' (Belphegor): {len(mit_166)} ({len(mit_166)/len(ergebnisse)*100:.1f}%)")
print(f"  Mit '777' (heilig): {len(mit_777)} ({len(mit_777)/len(ergebnisse)*100:.1f}%)")
print(f"  Wurzel = 7: {len(wurzel_7)} ({len(wurzel_7)/len(ergebnisse)*100:.1f}%)")
print(f"  Wurzel = 6: {len(wurzel_6)} ({len(wurzel_6)/len(ergebnisse)*100:.1f}%)")
print(f"  mod 13 = 7: {len(mod_13_7)} ({len(mod_13_7)/len(ergebnisse)*100:.1f}%)")
print(f"  mod 13 = 6: {len(mod_13_6)} ({len(mod_13_6)/len(ergebnisse)*100:.1f}%)")

# Besondere ISBNs
print("\n[BESONDERE ISBNs MIT MUSTERN]")

print("\n  ISBNs mit 666:")
for e in mit_666:
    print(f"    - {e['isbn']} (Wurzel: {e['wurzel']})")

print("\n  ISBNs mit 166 (Belphegor):")
for e in mit_166:
    print(f"    - {e['isbn']} (Wurzel: {e['wurzel']})")

print("\n  ISBNs mit Wurzel 7:")
for e in wurzel_7:
    print(f"    - {e['isbn']} (mod 13: {e['mod_13']})")

print("\n  ISBNs mit Wurzel 6:")
for e in wurzel_6:
    print(f"    - {e['isbn']} (mod 13: {e['mod_13']})")

# Kreuzverbindungen suchen
print("\n[KREUZVERBINDUNGEN ZWISCHEN ISBNs]")

# Gleiche Endungen/Anfänge
endungen = {}
anfaenge = {}

for e in ergebnisse:
    if len(e['clean']) >= 4:
        ende = e['clean'][-4:]
        anfang = e['clean'][:4]
        
        if ende not in endungen:
            endungen[ende] = []
        endungen[ende].append(e['isbn'])
        
        if anfang not in anfaenge:
            anfaenge[anfang] = []
        anfaenge[anfang].append(e['isbn'])

# Mehrfache Endungen
print("\n  Gleiche 4-Ziffer-Endungen:")
for ende, isbns in endungen.items():
    if len(isbns) > 1:
        print(f"    ...{ende}: {len(isbns)} ISBNs")
        for isbn in isbns:
            print(f"      - {isbn}")

# Mehrfache Anfänge
print("\n  Gleiche 4-Ziffer-Anfänge:")
for anfang, isbns in anfaenge.items():
    if len(isbns) > 1:
        print(f"    {anfang}...: {len(isbns)} ISBNs")
        for isbn in isbns:
            print(f"      - {isbn}")

print("\n" + "="*80)
print("ANALYSE ABGESCHLOSSEN")
print("="*80)
