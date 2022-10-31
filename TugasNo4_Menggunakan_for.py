#kode program pengulangan menggunakan for angka
for i in range(10):
    print("pengulangan ke - ", i)

print ("\n")

#kode program pengulangan menggunakan for karakter
print("listMotor : ")
listMotor = [
  'CBR250RR', 'ZX25R', 'R25', 'NINJA250RR', 'GSX250R'
]

for i, listMotor in enumerate(listMotor):
  print(i+1, listMotor)
