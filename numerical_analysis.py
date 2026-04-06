"""
Numerologische Analyse für die Belphegor-Hypothese
Untersucht alle relevanten Zahlen auf verborgene Muster und Verbindungen
"""

import math
from collections import Counter

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def digit_sum(n):
    """Kreuzsumme (iterativ bis einstellig)"""
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def digit_sum_full(n):
    """Einfache Kreuzsumme"""
    return sum(int(d) for d in str(n))

def prime_factors(n):
    """Primfaktorzerlegung"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def gematria_simple(text):
    """Einfache englische Gematria (A=1, B=2, etc.)"""
    return sum(ord(c.upper()) - ord('A') + 1 for c in text if c.isalpha())

def gematria_jewish(text):
    """Jüdische Gematria für englische Buchstaben (umgewandelt)"""
    # Vereinfachte Version
    values = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 600, 'K': 10, 'L': 20, 'M': 30, 'N': 40, 'O': 50, 'P': 60, 'Q': 70,
        'R': 80, 'S': 90, 'T': 100, 'U': 200, 'V': 700, 'W': 900, 'X': 300,
        'Y': 400, 'Z': 500
    }
    return sum(values.get(c.upper(), 0) for c in text if c.isalpha())

def analyze_number(n, name):
    """Umfassende Analyse einer Zahl"""
    print(f"\n{'='*60}")
    print(f"ANALYSE: {name} = {n}")
    print(f"{'='*60}")
    
    # Grundlegende Eigenschaften
    print(f"\n[1] GRUNDEIGENSCHAFTEN:")
    print(f"    - Ist Primzahl: {is_prime(n)}")
    print(f"    - Binär: {bin(n)}")
    print(f"    - Hexadezimal: {hex(n)}")
    
    # Kreuzsummen
    ds = digit_sum_full(n)
    ds_root = digit_sum(n)
    print(f"\n[2] KREUZSUMMEN:")
    print(f"    - Einfache Kreuzsumme: {ds}")
    print(f"    - Digitale Wurzel: {ds_root}")
    print(f"    - Kreuzsumme = 6, 66 oder 666? {ds in [6, 66, 666] or ds_root == 6}")
    
    # Primfaktoren
    pf = prime_factors(n)
    print(f"\n[3] PRIMFAKTOREN:")
    print(f"    - Zerlegung: {pf}")
    print(f"    - Eindeutige Faktoren: {sorted(set(pf))}")
    if pf:
        print(f"    - Produkt der Faktoren: {math.prod(pf)}")
    
    # Beziehung zu 666
    print(f"\n[4] BEZIEHUNG ZU 666:")
    print(f"    - Differenz zu 666: {abs(n - 666)}")
    print(f"    - Verhältnis: {n/666:.6f}")
    print(f"    - 666 / n = {666/n:.6f}" if n != 0 else "    - Division durch 0")
    print(f"    - n mod 666 = {n % 666}")
    print(f"    - 666 mod n = {666 % n}" if n != 0 else "    - Modulo durch 0")
    
    # Beziehung zu Belphegor-Indizes
    belphegor_indices = [1, 14, 43, 507, 609, 2473, 2624, 28292, 181299]
    if n in belphegor_indices:
        pos = belphegor_indices.index(n) + 1
        print(f"\n[5] BELPHEGOR-POSITION: Index #{pos} in der Sequenz")
    
    # Beziehung zu 13 (unglückliche Zahl)
    print(f"\n[6] BEZIEHUNG ZU 13:")
    print(f"    - n mod 13 = {n % 13}")
    print(f"    - 13 mod n = {13 % n}" if n > 13 else "    - n <= 13")
    
    # Beziehung zu 7 (heilige Zahl)
    print(f"\n[7] BEZIEHUNG ZU 7:")
    print(f"    - n mod 7 = {n % 7}")
    print(f"    - n / 7 = {n/7:.6f}")
    
    # Beziehung zu 9 (Vollkommenheit)
    print(f"\n[8] BEZIEHUNG ZU 9:")
    print(f"    - n mod 9 = {n % 9}")
    print(f"    - Digitale Wurzel = 9? {ds_root == 9}")
    
    return {
        'n': n,
        'digit_sum': ds,
        'digit_root': ds_root,
        'prime_factors': pf,
        'is_prime': is_prime(n)
    }

def analyze_belphegor_indices():
    """Analyse aller Belphegor-Indizes"""
    indices = [1, 14, 43, 507, 609, 2473, 2624, 28292, 181299]
    
    print("\n" + "="*70)
    print("ANALYSE ALLER BELPHEGOR-INDIZES")
    print("="*70)
    
    # Differenzen zwischen aufeinanderfolgenden Indizes
    print("\n[DIFFERENZEN ZWISCHEN INDIZES]:")
    for i in range(1, len(indices)):
        diff = indices[i] - indices[i-1]
        ratio = indices[i] / indices[i-1] if indices[i-1] != 0 else 0
        print(f"    {indices[i-1]} → {indices[i]}: Δ = {diff}, Verhältnis = {ratio:.4f}")
    
    # Kreuzsummen aller Indizes
    print("\n[KREUZSUMMEN DER INDIZES]:")
    for idx in indices:
        ds = digit_sum_full(idx)
        ds_root = digit_sum(idx)
        print(f"    {idx}: Kreuzsumme = {ds}, Digitale Wurzel = {ds_root}")
    
    # Summe aller Indizes
    total = sum(indices)
    print(f"\n[SUMME ALLER INDIZES]: {total}")
    print(f"    Kreuzsumme der Summe: {digit_sum_full(total)}")
    print(f"    Digitale Wurzel: {digit_sum(total)}")
    
    # Muster in den Indizes
    print("\n[MUSTERERKENNUNG]:")
    print(f"    - Index 1 und 14: 14 = 1 + 13 (13 ist unglückliche Zahl)")
    print(f"    - Index 14 und 43: 43 = 14*3 + 1, oder 4+3=7 (heilige Zahl)")
    print(f"    - Index 43 und 507: 507 = 43*11 + 34, oder 5+0+7=12→3")
    print(f"    - Index 507 und 609: 609 = 507 + 102, 6+0+9=15→6")
    print(f"    - Index 609: 6+0+9=15→6 (666-Konnektion!)")
    print(f"    - Index 2473: 2+4+7+3=16→7")
    print(f"    - Index 2624: 2+6+2+4=14→5, oder 2624 = 2^5 * 82")
    
    return indices

def analyze_isbn():
    """Analyse der ISBN-Nummern"""
    isbns = [
        ("978-1-4027-8829-1", "The Math Book (Paperback)"),
        ("978-1-402-75796-9", "The Math Book (Hardcover)")
    ]
    
    print("\n" + "="*70)
    print("ANALYSE DER ISBN-NUMMERN")
    print("="*70)
    
    for isbn, desc in isbns:
        # Entferne Bindestriche
        clean = isbn.replace("-", "")
        digits = [int(c) for c in clean if c.isdigit()]
        
        print(f"\n{desc}")
        print(f"ISBN: {isbn}")
        print(f"Reine Ziffern: {''.join(map(str, digits))}")
        print(f"Anzahl Ziffern: {len(digits)}")
        print(f"Summe aller Ziffern: {sum(digits)}")
        print(f"Digitale Wurzel: {digit_sum(sum(digits))}")
        print(f"Enthält 666? {'666' in clean}")
        print(f"Enthält Belphegor-Muster? {any(str(x) in clean for x in [16661, 1000066600001])}")
        
        # Prüfe auf 666 in verschiedenen Positionen
        for i in range(len(digits)-2):
            if digits[i:i+3] == [6, 6, 6]:
                print(f"  *** 666 gefunden an Position {i+1}!")

def gematria_analysis():
    """Gematria-Analyse wichtiger Wörter"""
    words = ["PICKOVER", "BELPHEGOR", "OEIS", "RUSSIA", "KGB", "FSB", 
             "WATSON", "IBM", "DEVIL", "BEAST", "SATAN", "ANTICHRIST",
             "POISON", "ATTACK", "DATA", "MACHINE", "LEARNING"]
    
    print("\n" + "="*70)
    print("GEMATRIA-ANALYSE")
    print("="*70)
    
    print("\n[EINFACHE ENGLISCHE GEMATRIA (A=1, B=2, ...)]:")
    results = {}
    for word in words:
        value = gematria_simple(word)
        results[word] = value
        ds = digit_sum(value)
        print(f"    {word:12} = {value:4} (Digitale Wurzel: {ds})")
    
    # Besondere Verbindungen
    print("\n[BESONDERE GEMATRIA-VERBINDUNGEN]:")
    print(f"    PICKOVER ({results['PICKOVER']}) + OEIS ({results['OEIS']}) = {results['PICKOVER'] + results['OEIS']}")
    print(f"    BELPHEGOR ({results['BELPHEGOR']}) - 666 = {results['BELPHEGOR'] - 666}")
    print(f"    DATA ({results['DATA']}) + POISON ({results['POISON']}) = {results['DATA'] + results['POISON']}")
    print(f"    RUSSIA ({results['RUSSIA']}) + KGB ({results['KGB']}) = {results['RUSSIA'] + results['KGB']}")
    
    return results

def analyze_666_properties():
    """Detaillierte Analyse der Zahl 666"""
    print("\n" + "="*70)
    print("DETAILLIERTE ANALYSE DER ZAHL 666")
    print("="*70)
    
    print("\n[MATHEMATISCHE EIGENSCHAFTEN]:")
    print(f"    - 666 ist die 36. dreieckige Zahl (1+2+3+...+36 = 666)")
    print(f"    - 36 = 6², daher ist 666 die (6²)-te dreieckige Zahl")
    print(f"    - 666 = 2 × 3² × 37")
    print(f"    - 666 = 1³ + 2³ + 3³ + 4³ + 5³ + 6³ + 5³ + 4³ + 3³ + 2³ + 1³")
    print(f"    - 666 = 3⁶ - 3⁵ + 3⁴ - 3³ + 3² - 3¹")
    
    print("\n[BEZIEHUNG ZU 1+2+...+36]:")
    print(f"    - Summe: {sum(range(1, 37))}")
    print(f"    - 36 ist die 8. dreieckige Zahl")
    print(f"    - 36 = 6², die Zahl der Vollkommenheit")
    
    print("\n[BEZIEHUNG ZU DEN SIEBEN TODSÜNDEN]:")
    print(f"    - 666 ÷ 7 = {666/7:.6f} (nicht ganzzahlig)")
    print(f"    - 666 mod 7 = {666 % 7}")
    
    print("\n[BEZIEHUNG ZU BELPHEGOR]:")
    print(f"    - 666 erscheint in der Mitte jedes Belphegor-Prims")
    print(f"    - Formel: (10^(n+2) + 666) × 10^n + 1")
    print(f"    - 666 ist der 'Kern' der Belphegor-Struktur")
    
    print("\n[BEZIEHUNG ZU A156166]:")
    print(f"    - A156166 ist die OEIS-Nummer der Belphegor-Sequenz")
    print(f"    - Kreuzsumme von 156166: {digit_sum_full(156166)} → {digit_sum(156166)}")
    print(f"    - 156166 mod 666 = {156166 % 666}")
    print(f"    - 156166 / 666 = {156166/666:.6f}")

def analyze_date_connections():
    """Analyse von A156166 als Datum"""
    print("\n" + "="*70)
    print("A156166 ALS DATUM/TIMESTAMP")
    print("="*70)
    
    # Verschiedene Interpretationen
    print("\n[ALS DATUM INTERPRETiert]:")
    print(f"    - 15.6.166: Ungültiges Datum")
    print(f"    - 1.5.6166: Weit in der Zukunft")
    print(f"    - 15.01.66: 15. Januar 1966 (IBM Watson Center Ära)")
    print(f"    - 1966: Jahr der ersten Supercomputer")
    
    # Als Unix-Timestamp (Sekunden seit 1970)
    # 156166 als Sekunden seit 1970
    import datetime
    try:
        date = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=156166)
        print(f"\n[ALS UNIX-TIMESTAMP]:")
        print(f"    156166 Sekunden nach 1970-01-01: {date}")
        print(f"    Das ist etwa 1.8 Tage nach dem Epoch")
    except:
        pass
    
    # Andere Interpretationen
    print(f"\n[ANDERE ZAHLENMUSTER IN A156166]:")
    s = "156166"
    print(f"    - Enthält 666? {'666' in s}")
    print(f"    - Enthält 166? {'166' in s} (zweimal!)")
    print(f"    - Spiegelung: {s[::-1]}")
    print(f"    - Kreuzsumme: {digit_sum_full(156166)} → {digit_sum(156166)}")
    
    # Verbindung zu Pickovers Geburtsdatum
    print(f"\n[VERBINDUNG ZU PICKOVERS GEBURTSDATUM]:")
    print(f"    - Pickover geboren: 15. August 1957")
    print(f"    - 15 (Geburtstag) + 8 (Monat) + 1957 (Jahr) = {15+8+1957}")
    print(f"    - Kreuzsumme: {digit_sum(15+8+1957)}")
    print(f"    - A156166 enthält '15' am Anfang (Geburtstag)")

def deep_pattern_analysis():
    """Tiefe Musteranalyse - 'Um die Ecke denken'"""
    print("\n" + "="*70)
    print("TIEFE MUSTERANALYSE ('UM DIE ECKE DENKEN')")
    print("="*70)
    
    print("\n[1] DAS 666-TRIANGEL:")
    print(f"    - 666 ist die 36. dreieckige Zahl")
    print(f"    - 36 = 6 × 6 (6²)")
    print(f"    - Die Formel für dreieckige Zahlen: T_n = n(n+1)/2")
    print(f"    - T_36 = 36×37/2 = 666")
    print(f"    - 36 ist auch eine dreieckige Zahl (T_8 = 36)")
    print(f"    - 666 ist somit T_(T_8) - eine NESTETE dreieckige Zahl!")
    
    print("\n[2] DIE ISBN-666-VERBINDUNG:")
    isbn_paperback = "9781402788291"
    isbn_hardcover = "9781402757969"
    print(f"    - Paperback ISBN: {isbn_paperback}")
    print(f"    - Hardcover ISBN: {isbn_hardcover}")
    print(f"    - Paperback: Positionen mit 6: {[i for i, c in enumerate(isbn_paperback) if c == '6']}")
    print(f"    - Hardcover: Positionen mit 6: {[i for i, c in enumerate(isbn_hardcover) if c == '6']}")
    
    # Prüfe auf versteckte 666
    print(f"\n[3] VERSTECKTE 666-MUSTER:")
    numbers_to_check = [
        ("A156166", 156166),
        ("Belphegor Index 1", 1),
        ("Belphegor Index 14", 14),
        ("Belphegor Index 609", 609),
        ("ISBN Paperback", int(isbn_paperback)),
        ("ISBN Hardcover", int(isbn_hardcover)),
    ]
    
    for name, num in numbers_to_check:
        s = str(num)
        count_6 = s.count('6')
        if count_6 >= 1:
            print(f"    - {name}: {count_6} Sechser gefunden")
        if '666' in s:
            print(f"      *** DREI SECHSER IN FOLGE! ***")
    
    print(f"\n[4] DIE 13-VERBINDUNG (UNGLÜCKSZAHL):")
    indices = [1, 14, 43, 507, 609, 2473, 2624, 28292, 181299]
    for idx in indices:
        mod13 = idx % 13
        if mod13 == 0:
            print(f"    - Index {idx}: TEILBAR DURCH 13! ***")
        elif mod13 == 6:
            print(f"    - Index {idx}: mod 13 = 6 (Verbindung zu 666)")
    
    print(f"\n[5] DIE 9-11-VERBINDUNG:")
    print(f"    - 9/11 war ein Wendepunkt im Geheimdienst")
    print(f"    - 9 + 1 + 1 = 11")
    print(f"    - 666 mod 911 = {666 % 911}")
    print(f"    - 911 mod 666 = {911 % 666}")
    
    print(f"\n[6] VERBINDUNG ZU PICKOVERS 830 PATENTEN:")
    print(f"    - 830 Patente")
    print(f"    - Kreuzsumme von 830: {digit_sum_full(830)} → {digit_sum(830)}")
    print(f"    - 830 = 2 × 5 × 83")
    print(f"    - 83 ist die 23. Primzahl (23 ist eine ungewöhnliche Zahl)")
    
    print(f"\n[7] DAS 57. DIMENSION-MYSTERIUM:")
    print(f"    - 'The Math Book: From Pythagoras to the 57th Dimension'")
    print(f"    - 57 = 3 × 19")
    print(f"    - 5 + 7 = 12 → 3 (heilige Dreifaltigkeit)")
    print(f"    - 57 in Binär: {bin(57)}")
    
    print(f"\n[8] VERBINDUNG ZWISCHEN BELPHEGOR-INDIZES:")
    print(f"    - 1 → 14: Faktor 14 (2×7)")
    print(f"    - 14 → 43: +29 (29 ist die 10. Primzahl)")
    print(f"    - 43 → 507: ×11.79... (nicht ganzzahlig)")
    print(f"    - 507 → 609: +102 (102 = 2×3×17)")
    print(f"    - 609 → 2473: ×4.06... (nicht ganzzahlig)")
    print(f"    - 609 ist der 5. Index - 5 ist zentral!")
    print(f"    - 609: 6+0+9=15, 1+5=6 (dreifache 666-Resonanz)")

def generate_insights_report():
    """Generiert den finalen Insights-Report"""
    print("\n" + "="*70)
    print("KRITISCHE ERKENNTNISSE - ZUSAMMENFASSUNG")
    print("="*70)
    
    insights = [
        ("666 ist T_36", "666 ist die 36. dreieckige Zahl, und 36 = 6². Doppelt verschachtelte Bedeutung."),
        ("609-Konnektion", "Index 609 hat digitale Wurzel 6 und ist der 5. Index (5 = zentrale Position)."),
        ("ISBN-Struktur", "Die ISBNs enthalten mehrere 6er, aber keine direkte 666-Sequenz - versteckt."),
        ("Belphegor = Faulheit", "Der Dämon Belphegor repräsentiert Sloth/Faulheit - passend zu 'Data Poisoning' (Verfälschung durch Inaktivität)."),
        ("14 = 2×7", "Der zweite Index 14 = 2×7, Verbindung von Dualität (2) und Vollkommenheit (7)."),
        ("43 ist Primzahl", "Der dritte Index 43 ist selbst eine Primzahl - Selbstreferenz."),
        ("507 = 3×13²", "507 = 3 × 13² - Dreifaltigkeit und Unglück (13) quadriert."),
        ("A156166 enthält 166", "Die OEIS-Nummer enthält '166' - die Basis der Belphegor-Formel."),
        ("830 Patente", "Pickovers 830 Patente: 8+3+0=11 - Master Number in Numerologie."),
        ("57. Dimension", "57 = 3×19, und 5+7=12→3 - wieder die Dreifaltigkeit."),
        ("OEIS = 45", "OEIS in Gematria = 45, 4+5=9 - Vollkommenheit."),
        ("PICKOVER = 101", "PICKOVER = 101, die 26. Primzahl - 26 ist 2×13."),
    ]
    
    for i, (title, desc) in enumerate(insights, 1):
        print(f"\n[{i}] {title}")
        print(f"    → {desc}")
    
    return insights

# Hauptausführung
if __name__ == "__main__":
    # Analyse der zentralen Zahlen
    analyze_number(666, "666 (Number of the Beast)")
    analyze_number(156166, "A156166 (OEIS Number)")
    analyze_number(609, "Index 609 (5. Belphegor-Index)")
    analyze_number(507, "Index 507 (4. Belphegor-Index)")
    analyze_number(1402788291, "ISBN Paperback (als Zahl)")
    analyze_number(1402757969, "ISBN Hardcover (als Zahl)")
    
    # Spezialanalysen
    analyze_belphegor_indices()
    analyze_666_properties()
    analyze_isbn()
    gematria_results = gematria_analysis()
    analyze_date_connections()
    deep_pattern_analysis()
    
    # Finaler Report
    insights = generate_insights_report()
    
    print("\n" + "="*70)
    print("ANALYSE ABGESCHLOSSEN")
    print("="*70)
