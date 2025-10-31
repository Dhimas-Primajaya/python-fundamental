"""
Perulangan dengan while
"""
books = 10
print('Ibu berkata, "Baca semua bukumu"\n')

books_readed = 0
print(f"Jumlah buku yang sudah dibaca {books_readed}\n")

while books_readed < books:
    print("Baca 1 buku yang belum dibaca")
    books_readed = books_readed + 1
    print(f"Jumlah buku yang sudah dibaca {books_readed}\n")

print(f"Jumlah buku yang sudah dibaca {books_readed}")