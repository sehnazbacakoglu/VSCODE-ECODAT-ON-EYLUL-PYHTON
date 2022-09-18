"""
Lütfen 1. Snv Notunu Giriniz: ...
Lütfen 2. Snv Notunu Giriniz: ...
Lütfen 3. Snv Notunu Giriniz: ...
GEÇTİNİZ, Ortalama Notunuz ...
"""
# " " "
# sinav1 = int(input("lütfen 1. sınav notunuzu giriniz: "))
# sinav2 = int(input("lütfen 2. sınav notunuzu giriniz: "))
# sinav3 = int(input("lütfen 3. sınav notunuzu giriniz: "))
# ortalama = (sinav1+sinav2+sinav3)/3
# if ortalama >= 50:
#  print(f"Geçtiniz , {ortalama} notunuzdur.")
#  " " "

"""
Klavyeden 3 Sayı Girilecek Büyük Olanı Ekrana Yazacağız
1. Sayı : 52
2. Sayı : 60
3. Sayı : 12
En Büyük Sayı 60
"""
sayi1 = int(input("Lütfen birinci sayıyı giriniz : "))
sayi2 = int(input("Lütfen ikinci sayıyı giriniz : "))
sayi3 = int(input("Lütfen üçüncü sayıyı giriniz : "))
eb = 0
if sayi1 > eb:
    eb = sayi1
if sayi2 > eb:
    eb = sayi2
if sayi3 > eb:
    eb = sayi3

# print(f"en büyük sayı {eb} dir")
# s1 = int(input("ilk sayı:"))
# s2 = int(input("ikinci sayı:"))
# s3 = int(input("üçüncü sayı:"))

# if s1 > s2 & s3:
#     print(f"en büyük {s1}")
# if s2 > s3 & s1:
#     print(f"en büyük {s2}")
# if  s3 > s2 & s1:
#     print(f"en büyük {s3}")
"""
Klavyeden Sayı Değeri Girilecek
Program Mutlak Değer Hesaplayıp Ekrana Yazacak

L. Sayı Giriniz: 10
10 sayısının mutlak değeri 10

L. Sayı Giriniz: -5
-5 sayısının mutlak değeri 5
"""
sayi= int(input("Bir sayi giriniz"))
if sayi>0 :
    print(f"Girdiğiniz sayının mutlak değeri {sayi} dır")
else sayi<0 :
print(f"girdiğiniz sayının mutlak değeri {sayi* -1}")
