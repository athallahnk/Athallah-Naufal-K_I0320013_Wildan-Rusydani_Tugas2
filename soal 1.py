#Menampilkan informasi
def Persegi_Panjang():
    print("menghitung luas persegi panjang")

#Input panjang dan lebar
    panjang = int(input("masukkan nilai panjang: "))
    lebar = int(input("masukkan nilai lebar: "))
    luas = (panjang * lebar)
    print("luas persegi panjang: ",luas)

#Menampilkan hasil luas persegi panjang
Persegi_Panjang()

#Menampilkan informasi
print("Menghitung luas lingkaran")

#input jari-jari
r=float(input("masukkan jari-jari: "))

#variabel
phi = 3.14

#menghitung luas lingkaran
luas = phi * r * r

#menampilkan hasil luas lingkaran
print("luas lingkaran: ", luas)

#menampilkan informasi
print("menghitung luas permukaan kubus")

#input nilai sisi
s=float(input("masukkan nilai sisi: "))

#menghitung luas permukaan kubus
luas_kubus = 6 * s * s

#menampilkan hasil luas permukaan kubus
print("luas kubus: ", luas_kubus)

#menampilkan informasi
print("konversi celcius ke fahrenheit")

#input nilai celcius
C = int(input("masukkan suhu dalam celcius: "))

#menghitung dalam fahrenheit
fah = (C * 9/5)+32

#menampilkan hasil dalam fahrenheit
print("suhu dalam fahrenheit: ", fah)

#menampilkan informasi
print("konversi reamur ke kelvin")

#input nilai reamur
R= int(input("masukkan suhu dalam reamur: "))

#menghitung dalam kelvin
kel = (R * 5/4)+273

#menampilkan hasil dalam kelvin
print("suhu dalam kelvin: ", kel)



