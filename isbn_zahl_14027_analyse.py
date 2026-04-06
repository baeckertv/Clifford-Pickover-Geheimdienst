"""
ANALYSE: Die ISBN-Zahlen-Sequenz 97814027 / 14027 / 4027
Neue Entdeckung in Pickover-ISBNs
"""

print("="*80)
print("ANALYSE: Die ISBN-Zahlen-Sequenz 97814027 / 14027 / 4027")
print("="*80)

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

# ============================================================
# TEIL 1: ANALYSE DER VOLLSTAENDIGEN SEQUENZ 97814027
# ============================================================
print("\n" + "="*80)
print("TEIL 1: ANALYSE VON 97814027")
print("="*80)

zahl = 97814027
print(f"\n[1.1] GRUNDEIGENSCHAFTEN VON {zahl}")
print(f"  Zahl: {zahl}")
print(f"  Länge: {len(str(zahl))} Ziffern")
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

# Modulo-Analyse
print(f"\n[1.2] MODULO-ANALYSE]")
print(f"  mod 666: {zahl % 666}")
print(f"  mod 13: {zahl % 13} {'(HEILIGE 7!)' if zahl % 13 == 7 else '(666-Resonanz)' if zahl % 13 == 6 else ''}")
print(f"  mod 7: {zahl % 7} {'(TEILBAR!)' if zahl % 7 == 0 else ''}")
print(f"  mod 1957: {zahl % 1957}")
print(f"  mod 2009: {zahl % 2009}")

# ============================================================
# TEIL 2: ANALYSE VON 14027
# ============================================================
print("\n" + "="*80)
print("TEIL 2: ANALYSE VON 14027")
print("="*80)

zahl = 14027
print(f"\n[2.1] GRUNDEIGENSCHAFTEN VON {zahl}")
print(f"  Zahl: {zahl}")
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
print(f"\n[2.2] MODULO-ANALYSE]")
print(f"  mod 666: {zahl % 666}")
print(f"  mod 13: {zahl % 13} {'(HEILIGE 7!)' if zahl % 13 == 7 else '(666-Resonanz)' if zahl % 13 == 6 else ''}")
print(f"  mod 7: {zahl % 7} {'(TEILBAR!)' if zahl % 7 == 0 else ''}")

# Spezielle Muster
z_str = str(zahl)
print(f"\n[2.3] MUSTER IM ZAHLENSTRING '{z_str}']")

# Enthält 14 (Pickover's Geburtsdatum - Tag/Monat)
if "14" in z_str:
    print(f"  *** Enthält '14' (wie 14.08. Geburtstag!) ***")

# Enthält 27
if "27" in z_str:
    print(f"  *** Enthält '27' ***")
    # 27 = 3³
    print(f"  27 = 3³ (Kubus der Dreifaltigkeit)")

# ============================================================
# TEIL 3: ANALYSE VON 4027
# ============================================================
print("\n" + "="*80)
print("TEIL 3: ANALYSE VON 4027")
print("="*80)

zahl = 4027
print(f"\n[3.1] GRUNDEIGENSCHAFTEN VON {zahl}")
print(f"  Zahl: {zahl}")
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

# Modulo-Analyse
print(f"\n[3.2] MODULO-ANALYSE]")
print(f"  mod 666: {zahl % 666}")
print(f"  mod 13: {zahl % 13} {'(HEILIGE 7!)' if zahl % 13 == 7 else '(666-Resonanz)' if zahl % 13 == 6 else ''}")
print(f"  mod 7: {zahl % 7} {'(TEILBAR!)' if zahl % 7 == 0 else ''}")

# ============================================================
# TEIL 4: BEZIEHUNGEN ZWISCHEN DEN ZAHLEN
# ============================================================
print("\n" + "="*80)
print("TEIL 4: BEZIEHUNGEN ZWISCHEN 97814027, 14027, 4027")
print("="*80)

print("\n[4.1] STRUKTURELLE BEZIEHUNGEN]")
print(f"  97814027 enthält 14027: {'14027' in str(97814027)}")
print(f"  14027 enthält 4027: {'4027' in str(14027)}")
print(f"  Position von 14027 in 97814027: Position {str(97814027).find('14027')}")
print(f"  Position von 4027 in 14027: Position {str(14027).find('4027')}")

print(f"\n[4.2] ARITHMETISCHE BEZIEHUNGEN]")
print(f"  97814027 ÷ 14027 = {97814027 / 14027:.6f}")
print(f"  14027 ÷ 4027 = {14027 / 4027:.6f}")
print(f"  97814027 ÷ 4027 = {97814027 / 4027:.6f}")

# Division mit Rest
print(f"\n[4.3] DIVISION MIT REST]")
print(f"  97814027 mod 14027 = {97814027 % 14027}")
print(f"  14027 mod 4027 = {14027 % 4027}")

# ============================================================
# TEIL 5: VERBINDUNGEN ZU PICKOVER-ZAHLEN
# ============================================================
print("\n" + "="*80)
print("TEIL 5: VERBINDUNGEN ZU PICKOVER-ZAHLEN")
print("="*80)

pickover_zahlen = {
    "Geburt 1957": 1957,
    "PhD 1982": 1982,
    "Math Book 2009": 2009,
    "666": 666,
    "700 Patente": 700,
    "609 Belphegor": 609,
    "57 Dimension": 57,
}

print("\n[5.1] DIFFERENZEN UND MODULO]")
for name, p_zahl in pickover_zahlen.items():
    print(f"\n  {name}: {p_zahl}")
    
    # Für 97814027
    diff1 = abs(97814027 - p_zahl)
    mod1 = 97814027 % p_zahl if p_zahl != 0 else -1
    print(f"    97814027: |Diff| = {diff1}, mod = {mod1}")
    
    # Für 14027
    diff2 = abs(14027 - p_zahl)
    mod2 = 14027 % p_zahl if p_zahl != 0 else -1
    print(f"    14027: |Diff| = {diff2}, mod = {mod2}")
    
    # Für 4027
    diff3 = abs(4027 - p_zahl)
    mod3 = 4027 % p_zahl if p_zahl != 0 else -1
    print(f"    4027: |Diff| = {diff3}, mod = {mod3}")

# ============================================================
# TEIL 6: ISBN-KONTEXT
# ============================================================
print("\n" + "="*80)
print("TEIL 6: ISBN-KONTEXT ANALYSE")
print("="*80)

print("""
[6.1] BEKANNTE PICKOVER-ISBNS MIT 978-1-4027-...]

Die ISBN-Struktur für The Math Book und andere Pickover-Werke:
- 978-1-4027-5796-9 (The Math Book Hardcover)
- 978-1-4027-8829-1 (The Math Book Paperback)
- 978-1-4027-7861-2 (The Physics Book)
- 978-1-4027-8585-7 (The Medical Book)

DIE ZAHL 14027 ERSCHEINT ALS:
- Teil der Verlagsnummer (14027)
- Oder als Fragment: 4027

ANALYSE:
- 978 = EAN/ISBN-Praefix
- 1 = Laendercode (USA)
- 4027 = Verlagsnummer (Hachette/Sterling)
- Die restlichen Ziffern = Titelnummer + Pruefziffer
""")

# ============================================================
# TEIL 7: ZUSAMMENFASSUNG
# ============================================================
print("\n" + "="*80)
print("TEIL 7: ZUSAMMENFASSUNG DER ENTDECKUNGEN")
print("="*80)

entdeckungen = []

# Analysiere jede Zahl
for zahl_name, zahl in [("97814027", 97814027), ("14027", 14027), ("4027", 4027)]:
    dr = digital_root(zahl)
    mod_7 = zahl % 7
    mod_13 = zahl % 13
    
    if dr == 7:
        entdeckungen.append(f"{zahl_name}: Wurzel 7 (heilig)")
    if mod_7 == 0:
        entdeckungen.append(f"{zahl_name}: Teilbar durch 7")
    if mod_13 == 7:
        entdeckungen.append(f"{zahl_name}: mod 13 = 7 (heilig)")

# Spezielle Muster
if "14" in str(14027):
    entdeckungen.append("14027 enthält '14' (Geburtstag 14.08.)")

if "27" in str(14027):
    entdeckungen.append("14027 enthält '27' = 3³ (Kubus)")

print(f"\n[WICHTIGSTE ENTDECKUNGEN:]")
for i, entdeckung in enumerate(entdeckungen, 1):
    print(f"  {i}. {entdeckung}")

if not entdeckungen:
    print(f"\n  Keine auffälligen mathematischen Muster gefunden.")
    print(f"  Die Zahl 14027 scheint eine standard Verlagsnummer zu sein.")

print(f"\n[STATISTISCHE BEWERTUNG:]")
print(f"  Anzahl geprüfter Zahlen: 3 (97814027, 14027, 4027)")
print(f"  Anzahl gefundener signifikanter Muster: {len(entdeckungen)}")

print("\n" + "="*80)
print("ANALYSE ABGESCHLOSSEN")
print("="*80)
