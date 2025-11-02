print('\nPerintah del untuk menghapus')
books_list = ['rich dad poor dad', 'How to influence people', 'The Warren Buffet Way', 'The Intelligent Investor']
del books_list[0]
for i in range(0, len(books_list)):
    print(books_list[i])

print('\nPerintah del dengan List Comprehension')
books_list = ['rich dad poor dad', 'How to influence people', 'The Warren Buffet Way', 'The Intelligent Investor']
del books_list[:]
for i in range(0, len(books_list)):
    print(books_list[i])
print('\njadi books_list[:] = books_list[kiri = start : kanan = stop]')
print('kalau tidak di defenisikan start dan stop nya maka akan menghapus semuanya')

print('\nPerintah del dengan List Comprehension dengan Start dan stop')
books_list = ['rich dad poor dad', 'How to influence people', 'The Warren Buffet Way', 'The Intelligent Investor']
del books_list[0:3]
# atau bisa juga books_list[:3]
for i in range(0, len(books_list)):
    print(books_list[i])

print('\nPerintah del dengan List Comprehension dengan minus')
books_list = ['rich dad poor dad', 'How to influence people', 'The Warren Buffet Way', 'The Intelligent Investor']
del books_list[0:-2] #Start:End
# Hasilnya sama dengan books_list[0:3]
for i in range(0, len(books_list)):
    print(books_list[i])

print('\nPerintah del dengan List Comprehension dengan Step')
books_list = ['rich dad poor dad', 'How to influence people', 'The Warren Buffet Way', 'The Intelligent Investor']
del books_list[0::3] #Start:End:Step
for i in range(0, len(books_list)):
    print(books_list[i])
print('\nJadi disini nanti akan hilang sesuai incrementnya (step = increment) '
      'dan increment nya dihitung menggunakan index bukan jumlah')
print('del books_list[0::3] \nJadi yang di hapus adalah 0 dan increment 3')
print('karena disini index nya dari 0 sampai 3 maka yang dihapus adalah awal dan akhir')

print('\nMembuat List Baru:')
books_list = ['rich dad poor dad', 'How to influence people', 'The Warren Buffet Way', 'The Intelligent Investor']

new_books_list = books_list[:] #Begini caranya dengan menggunakan list comprehension

for i in range(0, len(books_list)):
    print(books_list[i])
print('\nMembuat List Baru (tidak ikutan terhapus karena menggunakan list comprehension.\n'
      'Jika tidak maka akan ikut terhapus. Berikut perbedaan:\n'
      'new_books_list = books_list[:] berbeda dengan new_books_list = books_list\n'
      'yang kiri akan menciptakan list baru walaupun list sebelumnya dihapus\n'
      'sedangkan yang kanan, list baru akan ikut terhapus) :')
del books_list[:]
for i in range(0, len(new_books_list)):
    print(new_books_list[i])

print('\nMembuat List baru dengan Comprehension (ganjil):')
books_list = ['1. rich dad poor dad', '2. How to influence people', '3. The Warren Buffet Way', '4. The Intelligent Investor']
new_books_list = books_list[0::2] #Start:End:Step
for i in range(0, len(new_books_list)):
    print(new_books_list[i])
print('Jadi yang diambil adalah yang index 0 dan index 0+2 dan seterusnya jika ada\n'
      'jadi yang tidak diikutkan dalam list baru adalah index 1 dan 3.\n')

print('\nMembuat List baru dengan Comprehension (genap):')
books_list = ['1. rich dad poor dad', '2. How to influence people', '3. The Warren Buffet Way', '4. The Intelligent Investor']
new_books_list = books_list[1::2] #Start:End:Step
for i in range(0, len(new_books_list)):
    print(new_books_list[i])
print('mulainya dari 1 karena komputer menghitung dari 0 dimana 0 = ganjil dan 1 = genap')

print('\nMembuat List baru dengan Comprehension (buang dari UJUNG):')
books_list = ['1. rich dad poor dad', '2. How to influence people', '3. The Warren Buffet Way', '4. The Intelligent Investor']
new_books_list = books_list[0:-2] #Start:End
for i in range(0, len(new_books_list)):
    print(new_books_list[i])

print('\nMembuat List baru dengan Comprehension (buang dari UJUNG):')
books_list = ['1. rich dad poor dad', '2. How to influence people', '3. The Warren Buffet Way', '4. The Intelligent Investor']
new_books_list = books_list[0:-1:2] #Start:End:Step
for i in range(0, len(new_books_list)):
    print(new_books_list[i])

print('\nMembuat List baru dengan Comprehension (ganjil) Lebih singkat tanpa variabel baru:')
books_list = ['1. rich dad poor dad', '2. How to influence people', '3. The Warren Buffet Way', '4. The Intelligent Investor']
print(books_list[0::2]) #Start:End:Step
