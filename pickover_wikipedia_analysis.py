"""
Tiefe Zahlenanalyse der Wikipedia-Artikel über Clifford A. Pickover
Analysiert alle ISBNs, Jahre, Vampire Numbers, und andere signifikante Zahlen
"""

import math
from collections import Counter, defaultdict

def digit_sum(n):
    """Kreuzsumme berechnen"""
    return sum(int(d) for d in str(abs(n)) if d.isdigit())

def digital_root(n):
    """Digitale Wurzel berechnen"""
    while n >= 10:
        n = digit_sum(n)
    return n

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

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

def analyze_isbn(isbn, title, year):
    """Analysiere eine einzelne ISBN tiefgehend"""
    # Bereinige ISBN (entferne Bindestriche)
    clean = isbn.replace('-', '').replace(' ', '')
    digits = [int(c) for c in clean if c.isdigit()]
    
    print(f"\n{'='*70}")
    print(f"ISBN: {isbn}")
    print(f"Titel: {title}")
    print(f"Jahr: {year}")
    print(f"{'='*70}")
    
    print(f"\n[GRUNDANALYSE]")
    print(f"  - Gereinigte Ziffern: {clean}")
    print(f"  - Anzahl Ziffern: {len(digits)}")
    print(f"  - Summe aller Ziffern: {sum(digits)}")
    print(f"  - Digitale Wurzel: {digital_root(sum(digits))}")
    
    print(f"\n[ZIFFERNANALYSE]")
    digit_counts = Counter(digits)
    for d in sorted(digit_counts.keys()):
        print(f"  - Ziffer {d}: {digit_counts[d]}x")
    
    print(f"\n[666-ANALYSE]")
    clean_str = ''.join(map(str, digits))
    if '666' in clean_str:
        pos = clean_str.index('666')
        print(f"  *** 666 GEFUNDEN an Position {pos+1}! ***")
    if '66' in clean_str:
        print(f"  - 66 gefunden: {clean_str.count('66')}x")
    count_6 = clean_str.count('6')
    if count_6 >= 1:
        print(f"  - Anzahl der Sechser: {count_6}")
    
    print(f"\n[13-ANALYSE (UNGLÜCKSZAHL)]")
    clean_num = int(clean_str) if clean_str else 0
    if clean_num > 0:
        print(f"  - ISBN mod 13: {clean_num % 13}")
        if clean_num % 13 == 0:
            print(f"  *** TEILBAR DURCH 13! ***")
    
    print(f"\n[7-ANALYSE (HEILIGE ZAHL)]")
    if clean_num > 0:
        print(f"  - ISBN mod 7: {clean_num % 7}")
        if clean_num % 7 == 0:
            print(f"  *** TEILBAR DURCH 7! ***")
    
    print(f"\n[PRIMZAHL-ANALYSE]")
    if clean_num > 0:
        print(f"  - Ist ISBN-Nummer prim? {is_prime(clean_num)}")
        if is_prime(clean_num):
            print(f"  *** ISBN IST PRIMZAHL! ***")
    
    print(f"\n[BEZIEHUNG ZU BELPHEGOR]")
    # Prüfe auf 166, 16661
    if '166' in clean_str:
        print(f"  - '166' gefunden! (Belphegor-Basis)")
    if '16661' in clean_str:
        print(f"  *** '16661' GEFUNDEN! (Belphegor-Zahl) ***")
    
    print(f"\n[JAHR-VERBINDUNG]")
    year_digits = [int(c) for c in str(year)]
    year_sum = sum(year_digits)
    print(f"  - Jahr-Kreuzsumme: {year_sum}")
    print(f"  - Jahr-Digitale-Wurzel: {digital_root(year_sum)}")
    print(f"  - Verbindung Jahr+ISBN-Summe: {year_sum + sum(digits)}")
    
    return {
        'isbn': isbn,
        'title': title,
        'year': year,
        'digit_sum': sum(digits),
        'digital_root': digital_root(sum(digits)),
        'count_6': count_6 if 'count_6' in dir() else clean_str.count('6'),
        'has_666': '666' in clean_str,
        'has_166': '166' in clean_str
    }

def analyze_vampire_numbers():
    """Analysiere die Vampire Numbers aus Wikipedia"""
    print("\n" + "="*70)
    print("VAMPIRE NUMBERS ANALYSE (aus Wikipedia)")
    print("="*70)
    
    vampires = [
        (1260, "21 × 60"),
        (136948, "146 × 938")
    ]
    
    for num, factors in vampires:
        print(f"\n[ANALYSE: {num}]")
        print(f"  - Faktorisierung: {factors}")
        print(f"  - Kreuzsumme: {digit_sum(num)}")
        print(f"  - Digitale Wurzel: {digital_root(num)}")
        print(f"  - Primfaktoren: {prime_factors(num)}")
        
        # Prüfe auf 666-Verbindung
        print(f"  - Differenz zu 666: {abs(num - 666)}")
        print(f"  - 666 mod {num}: {666 % num if num != 0 else 'N/A'}")
        
        # Prüfe auf 13-Verbindung
        print(f"  - {num} mod 13: {num % 13}")
        if num % 13 == 0:
            print(f"  *** TEILBAR DURCH 13! ***")
        
        # Spezielle Eigenschaften
        if num == 1260:
            print(f"  - 1260 = 2² × 3² × 5 × 7")
            print(f"  - 1260 / 666 = {1260/666:.4f}")
            print(f"  - 1260 ist das Produkt von 21 und 60 (halbierte 42 und 60)")
        elif num == 136948:
            print(f"  - 136948 = 2² × 146 × 938... warte")
            pf = prime_factors(136948)
            print(f"  - Tatsächliche Primfaktoren: {pf}")

# Alle ISBNs aus der Wikipedia-Seite
isbn_data = [
    ("0-486-41709-3", "Computers, Pattern, Chaos, and Beauty", 1990),
    ("0-688-16894-9", "Strange Brains and Genius", 1999),
    ("0-691-11597-4", "The Zen of Magic Squares, Circles, and Stars", 2002),
    ("0-521-01678-9", "The Mathematics of Oz", 2002),
    ("1-4039-6457-2", "The Paradox of God and the Science of Omniscience", 2002),
    ("0-471-26987-5", "Calculus and Pizza", 2003),
    ("1-890572-17-9", "Sex, Drugs, Einstein, and Elves", 2005),
    ("0-471-69098-8", "A Passion for Mathematics", 2005),
    ("1-56025-826-8", "The Mobius Strip", 2006),
    ("978-1-56025-984-8", "A Beginner's Guide to Immortality", 2007),
    ("978-1-4303-2969-5", "The Heaven Virus", 2007),
    ("978-0-19-533611-5", "Archimedes to Hawking", 2008),
    ("978-1-4027-6400-4", "The Loom of God", 2009),
    ("978-1-4027-5796-9", "The Math Book", 2009),
    ("978-1-4027-7861-2", "The Physics Book", 2011),
    ("978-1-4027-8585-6", "The Medical Book", 2012),
    ("978-1606600498", "The Book of Black", 2013),
    ("978-1454913221", "The Mathematics Devotional", 2014),
    ("978-1454915546", "The Physics Devotional", 2015),
    ("978-1454914341", "Death and the Afterlife", 2015),
    ("978-1454930068", "The Science Book", 2018),
    ("978-1454933595", "Artificial Intelligence: An Illustrated History", 2019),
    ("0-9714827-9-9", "Egg Drop Soup", 2002),
    ("981-02-0615-1", "Spiral Symmetry", 1992),
]

def analyze_all_isbns():
    """Analysiere alle ISBNs"""
    print("\n" + "="*70)
    print("KOMPLETTE ISBN-ANALYSE ALLER PICKOVER-WERKE")
    print("="*70)
    
    results = []
    for isbn, title, year in isbn_data:
        result = analyze_isbn(isbn, title, year)
        results.append(result)
    
    # Zusammenfassung
    print("\n" + "="*70)
    print("ZUSAMMENFASSUNG ALLER ISBN-ANALYSEN")
    print("="*70)
    
    # Zähle 666-Vorkommen
    has_666_count = sum(1 for r in results if r.get('has_666'))
    has_166_count = sum(1 for r in results if r.get('has_166'))
    
    print(f"\n[STATISTIK]")
    print(f"  - Gesamte ISBNs analysiert: {len(results)}")
    print(f"  - ISBNs mit '666': {has_666_count}")
    print(f"  - ISBNs mit '166' (Belphegor-Basis): {has_166_count}")
    
    # Analysiere Digitale Wurzeln
    roots = [r['digital_root'] for r in results]
    root_counts = Counter(roots)
    print(f"\n[DIGITALE WURZELN VERTEILUNG]")
    for root in sorted(root_counts.keys()):
        print(f"  - Wurzel {root}: {root_counts[root]}x")
    
    # Analysiere 6-Sechser
    six_counts = [r.get('count_6', 0) for r in results]
    print(f"\n[SECHSER-ANALYSE]")
    print(f"  - Durchschnittliche Sechser pro ISBN: {sum(six_counts)/len(six_counts):.2f}")
    print(f"  - Maximale Sechser in einer ISBN: {max(six_counts)}")
    
    # Findet ISBNs mit besonderen Eigenschaften
    print(f"\n[BESONDERE ISBNs]")
    for r in results:
        if r.get('has_666') or r.get('has_166') or r.get('count_6', 0) >= 3:
            print(f"  - {r['isbn']} ({r['title'][:30]}...)")
            if r.get('has_666'):
                print(f"    *** Enthält 666!")
            if r.get('has_166'):
                print(f"    - Enthält 166 (Belphegor)")
            if r.get('count_6', 0) >= 3:
                print(f"    - Hat {r['count_6']} Sechser")

def analyze_years_pattern():
    """Analysiere die Jahre von Pickovers Publikationen"""
    print("\n" + "="*70)
    print("JAHR-MUSTER ANALYSE (1990-2019)")
    print("="*70)
    
    years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1997, 1998, 1998, 1998, 
             1999, 1999, 2000, 2000, 2000, 2001, 2001, 2002, 2002, 2002, 2002, 2002,
             2003, 2005, 2005, 2006, 2007, 2007, 2008, 2009, 2009, 2011, 2012, 2012,
             2013, 2014, 2015, 2015, 2018, 2019]
    
    print(f"\n[JAHR-STATISTIK]")
    print(f"  - Erste Publikation: {min(years)}")
    print(f"  - Letzte Publikation: {max(years)}")
    print(f"  - Aktive Jahre: {max(years) - min(years)} Jahre")
    print(f"  - Gesamte Bücher: {len(years)}")
    
    # Kreuzsummen der Jahre
    print(f"\n[KREUZSUMMEN DER WICHTIGSTEN JAHRE]")
    important_years = [1957, 1982, 1990, 2009, 2011, 2014]
    for year in important_years:
        ds = digit_sum(year)
        dr = digital_root(ds)
        print(f"  - {year}: Kreuzsumme={ds}, Digitale Wurzel={dr}")
        
        # Verbindung zu 666
        diff = abs(year - 666)
        if year < 666:
            print(f"    Differenz zu 666: {diff}")
        
        # Verbindung zu 13
        print(f"    {year} mod 13 = {year % 13}")
        if year % 13 == 0:
            print(f"    *** TEILBAR DURCH 13! ***")

def analyze_57th_dimension():
    """Analysiere die 57. Dimension"""
    print("\n" + "="*70)
    print("ANALYSE: '57th Dimension' (aus 'The Math Book')")
    print("="*70)
    
    print(f"\n[Zahl 57]")
    print(f"  - Kreuzsumme: {digit_sum(57)}")
    print(f"  - Digitale Wurzel: {digital_root(57)}")
    print(f"  - Primfaktoren: {prime_factors(57)}")
    print(f"  - 57 = 3 × 19")
    print(f"  - 5 + 7 = 12 → 3 (Dreifaltigkeit)")
    
    print(f"\n[BEZIEHUNG ZU BELPHEGOR]")
    print(f"  - 666 mod 57 = {666 % 57}")
    print(f"  - 57 mod 666 = 57")
    print(f"  - 666 / 57 = {666/57:.4f}")
    print(f"  - 57 × 11 = {57*11} (fast 666, Differenz: {666-57*11})")
    
    print(f"\n[MATHEMATISCHE EIGENSCHAFTEN]")
    print(f"  - 57 mod 7 = {57 % 7}")
    print(f"  - 57 mod 9 = {57 % 9}")
    print(f"  - Ist 57 prim? {is_prime(57)}")
    print(f"  - 57 in Binär: {bin(57)}")
    print(f"  - 57 in Hex: {hex(57)}")

def analyze_700_patents():
    """Analysiere die 700 Patente"""
    print("\n" + "="*70)
    print("ANALYSE: '700+ US Patente'")
    print("="*70)
    
    print(f"\n[Zahl 700]")
    print(f"  - Kreuzsumme: {digit_sum(700)}")
    print(f"  - Digitale Wurzel: {digital_root(700)}")
    print(f"  - Primfaktoren: {prime_factors(700)}")
    print(f"  - 700 = 2² × 5² × 7")
    print(f"  - 7+0+0 = 7 (heilige Zahl!)")
    
    print(f"\n[BEZIEHUNG ZU 666]")
    print(f"  - 700 - 666 = {700 - 666}")
    print(f"  - 700 + 666 = {700 + 666}")
    print(f"  - 700 mod 666 = {700 % 666}")
    print(f"  - 666 mod 700 = 666")
    
    print(f"\n[BEZIEHUNG ZU BELPHEGOR-INDIZES]")
    indices = [1, 14, 43, 507, 609, 2473, 2624, 28292, 181299]
    for idx in indices:
        if 700 % idx == 0:
            print(f"  *** 700 teilbar durch {idx}! ***")
    
    print(f"\n[BEZIEHUNG ZU 13]")
    print(f"  - 700 mod 13 = {700 % 13}")
    print(f"  - 700 / 13 = {700/13:.4f}")

def analyze_50_books():
    """Analysiere die 50+ Bücher"""
    print("\n" + "="*70)
    print("ANALYSE: '50+ Bücher'")
    print("="*70)
    
    print(f"\n[Zahl 50]")
    print(f"  - Kreuzsumme: {digit_sum(50)}")
    print(f"  - Digitale Wurzel: {digital_root(50)}")
    print(f"  - Primfaktoren: {prime_factors(50)}")
    print(f"  - 50 = 2 × 5²")
    print(f"  - 5 + 0 = 5 (Zahl der Menschlichkeit/Mitte)")
    
    print(f"\n[BEZIEHUNG ZU 666]")
    print(f"  - 666 mod 50 = {666 % 50}")
    print(f"  - 50 mod 666 = 50")
    print(f"  - 666 / 50 = {666/50:.2f}")
    
    print(f"\n[BEZIEHUNG ZU BELPHEGOR-INDIZES]")
    print(f"  - 50 - 43 = {50-43} (Differenz zu Index 3)")
    print(f"  - 50 + 1 = {50+1} (Index 1)")
    
    print(f"\n[BEZIEHUNG ZU 13]")
    print(f"  - 50 mod 13 = {50 % 13}")
    print(f"  - 50 / 13 = {50/13:.4f}")

# Hauptausführung
if __name__ == "__main__":
    print("="*70)
    print("TIEFE ZAHLENANALYSE: WIKIPEDIA - CLIFFORD A. PICKOVER")
    print("="*70)
    print("Quelle: https://en.wikipedia.org/wiki/Clifford_A._Pickover")
    print("="*70)
    
    # Führe alle Analysen durch
    analyze_all_isbns()
    analyze_vampire_numbers()
    analyze_years_pattern()
    analyze_57th_dimension()
    analyze_700_patents()
    analyze_50_books()
    
    print("\n" + "="*70)
    print("ANALYSE ABGESCHLOSSEN")
    print("="*70)
    print("\nAlle Analysen basieren auf Daten von:")
    print("- https://en.wikipedia.org/wiki/Clifford_A._Pickover")
    print("- OEIS A156166 (https://oeis.org/A156166)")
    print("- Pickovers offizielle Website (https://www.pickover.com)")
