def volume_tabung(jari_jari, tinggi):
    return 3.14 * jari_jari ** 2 * tinggi

jari_jari = float(input("Masukkan jari-jari Tabung: "))
tinggi = float(input("Masukkan tinggi Tabung: "))
print(f"Volume Tabung: {volume_tabung(jari_jari, tinggi)}cm³")