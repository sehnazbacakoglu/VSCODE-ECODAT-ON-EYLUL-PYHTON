"""
Lütfen Kullanıcı Adınızı Giriniz : user
user yetkis ile admin paneline giriş yapamazsınız
"""
kullaniciAdi = input("lütfen kullanıcı adınızı giriniz: ")
if kullaniciAdi != "admin" :
    print(f"{kullaniciAdi} yetkisi  ile admin paneline giriş yapamazsınız ")
