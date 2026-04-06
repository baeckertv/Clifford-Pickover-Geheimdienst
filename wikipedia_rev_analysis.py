"""
Analyse versteckter Muster in Wikipedia Revision IDs
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

# Wikipedia Revision IDs von Clifford A. Pickover
rev_ids = [
    1338085818, 1309713054, 1305617408, 1280283943, 1270906297,
    1241057353, 1223231298, 1218724506, 1190408848, 1189687532,
    1175072371, 1164648660, 1147709847, 1146535506, 1115925198,
    1105128335, 1085705129, 1077400337, 1076314855, 1026232095
]

print("="*70)
print("WIKIPEDIA REVISION IDs ANALYSE")
print("Clifford A. Pickover Artikel - History")
print("="*70)

print("\n[ANALYSE ALLER 20 REVISION IDs]")
print("-" * 70)

suspicious = []

for i, rev_id in enumerate(rev_ids, 1):
    rev_str = str(rev_id)
    ds = digit_sum(rev_id)
    dr = digital_root(rev_id)
    
    print(f"\n{i}. ID: {rev_id}")
    print(f"   - Kreuzsumme: {ds} -> Wurzel: {dr}")
    print(f"   - mod 666: {rev_id % 666}")
    print(f"   - mod 13: {rev_id % 13}")
    print(f"   - mod 7: {rev_id % 7}")
    
    # Prüfe auf verdächtige Muster
    markers = []
    if '666' in rev_str:
        markers.append("*** ENTHÄLT 666!")
    if '166' in rev_str:
        markers.append("Enthält 166 (Belphegor)")
    if dr == 6:
        markers.append("Wurzel 6 (666-Resonanz)")
    if dr == 7:
        markers.append("Wurzel 7 (Heilig)")
    if rev_id % 666 == 0:
        markers.append("*** TEILBAR DURCH 666!")
    if rev_id % 13 == 0:
        markers.append("*** TEILBAR DURCH 13!")
    
    if markers:
        print(f"   - MARKER: {' | '.join(markers)}")
        suspicious.append((rev_id, markers))

print("\n" + "="*70)
print("VERDÄCHTIGE IDs ZUSAMMENFASSUNG")
print("="*70)

if suspicious:
    print(f"\n{len(suspicious)} von {len(rev_ids)} IDs haben auffällige Muster:")
    for rev_id, markers in suspicious:
        print(f"  - {rev_id}: {', '.join(markers)}")
else:
    print("\nKeine der IDs hat offensichtliche 666/13/7-Muster.")

# Analysiere die neueste ID (1338085818) tiefgehend
print("\n" + "="*70)
print("TIEFANALYSE: NEUESTE ID 1338085818 (13 Feb 2026)")
print("="*70)

latest = 1338085818
latest_str = str(latest)

print(f"\nRoh-ID: {latest}")
print(f"- Länge: {len(latest_str)} Ziffern")
print(f"- Kreuzsumme: {digit_sum(latest)} -> {digital_root(latest)}")
print(f"- Primzahl? {is_prime(latest)}")

# Ziffernanalyse
print("\n[ZIFFERNANALYSE]")
for d in range(10):
    count = latest_str.count(str(d))
    if count > 0:
        print(f"  - Ziffer {d}: {count}x")

print("\n[POSITIONALE MUSTER]")
print(f"- Erste 3 Ziffern: {latest_str[:3]} (133)")
print(f"- Letzte 3 Ziffern: {latest_str[-3:]} (818)")
print(f"- Mitte (4-6): {latest_str[3:6]} (808)")
print(f"- 133 + 808 + 5818 = {133 + 808 + 5818}")
print(f"- 1+3+3+8+0+8+5+8+1+8 = {digit_sum(latest)}")

# Spezielle Prüfungen
print("\n[SPEZIELLE PRÜFUNGEN]")
print(f"- Enthält '666'? {'666' in latest_str}")
print(f"- Enthält '133'? {'133' in latest_str} (Anfang!)")
print(f"- Enthält '888'? {'888' in latest_str}")
print(f"- Spiegelung: {latest_str[::-1]} (8185808331)")

# Modulo-Analyse
print("\n[MODULO-ANALYSE]")
for mod in [6, 7, 13, 37, 73, 666]:
    print(f"- mod {mod}: {latest % mod}")

# Vergleich mit Belphegor-Indizes
print("\n[VERGLEICH MIT BELPHEGOR-INDIZES]")
belphegor = [1, 14, 43, 507, 609, 2473, 2624, 28292, 181299]
for idx in belphegor:
    if latest % idx == 0:
        print(f"  *** TEILBAR DURCH Belphegor-Index {idx}!")

print("\n" + "="*70)
print("ZEITSTEMPEL-ANALYSE")
print("="*70)

# Die Zeitstempel vom 13. Februar 2026
print("\nDatum: 13. Februar 2026")
print("- 13 = Unglückszahl")
print("- Februar = 2. Monat")
print("- 2026 = 2+0+2+6 = 10 -> 1")
print("- 13+2+2026 = 2041 -> 2+0+4+1 = 7 (HEILIG!)")

print("\n" + "="*70)
print("VERBINDUNG ZU A156166")
print("="*70)

seq_num = 156166
print(f"\nA156166 als Zahl: {seq_num}")
print(f"- 1338085818 mod {seq_num} = {latest % seq_num}")

# Versuche eine Verbindung zu finden
conn = abs(latest - seq_num)
print(f"- Differenz: {conn}")
print(f"- Differenz mod 666: {conn % 666}")
print(f"- Differenz mod 13: {conn % 13}")

print("\n" + "="*70)
print("FERTIG")
print("="*70)
