import csv
import os

csv_dosya1 = "/your/folder/path"
csv_dosya2 = "/your/folder/path"

# CSV dosyalarını oku ve uzantıları kaldırarak isimleri bir küme olarak dön
def csv_dosyasini_oku_ve_duzenle(dosya_yolu):
    with open(dosya_yolu, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        veri = {os.path.splitext(row[0].strip())[0] for row in reader if row}  # Uzantıyı kaldır ve boş satırları filtrele
        return veri

# CSV dosyalarını yükle
veriler1 = csv_dosyasini_oku_ve_duzenle(csv_dosya1)
veriler2 = csv_dosyasini_oku_ve_duzenle(csv_dosya2)

# Fazladan öğeyi bul
fazladan_oge = veriler1.symmetric_difference(veriler2)

# Sonuçları yazdır
if fazladan_oge:
    print("Fazladan öğe(ler):", fazladan_oge)
else:
    print("İki dosyadaki veriler tamamen aynı.")
