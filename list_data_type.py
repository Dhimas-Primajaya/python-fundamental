books_list = ['rich dad poor dad', 'How to influence people', 'The Warren Buffet Way', 'The Intelligent Investor']
print('Tampilkan variable books_list:')
print(books_list)

print('\nProses semua dengan for in:')
for book in books_list:
    print(book)

print('\nTampilkan isi books_list pada index tertentu:')
print(books_list[2])

print('\nTampilkan dengan for in range:')
for i in range(0, len(books_list)):
    print(books_list[i])


print('\nTampilkan dengan for in range dimana tiap tipe data berbeda:')
books_list = [1, 'Security Analysis', 3.14]
for i in range(0, len(books_list)):
    print(books_list[i])


print('\nKembalikan nilai awal books_list:')
books_list = ['rich dad poor dad', 'How to influence people', 'The Warren Buffet Way', 'The Intelligent Investor']
print('Tambahkan buku baru:')
books_list.append('The Outsiders')
for i in range(0, len(books_list)):
    print(books_list[i])

print('\nClear List')
books_list.clear()
for i in range(0, len(books_list)):
    print(books_list[i])

print('\nGanti elemen pertama:')
books_list = ['rich dad poor dad', 'How to influence people', 'The Warren Buffet Way', 'The Intelligent Investor']
books_list[0] = 'Common Stocks and Uncommon Profits'
for i in range(0, len(books_list)):
    print(books_list[i])

print('\nAmbil elemen ke-2:')
# books_list.pop(1)
# kalau pakai yang diatas cuma bisa di ambil namun tidak dapat dikembalikan, karena tidak ada variable
book = books_list.pop(1)
for i in range(0, len(books_list)):
    print(books_list[i])

print('\nbuku yang diambil tadi:')
print(book)

print('\nPop tanpa menggunakan parameter (nomor index):')
books_list.pop()
for i in range(0, len(books_list)):
    print(books_list[i])
print('Maka yang diambil adalah yang paling belakang di list')

print('\nPop Menggunakan tanda negatif/Minus ( - ):')
books_list = ['rich dad poor dad', 'How to influence people', 'The Warren Buffet Way', 'The Intelligent Investor']
books_list.pop(-2)
for i in range(0, len(books_list)):
    print(books_list[i])
print('Maka yang diambil adalah nomor 2 dari belakang')
print('Pop Seperti ini berguna untuk tipe data stack')

