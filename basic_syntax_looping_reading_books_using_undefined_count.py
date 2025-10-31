"""
Perulangan dengan while samopai paham
"""
books = 10
books_read_total = 0
books_read_and_understood = 0

print('Ibu berkata, "Baca dan pahami semua bukumu"\n')
print(f"Jumlah buku yang sudah dibaca dan dipahami =  {books_read_and_understood}\n")

while books_read_total < books * 2:
    books_read_total = books_read_total + 1
    if  books_read_and_understood == 9:
        print(f"Buku ke {books_read_and_understood + 1} belum paham")
    else:
        books_read_and_understood = books_read_and_understood + 1
        print(f"Buku ke sudah dibaca dan dipahami {books_read_and_understood}")

print(f"Jumlah buku yang sudah dibaca dan dipahami = {books_read_and_understood}")

if books_read_and_understood == books:
    print("Bu, semua buku sudah dibaca dan dipahami")
else:
    print(f"Bu, tidak semua buku dipahami. "
          f"Budi hanya bisa memahami {books_read_and_understood} buku")