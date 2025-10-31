"""
Perulangan dengan while samopai paham
"""
books = 10
books_read = 0
books_understood = 0

print('Ibu berkata, "Baca dan pahami semua bukumu"\n')
print(f"Jumlah buku yang sudah dibaca dan dipahami =  {books_understood}\n")

while books_read < books * 2:
    books_read = books_read + 1
    if  books_understood == 9:
        print(f"Buku ke {books_understood + 1} belum paham")
    else:
        books_understood = books_understood + 1
        print(f"Buku ke sudah dibaca dan dipahami {books_understood}")

print(f"Jumlah buku yang sudah dibaca dan dipahami = {books_understood}")

if books_understood == books:
    print("Bu, semua buku sudah dibaca dan dipahami")
else:
    print(f"Bu, tidak semua buku dipahami. "
          f"Budi hanya bisa memahami {books_understood} buku")