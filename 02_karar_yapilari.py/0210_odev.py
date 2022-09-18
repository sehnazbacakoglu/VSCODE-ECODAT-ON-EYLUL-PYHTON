""" 
Kargo Bedeli 7.5 TL.’dir 
Satın Alınan Ürünlerin Toplam Fiyatı 250 TL üzeri olduğunda kargo bedavadır. 
Kullanıcıdan fiyat bilgisi alıp ekrana ödenecek tutarı yazan prog.? 
"""
fiyatBilgisi = int(input("Lütfen satın aldığınız ürünlerin toplam ücretini giriniz: "))
kargoBedeli=7.5 
if fiyatBilgisi <=250 :
    fiyatBilgisi+=kargoBedeli
print(f"Ödeceğiniz tutar {fiyatBilgisi} TL dir")



