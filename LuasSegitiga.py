def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

alas = float(input("Masukkan alas Segitiga: "))
tinggi = float(input("Masukkan tinggi Segitiga: "))
print(f"Luas Segitiga: {luas_segitiga(alas, tinggi)}cm²")