"""
Tiefe Analyse versteckter IDs, Zeitstempel und Kuriositäten
Untersucht OEIS-Revision-IDs, Wikipedia-Edit-IDs, ISBN-Prüfziffern, etc.
"""

import math
from datetime import datetime

def digit_sum(n):
    return sum(int(d) for d in str(abs(n)) if d.isdigit())

def digital_root(n):
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

def analyze_oeis_ids():
    print("="*70)
    print("OEIS VERSTECKTE IDs UND ZEITSTEMPEL")
    print("="*70)
    
    print("\n[1] M. F. HASLER PROFIL-DATEN")
    print("  - Letzte Bearbeitung: 4. März 2025, 18:13 Uhr")
    print("  - Revision ID: 1663265")
    print("  - Analyse von 1663265:")
    
    rev_id = 1663265
    print(f"    - Kreuzsumme: {digit_sum(rev_id)} -> {digital_root(rev_id)}")
    print(f"    - Primzahl? {is_prime(rev_id)}")
    print(f"    - 1663265 mod 666 = {rev_id % 666}")
    print(f"    - 1663265 mod 13 = {rev_id % 13}")
    print(f"    - 1663265 mod 7 = {rev_id % 7}")
    print(f"    - Enthält '666'? {'666' in str(rev_id)}")
    print(f"    - Enthält '166'? {'166' in str(rev_id)} (Belphegor-Basis!)")
    
    print("\n  - Datum: 4. März 2025")
    date_nums = [4, 3, 2025]
    print(f"    - 4+3+2025 = {sum(date_nums)}")
    print(f"    - Digitale Wurzel: {digital_root(sum(date_nums))}")
    print(f"    - 2025 mod 666 = {2025 % 666}")
    print(f"    - 2025 mod 13 = {2025 % 13}")
    
    print("\n  - Uhrzeit: 18:13")
    print(f"    - 1+8+1+3 = {1+8+1+3}")
    print(f"    - 18:13 als Zahl: 1813")
    print(f"    - 1813 mod 666 = {1813 % 666}")
    print(f"    - 1813 mod 13 = {1813 % 13}")
    
    print("\n[2] A156166 EINREICHUNGSDATEN (10. Februar 2009)")
    print("  - Datum: 10. Februar 2009")
    print(f"    - 10+2+2009 = {10+2+2009}")
    print(f"    - Digitale Wurzel: {digital_root(10+2+2009)}")
    print(f"    - 2009 mod 666 = {2009 % 666}")
    print(f"    - 2009 mod 13 = {2009 % 13} (HEILIGE 7!)")
    print(f"    - 10+2 = 12 -> 3 (Dreifaltigkeit)")

def analyze_isbn_checkdigits():
    print("\n" + "="*70)
    print("ISBN-PRÜFZIFFERN-ANALYSE")
    print("="*70)
    
    def isbn13_check(isbn):
        isbn_clean = isbn.replace('-', '').replace(' ', '')
        if len(isbn_clean) != 13:
            return None
        total = 0
        for i, digit in enumerate(isbn_clean[:-1]):
            if i % 2 == 0:
                total += int(digit)
            else:
                total += int(digit) * 3
        check = (10 - (total % 10)) % 10
        return check
    
    isbns = [
        "978-1-4027-5796-9",
        "978-1-4027-8829-1",
        "978-1606600498",
        "978-1454913221",
    ]
    
    print("\n[ISBN-13 PRÜFZIFFERN]")
    for isbn in isbns:
        clean = isbn.replace('-', '')
        if len(clean) == 13:
            provided_check = int(clean[-1])
            calculated_check = isbn13_check(isbn)
            
            print(f"\n  ISBN: {isbn}")
            print(f"    - Prüfziffer: {provided_check}")
            print(f"    - Berechnet: {calculated_check}")
            print(f"    - OK: {provided_check == calculated_check}")
            
            if provided_check == calculated_check:
                print(f"    - Spezial: {provided_check in [6, 7, 9] and ('Heilig/Vollkommen' if provided_check in [6,7,9] else 'Normal')}")

def analyze_hidden_patterns():
    print("\n" + "="*70)
    print("VERSTECKTE MUSTER")
    print("="*70)
    
    print("\n[1] A156166 ZAHLENMUSTER")
    seq = "156166"
    print(f"  - Roh: {seq}")
    print(f"    - '666' bei Position: {seq.find('666')}")
    print(f"    - '166' kommt: {seq.count('166')}x")
    print(f"    - Rückwärts: {seq[::-1]}")
    
    print("\n[2] BELPHEGOR-INDIZES")
    indices = [1, 14, 43, 507, 609, 2473, 2624, 28292, 181299]
    print("  - Als Zeitmarken:")
    for i, idx in enumerate(indices, 1):
        h, rem = divmod(idx, 3600)
        m, s = divmod(rem, 60)
        print(f"    {i}. {idx:>6} = {h}h {m}m {s}s")

if __name__ == "__main__":
    analyze_oeis_ids()
    analyze_isbn_checkdigits()
    analyze_hidden_patterns()
