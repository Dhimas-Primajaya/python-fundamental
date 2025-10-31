"""
Program perulangan membaca buku dengan for
"""

books = 110
print('Ibu berkata, "Baca semua bukumu"\n')

books_readed = 0
print(f"Jumlah buku yang sudah dibaca {books_readed}\n")

for books_readed in range(1, books+1):
    print(f"Buku ke {books_readed} sudah dibaca")

print(f"\nJumlah buku yang sudah dibaca {books_readed}")
