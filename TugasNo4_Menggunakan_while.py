#penggunaan while angka
p = int(input("Masukkan banyak pengulangan: "))
i = 1
while i <= p:
   print(i)
   i+=1

#penggunaan while karakter
print("lisUniversitas : ")
listUniversitas = [
  'UBHARA', 'UI', 'UNPAD', 'BINUS', 'UGM',
  'IPB', 'ITB', 'GUNDAR', 'UNJ', 'UIN'
]

i = 0
while i < len(listUniversitas):
  print(listUniversitas[i])
  i += 1