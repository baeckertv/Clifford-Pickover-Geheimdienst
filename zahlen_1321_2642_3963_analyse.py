"""
TIEFANALYSE: 1321, 2642, 3963
Untersuchung der Zahlen und ihrer Beziehungen zu 333, 666, 999
"""

import math

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

def prime_factors(n):
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

def triangle_number(n):
    return n * (n + 1) // 2

print("="*80)
print("TIEFANALYSE: 1321, 2642, 3963")
print("Beziehungen zu 333, 666, 999")
print("="*80)

zahlen = [1321, 2642, 3963]
teiler = [333, 666, 999]

# ============================================================
# TEIL 1: GRUNDANALYSE DER ZAHLEN
# ============================================================
print("\n" + "="*80)
print("TEIL 1: GRUNDANALYSE VON 1321, 2642, 3963")
print("="*80)

for zahl in zahlen:
    print(f"\n{'='*60}")
    print(f"ZAHL: {zahl}")
    print(f"{'='*60}")
    
    # Grundlegende Eigenschaften
    print(f"\n[GRUNDEIGENSCHAFTEN]")
    print(f"  Kreuzsumme: {digit_sum(zahl)}")
    print(f"  Digitale Wurzel: {digital_root(zahl)}")
    
    dr = digital_root(zahl)
    if dr == 7:
        print(f"  *** WURZEL 7 - HEILIGE ZAHL! ***")
    elif dr == 6:
        print(f"  *** WURZEL 6 - 666-RESONANZ! ***")
    elif dr == 9:
        print(f"  *** WURZEL 9 - VOLLKOMMENHEIT! ***")
    
    # Primzahltest
    if is_prime(zahl):
        print(f"  *** IST PRIMZAHL! ***")
    else:
        pf = prime_factors(zahl)
        print(f"  Primfaktoren: {pf}")
        if 7 in pf:
            print(f"  *** Enthält HEILIGE 7! ***")
        if 13 in pf:
            print(f"  *** Enthält UNGLÜCKSZAHL 13! ***")
    
    # Modulo-Analyse
    print(f"\n[MODULO-ANALYSE]")
    print(f"  mod 13: {zahl % 13} {'(HEILIGE 7!)' if zahl % 13 == 7 else '(666-Resonanz)' if zahl % 13 == 6 else ''}")
    print(f"  mod 7: {zahl % 7} {'(TEILBAR!)' if zahl % 7 == 0 else ''}")
    print(f"  mod 666: {zahl % 666}")
    print(f"  mod 333: {zahl % 333}")
    print(f"  mod 999: {zahl % 999}")
    
    # Spezielle Muster
    z_str = str(zahl)
    print(f"\n[MUSTER IM ZAHLENSTRING '{z_str}']")
    
    # Aufsteigend/Absteigend
    if len(z_str) >= 3:
        ziffern = [int(c) for c in z_str]
        if ziffern[0] < ziffern[1] < ziffern[2]:
            print(f"  Aufsteigende Sequenz: {ziffern[0]} < {ziffern[1]} < {ziffern[2]}")
        if ziffern[0] > ziffern[1] > ziffern[2]:
            print(f"  Absteigende Sequenz: {ziffern[0]} > {ziffern[1]} > {ziffern[2]}")
    
    # Palindrom-Teile
    if len(z_str) >= 4:
        first_half = z_str[:2]
        second_half = z_str[2:]
        if first_half == second_half[::-1]:
            print(f"  *** Spiegelung: {first_half} | {second_half} ***")
    
    # Wiederholungen
    for i in range(len(z_str) - 1):
        if z_str[i] == z_str[i+1]:
            print(f"  Wiederholung: {z_str[i]} wiederholt an Position {i}")

# ============================================================
# TEIL 2: DIVISION DURCH 333, 666, 999
# ============================================================
print("\n" + "="*80)
print("TEIL 2: DIVISION DURCH 333, 666, 999")
print("="*80)

for zahl in zahlen:
    print(f"\n{'='*60}")
    print(f"ZAHL: {zahl}")
    print(f"{'='*60}")
    
    for t in teiler:
        print(f"\n  Division durch {t}:")
        quotient = zahl / t
        ganzzahl = zahl // t
        rest = zahl % t
        
        print(f"    {zahl} ÷ {t} = {quotient:.6f}")
        print(f"    Ganzzahliger Anteil: {ganzzahl}")
        print(f"    Rest: {rest}")
        
        if rest == 0:
            print(f"    *** EXAKT TEILBAR! {zahl} = {ganzzahl} × {t} ***")
        elif rest == 7:
            print(f"    *** REST = 7 (HEILIG!) ***")
        elif rest == 6:
            print(f"    *** REST = 6 (666-Resonanz!) ***")
        
        # Analyse des Quotienten
        if quotient > 1 and quotient < 10:
            print(f"    Quotient {quotient:.2f} ist zwischen 1 und 10")

# ============================================================
# TEIL 3: BEZIEHUNGEN ZWISCHEN DEN ZAHLEN
# ============================================================
print("\n" + "="*80)
print("TEIL 3: BEZIEHUNGEN ZWISCHEN 1321, 2642, 3963")
print("="*80)

print("\n[3.1] DIFFERENZEN UND VERHÄLTNISSE]")
print(f"  2642 - 1321 = {2642 - 1321}")
print(f"  3963 - 2642 = {3963 - 2642}")
print(f"  3963 - 1321 = {3963 - 1321}")

print(f"\n  2642 ÷ 1321 = {2642 / 1321:.6f}")
print(f"  3963 ÷ 2642 = {3963 / 2642:.6f}")
print(f"  3963 ÷ 1321 = {3963 / 1321:.6f}")

# Sind es Vielfache?
print("\n[3.2] VIELFACHEN-ANALYSE]")
for i, z1 in enumerate(zahlen):
    for j, z2 in enumerate(zahlen):
        if i != j:
            if z2 % z1 == 0:
                f = z2 // z1
                print(f"  *** {z2} = {f} × {z1} ***")

# Arithmetische Progression?
print("\n[3.3] ARITHMETISCHE PROGRESSION?]")
diff1 = 2642 - 1321
diff2 = 3963 - 2642
print(f"  Differenz 1: {diff1}")
print(f"  Differenz 2: {diff2}")
if diff1 == diff2:
    print(f"  *** ARITHMETISCHE PROGRESSION! Gemeinsame Differenz: {diff1} ***")
else:
    print(f"  Keine arithmetische Progression ({diff1} ≠ {diff2})")

# Geometrische Progression?
print("\n[3.4] GEOMETRISCHE PROGRESSION?]")
if 2642**2 == 1321 * 3963:
    print(f"  *** GEOMETRISCHE PROGRESSION! 2642² = 1321 × 3963 ***")
else:
    print(f"  2642² = {2642**2}")
    print(f"  1321 × 3963 = {1321 * 3963}")
    print(f"  Differenz: {abs(2642**2 - 1321 * 3963)}")

# ============================================================
# TEIL 4: BEZIEHUNGEN ZU 333, 666, 999
# ============================================================
print("\n" + "="*80)
print("TEIL 4: SYSTEMATISCHE BEZIEHUNGEN ZU 333, 666, 999")
print("="*80)

print("\n[4.1] STRUKTUR VON 333, 666, 999]")
for t in teiler:
    print(f"\n  {t}:")
    print(f"    Kreuzsumme: {digit_sum(t)} -> Wurzel: {digital_root(t)}")
    pf = prime_factors(t)
    print(f"    Primfaktoren: {pf}")
    
    if t == 333:
        print(f"    333 = 3 × 111 = 3 × 3 × 37 = 9 × 37")
    elif t == 666:
        print(f"    666 = 2 × 333 = 2 × 3 × 111 = 2 × 9 × 37")
        print(f"    666 = T_36 (36. dreieckige Zahl)")
    elif t == 999:
        print(f"    999 = 3 × 333 = 27 × 37 = 3³ × 37")

# Multiplikationstabellen
print("\n[4.2] MULTIPLIKATIONSTABELLE]")
print(f"\n{'n':<5} {'n×333':<10} {'n×666':<10} {'n×999':<10}")
print("-" * 40)
for n in range(1, 13):
    print(f"{n:<5} {n*333:<10} {n*666:<10} {n*999:<10}")

# Wo tauchen unsere Zahlen auf?
print("\n[4.3] POSITION VON 1321, 2642, 3963 IN DER MULTIPLIKATIONSTABELLE")
for zahl in zahlen:
    print(f"\n  {zahl}:")
    for t in teiler:
        quotient = zahl / t
        if quotient == int(quotient):
            print(f"    *** {zahl} = {int(quotient)} × {t} ***")
        else:
            naechstes_kleiner = (zahl // t) * t
            naechstes_groesser = ((zahl // t) + 1) * t
            print(f"    Liegt zwischen {naechstes_kleiner} ({zahl//t}×{t}) und {naechstes_groesser} ({zahl//t+1}×{t})")

# ============================================================
# TEIL 5: VERBINDUNGEN ZU PICKOVER-ZAHLEN
# ============================================================
print("\n" + "="*80)
print("TEIL 5: VERBINDUNGEN ZU PICKOVER-ZAHLEN")
print("="*80)

pickover_zahlen = {
    "Geburt": 1957,
    "PhD": 1982,
    "Math Book": 2009,
    "666": 666,
    "700 Patente": 700,
    "609 Belphegor": 609,
    "57 Dimension": 57,
}

print("\n[5.1] DIFFERENZEN ZU PICKOVER-ZAHLEN]")
for p_name, p_zahl in pickover_zahlen.items():
    print(f"\n  Pickover {p_name}: {p_zahl}")
    for zahl in zahlen:
        diff = abs(zahl - p_zahl)
        print(f"    |{zahl} - {p_zahl}| = {diff}")
        if diff < 100:
            print(f"      *** KLEINE DIFFERENZ (<100)! ***")

print("\n[5.2] MODULO-BEZIEHUNGEN]")
for p_name, p_zahl in pickover_zahlen.items():
    print(f"\n  Pickover {p_name}: {p_zahl}")
    for zahl in zahlen:
        mod = zahl % p_zahl if p_zahl != 0 else -1
        if mod != -1 and mod < 100:
            print(f"    {zahl} mod {p_zahl} = {mod}")

# ============================================================
# TEIL 6: KRYPTOGRAPHISCHE UND SYMBOLISCHE ANALYSE
# ============================================================
print("\n" + "="*80)
print("TEIL 6: SYMBOLISCHE UND KRYPTOGRAPHISCHE ANALYSE")
print("="*80)

print("\n[6.1] ZAHLEN ALS DATEN/ZEIT]")
# 1321 als Zeit
print(f"\n  1321 als Uhrzeit: 13:21 (13 Uhr 21 Minuten)")
print(f"    13 + 21 = 34 -> 3+4 = 7 (HEILIG!)")
print(f"    13 × 21 = 273")
print(f"    13:21 ist 1:21 PM (13 = 1, 21 = 3×7)")

# 2642 als Zeit
print(f"\n  2642 als Uhrzeit: 26:42 (ungültig, da > 24)")
print(f"    Aber: 2:6:42 = 2 Stunden 6 Min 42 Sek = 2:06:42")

# 3963 als Zeit  
print(f"\n  3963 als Uhrzeit: 39:63 (ungültig)")
print(f"    Aber: 3:9:63 = 3 Stunden 9 Min 63 Sek")

print("\n[6.2] ZAHLEN ALS DATUM]")
# Tag.Monat oder Monat.Tag
print(f"\n  1321 als Datum:")
print(f"    Tag 13, Monat 21: 13.21. (21. Monat existiert nicht)")
print(f"    Oder: 1.3.21 = 1. März 2021")

print(f"\n  2642 als Datum:")
print(f"    2.6.42 = 2. Juni 1942 oder 6.2.42 = 6. Februar 1942")

print(f"\n  3963 als Datum:")
print(f"    3.9.63 = 3. September 1963")
print(f"    1963 - 1957 (Pickover Geburt) = 6 Jahre")

# ============================================================
# TEIL 7: ZUSAMMENFASSUNG
# ============================================================
print("\n" + "="*80)
print("TEIL 7: ZUSAMMENFASSUNG DER ENTDECKUNGEN")
print("="*80)

entdeckungen = []

# Analysiere jede Zahl für wichtige Muster
for zahl in zahlen:
    dr = digital_root(zahl)
    mod_7 = zahl % 7
    mod_13 = zahl % 13
    
    if dr == 7:
        entdeckungen.append(f"{zahl}: Wurzel 7 (heilig)")
    if mod_7 == 0:
        entdeckungen.append(f"{zahl}: Teilbar durch 7")
    if mod_13 == 7:
        entdeckungen.append(f"{zahl}: mod 13 = 7 (heilig)")
    if mod_13 == 6:
        entdeckungen.append(f"{zahl}: mod 13 = 6 (666-Resonanz)")

# Beziehungen zu 333/666/999
for zahl in zahlen:
    for t in teiler:
        if zahl % t == 0:
            f = zahl // t
            entdeckungen.append(f"{zahl} = {f} × {t}")

# Arithmetische Beziehungen
if 2642 - 1321 == 3963 - 2642:
    entdeckungen.append(f"Arithmetische Progression: 1321, 2642, 3963 (Diff={2642-1321})")

print(f"\n[WICHTIGSTE ENTDECKUNGEN:]")
for i, entdeckung in enumerate(entdeckungen, 1):
    print(f"  {i}. {entdeckung}")

if not entdeckungen:
    print(f"\n  Keine statistisch signifikanten Muster gefunden.")
    print(f"  Die Zahlen 1321, 2642, 3963 scheinen 'normal' zu sein.")

print(f"\n[STATISTISCHE BEWERTUNG:]")
print(f"  Anzahl geprüfter Zahlen: 3")
print(f"  Anzahl geprüfter Teiler: 3 (333, 666, 999)")
print(f"  Anzahl gefundener signifikanter Muster: {len(entdeckungen)}")

print("\n" + "="*80)
print("ANALYSE ABGESCHLOSSEN")
print("="*80)
