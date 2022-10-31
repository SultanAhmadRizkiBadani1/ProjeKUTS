# Penggunaan IF
print("Penggunaan IF")
angka = 30
if angka > 0:
    print(angka, "angka adalah bilangan positif")

#Penggunaan IF dan ELSE
print("Penggunaan IF dan ELSE")
nama = input("masukan nama anda : ")
if nama =="sultan ahmad" : 
    print("hallo,selamat datang boss")
else :
    print(f"maaf {nama},kamu bukan boss saya")

#penggunaan IF, ELIF, dan ELSE
print("Penggunaan IF, ELIF, dan ELSE")
Harga = int(input("Masukan Harga: "))

if Harga >= 1000:
    print("Teh Eco")
elif Harga >= 2000:
    print("Granita")
elif Harga >= 3000:
    print("Aqua Botol")
elif Harga >= 4000:
    print("Teh Pucul Botol")
else :
    print("")