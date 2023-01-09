# Veri tipleri
# string (metinsel)veri tipi
# tek tırnak yada çift tırnak içerisne yazılan karakter dizeeridir.
# Bu karakterler (a-z) rakam (0-9)
# yada özel semboller olabilir(%/&)
#print("merhaba dünya")

# type:bilinmeyen veri tipini gösterir.
# Numbers(sayısal)veri tipleri.Sayısal veri tiplerine verilen isimdir. #
# sayısal veri tipleri genel olarak,int,floatve complex veri tipleri. int(integer)tam sayı
# not1=64
# not2=25
# not3=65
# ort=(not1+not2+not3)/3
# print(ort)

# boolean veri tipi kod yazarken bazı ifadelerin doğru yada yanlış olduğu değerlendirlmek istenebilir.
# print(1>2)
# print(2==2)

# kullanıcıdan veri alma
# yas=int (input("yaşınızı giriniz.."))
# yas=yas+1
# print(yas)
# print("3 aralıktaki yaşınız")
#sayi1=int(input("1. sayıyı giriniz:"))
#sayi2=int(input("2.sayıyı giriniz:"))
#sayi3=int(input("3.sayıyı gi20riniz:"))
# ort=(sayi1+sayi2+sayi3)/3
# print(ort)
# -----------------------------------
# kullanıcını girdiği kısa ve uzun kendardan dikdörtgenin alanını ve çevresini hesaplayan
#kenar1=int(input("kısa kenarı giriniz:"))
#kenar2=int(input("uzun kenarı giriniz:"))
# alan=kenar1*kenar2
# çevre=(kenar1+kenar2)*2
#print("alanı:",alan,"\n" "çevresi:",çevre)

# ----------------örnek1-------------------
# yas=int(input("Yaşınızı giriniz : "))
# yas=yas+1
# if yas >= 18 :
#     print("tebrikler 2023'de oy kullanabileceksiniz...")
# if yas < 18 :
#     print("Maalesef 2023'de oy kullanma yetkiniz yoktur...")
# --------------------örnek2----------------
# sayi=int(input("bir sayi giriniz : "))
# ort=sayi**2
# print(ort)


# **Numbers veri tipi**
# sayi1=int(input("birinci sayi:"))
# sayi2=int(input("ikinci sayi:"))
# toplam=sayi1+sayi2
# print(toplam)


# **Listeler**
# aynı türden farklı verilerin bir dizi halinde içinde toplanması.
# [] bu şekilde parantezin içine listeleme yapılır.

# ilk_liste=[88118646,"aslı","bilgisayar",3.14]
# print(ilk_liste)
# type(ilk_liste)

# sırasıyla pi sayısı ,inç biriminin cm karşılığı,mikroişlemci kısaltması,kullandığınız işletim sistemini adı ve 48 bitin byte karşılığını liste halinde hazırlayıp yazdırınız.

# list_1=[3.14,2.54,"Cpu","win10",6]
# print=(list_1)

# İNDEKS YADA İNDİS
# Listedeki elemanlara ulaşmak için elmaını indeksi kullanılır.

# sehirler=["burdur","ısparta","antalya","denizli","izmir"]
# print(sehirler[0]) #*indeks almak için kullanılan yöntem*
# print(sehirler[-1]) #*indeks - de olabilir - 1 ise bize sondan birinci olanı yazdırıcaktır.*

# asal_sayilar=[2,3,5,7,13,17,19,23]
# print(asal_sayilar[1:4]) #* 1 den 4e kadar yazdır ama 4 dahil değil
# # ***********
# print(asal_sayilar[::2]) #2 şer 2şer atlayarak yazdır.

# ornek=['Y','A','N','I','T']
# print(ornek)
# ornek[0] ='K'
# print(ornek)


# def encrypt(text, value, output=""):
#     for char in text:
#         output = "{}{}".format(output, chr(ord(char) + value))
#     return output

# def decrypt(text, value, output=""):
#     for char in text:
#         output = "{}{}".format(output, chr(ord(char) - value))
#     return output

# i = int(input("Increment value: "))

# text = input("Type your text: ")
# print("Encrypted text: {}".format(encrypt(text, i)))

# text = input("\nType for decrypt: ")
# print("Decrypted text: {}".format(decrypt(text, i)))

# sayi = float(input('sayi giriniz:  '))

# result = (sayi > 0) and (sayi<=100)
# print(f'sayi 0-100 arasındamı: {result}')

# --------------------------------------------------------------------------------------
# **************************************************************************************

# girilen sayının faktöriyelini hesaplayan program while döngüsü ile yapınız
# num = int(input("Lütfen faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
# factorial = 1
# i = 1
# while i <= num:
#   factorial = factorial * i
#   i += 1
# print("Girilen sayının faktöriyeli:", factorial)
# **************************************************************************************
# Girilen sayı sıfır(0) olana kadar girilen tüm sayıları toplayan ve ekrana gösteren programı yazınız.
# total = 0

# while True:   (sayi!=0) şeklindede yapılabilir
#   num = int(input("Lütfen bir sayı girin (0 girildiğinde toplamı gösterilecektir): "))
#   if num == 0:
#     break
#   total += num
# print("Girilen sayıların toplamı:", total)
# **************************************************************************************
# girilen şifre "python" olana kadar tekrar deneyiniz uyarısı veren , "python" girildiğinde giriş başarılı uyarısı veren programı yapınız
# while True:
#    password = input("Lütfen bir şifre girin: ")
#    if password == "python":
#        print("Giriş başarılı!")
#        break
#    else:
#        print("Girdiğiniz şifre hatalı, lütfen tekrar deneyin.")
# **************************************************************************************
# İÇ İÇE FOR DÖNGÜSÜNÜN KULLANIMI

# for i in range(0, 3):
#     for a in range(0, 3):
#         print(i, a)

# çarpım tablosunu yazdıran programı yapınız
# for i in range(0, 11):
#     print("-----------------------------------")
#     for j in range(0, 11):
#         print(f"{i} x {j} = {i * j}")
# **************************************************************************************

# ***Break ve Continue Deyimi***
# Break komutu döngüleri kırmak için kullanılır. algoritmada öngörülmeyen bir durumla ile karşılaşıldığında break komutu döngüden çıkmamızı sağlar
# döngüden sonra ki satırdan kod çalışmaya devam eder.
# **************************************************************************************

# i=1
# while True:
#     if (i==4):
#         print("Döngü Kırıldı")
#         break
#     print(i)
#     i=i+1
# **************************************************************************************

# Kullanıcıdan 1 ile 5 arasında bir sayı girmesini isteyiniz. Kullanıcı 3 sayısını girdiğinde break komutu ile döngüden çıkılarak "3 sayısı girildi ve döngü sona erdi" çıktısı veren programı yapınız
# while True:
#     sayi = int(input("Lütfen 1 ile 5 arasında bir sayı girin: "))
#     if sayi == 3:
#         print("3 sayısı girildi ve döngü sona erdi")
#         break
#     elif sayi < 1 or sayi > 5:
#         print("Lütfen 1-5 arasında sayı giriniz.")

# **************************************************************************************
# Kullanıcıdan 8 karakterlik bir şifre girmesini isteyiniz, kullanıcı 8 den az ya da daha fazla karakter içeren bir şifre girdiğinde şifrenin 8 karakterli olmalıdır uyarısı versin, 12345678 şifresi girdiğinde şifreniz başarılı kaydedildi uyarısı veren programı yazınız
# while True:
#     sifre = input("Lütfen 8 karakterlik bir şifre girin: ")

#     if sifre == "12345678":
#         print("Şifreniz Kaydedildi")
#         break
#     elif len(sifre) == 8:
#         print("Yanlış şifre girdiniz.")
#     else:
#         print("Şİfreniz 8 karakterli olmalıdır.")
# **************************************************************************************
# sayi = int(input("Bir sayı giriniz...:"))
# for i in range(1, 10):
#     if i == sayi:
#         break
# print(i)
# **************************************************************************************

metin="Ankara"
for osman in metin:
    if osman=='a':
        break
    print(osman)
# **************************************************************************************

# sayilar = [10, 11, 12, 13, 14, 15, 16]
# for aranan in sayilar:
#     print(aranan)
#     if aranan == 14:
#         break
# **************************************************************************************
# RANDOM KULLANIMI
# import random
# while True:
#     sayi=random.randint(1,20)
#     print("Rasgele seçilen sayı",sayi)
#     if(sayi%2==0):
#         print("sayı çift olduğu için döngü kırıldı",sayi)
#         break
# **************************************************************************************

# import random

# randomSayi = random.randint(1, 100)

# while True:
#     giris = int(input("Bir sayı tahmin edin (1 ile 100 arasında): "))

#     if giris == randomSayi:
#         print("Tebrikler, doğru tahmin ettiniz!")
#         break
#     elif giris < randomSayi:
#         print("Tahmin ettiğiniz değer daha büyük")
#     elif giris > randomSayi:
#         print("Tahmin Ettiğiniz değer daha Küçük")
#     else:
#         print("Yanlış tahmin, lütfen tekrar deneyin")
# **************************************************************************************

# CONTİNUE

while True:
    sifre=input("LÜtfen şifrenizi giriniz....:")

    if len (sifre)==4:
        print("Tebrikler 4 karakterli şifre girdiniz....:",sifre)
        break
    else:
        print("LÜtfen 4 karakterli şifre giriniz...:")

# **************************************************************************************

#  **Fonskiyonlar**
#  Programlama yaparken bazı işlemlerin programın farklı yerlerinde tekrarlanması gerekebilir. İhtiyaç duyuduğunda çağrılıp çalıştırılabilen kod paketine fonksiyon denir.
#  Bazı dillerde prosödür ya da yordam denilebilir.
#  Gömülü fonksiyonların ve modüllerin kullanuımı
#  Orneğin matematiksel işlemlerde ihtiyaç duyacağımız "MATH" isimli kütüphane vardır.İstendiğinde programa eklenip kullanılabilir. Nunlara modül denir.
#  Modüller istenildiği zaman çağrılabilir.

#  kULLANIMI
# from ModulAdı import fonksiyon adı
# fonksiyonlara erişim sağlanır
# from math import sin,sqrt,pow,cos
# **************************************************************************************
# # Karekök
# print(sqrt(4))
# **************************************************************************************
# # Sinüs hesaplatma
# print(sin(30))
# **************************************************************************************

# # Cosinus hesaplatma
# print(cos(45))
# **************************************************************************************

# # 5 sayısının 2. kuvveti
# print(pow(5,2))
# **************************************************************************************

# import math
# print(math.sqrt(16))
# print(math.pow(2,5))
# **************************************************************************************
# Fonksiyonlar "def"komutu kullanarak tanımlanabilir.
# 1 def komukullanarak fonksiyon tanımlanacağı programlana diline bildirir.
# 2 Anahtar sözcükten sonra fonksiyon çağrılırken kullanılacak ism python isimlendirme kurallarına göre belirlenir.
# 3 Parantezler arasına fonksiyona parametre gönderilecek parametreler yazılır, eğer parametre yoksa içi boş bırakılır.
# 4 tanım ve isim altında bir sekme bırakılarak fonksiyon çağrıldığında çalışacak kodlar yazılır.
# **************************************************************************************
# def selamla():
#     print("Herkese merhabalar")

#     for a in range(4):

#         selamla()
# **************************************************************************************

# def selamlar():
#     ad=input("Adınızı YAZINIZ.....:")
#     if ad:
#         print("merhaba",ad)
#     else:
#         print("mERHABA LANNN")
# selamlar()
# **************************************************************************************

# def say():
#     i=0
#     while i<=9:
#         i+=1
#         print(i)
# say()
# **************************************************************************************

# Yıldız programı

# def yildiz_ucgeni(n):
#   for i in range(n):
#     for j in range(i+1):
#       print("*", end=" ")
#     print("")

# yildiz_ucgeni(10)
# **************************************************************************************
# def ulke_yaz (ulke="TÜRKİYE"):
#     print(ulke +" benim memleketim")
# ulke_yaz("Türkiye")
# ulke_yaz("Azerbaycan")
# ulke_yaz("Rusya")
# ulke_yaz("Ukrayna")

# def en_kucuk_cocuk(cocuk3,cocuk2,cocuk1):
#     print("En küçük çocuk artık "+cocuk3)
# en_kucuk_cocuk(cocuk1="Aslı",cocuk2="Ali",cocuk3="Mehmet")
# **************************************************************************************
# Fonksiyonla üçgenin alanını bulma

# def dikdortgen_alan(kenar1,kenar2):
#     alan=kenar1*kenar2
#     print("Verilen dikdörtgenin alanı...: "+str(alan)+" metre karedir...: ")
# dikdortgen_alan(5,4)
# dikdortgen_alan(10,10)
# **************************************************************************************
# Fonksiyonla tek mi çift mi

# def tekcift(sayi):
#     if (sayi % 2 == 0):
#         print("sayı Çİfttir")
#     else:
#         print("sayı tektir.")


# tekcift(31)
# **************************************************************************************
# Fonksiyonla sınav ortalamsı buldurma
# def ortalama(not1,not2,sozlu):
#     ort=(not1+not2+sozlu)/3
#     return ort
# if(ortalama(35,85,45)>=45):
#     print("Dersi geçti")
# else:
#     print("Derste kaldı...")
# **************************************************************************************

# yanlış bir seçim girilene kadar hesap makinesi programınıfonksiyon ile yapınız
# def topla(sayi1, sayi2):
#   return sayi1 + sayi2

# def cikar(sayi1, sayi2):
#   return sayi1 - sayi2

# def carp(sayi1, sayi2):
#   return sayi1 * sayi2

# def bol(sayi1, sayi2):
#   if sayi2 == 0:
#     return "Sıfıra bölme hatası"
#   return sayi1 / sayi2

# def kare(sayi):
#   return sayi ** 2

# while True:
#   print("Hesap makinesi programına hoşgeldiniz. Lütfen bir işlem seçin:")
#   print("1. Toplama")
#   print("2. Çıkarma")
#   print("3. Çarpma")
#   print("4. Bölme")
#   print("5. Kare alma")
#   islem = input("Seçiminiz: ")

#   if islem == "1":
#     sayi1 = float(input("Birinci sayıyı girin: "))
#     sayi2 = float(input("İkinci sayıyı girin: "))
#     sonuc = topla(sayi1, sayi2)
#     print(f"{sayi1} + {sayi2} = {sonuc}")
#   elif islem == "2":
#     sayi1 = float(input("Birinci sayıyı girin: "))
#     sayi2 = float(input("İkinci sayıyı girin: "))
#     sonuc = cikar(sayi1, sayi2)
#     print(f"{sayi1} - {sayi2} = {sonuc}")
#   elif islem == "3":
#     sayi1 =float(input("Birinci Sayıyı Giriniz...:"))
#     sayi2=float(input("İkinci Sayıyı Giriniz....:"))
#     sonuc=bol(sayi1,sayi2)
#     print(f"{sayi1}/{sayi2}={sonuc}")
# **************************************************************************************
# lambda Fonksiyonlar
# Anonim fonksiyonlar isimsiz tek satırlık. lambda fonksiyonlar birden fazla argüman alabilir ancak geriye tek bir değer döndürür
# anonim oldukları için direkt çağrılmazlar değişkene atanırlar
# **************************************************************************************

# ÖRENK
# kdvliFiyat=lambda fiyat: fiyat *1.18
# print (kdvliFiyat(100))
# **************************************************************************************
# toplam = lambda a,b,c: a+b+c
# print(toplam(4,8,12))
# **************************************************************************************
# def carpan(n):
#     return lambda a: a*n
# carpilan= carpan(5)
# carpilan(10)
# **************************************************************************************
# def carpan(n):
#     return lambda a: a*n
# ikikat=carpan(2)
# uckat=carpan(3)
# beskat=carpan(5)
# onkat=carpan(10)

# print(ikikat(78))
# print(ikikat(30))
# print(ikikat(9))
# print(ikikat(10))
# **************************************************************************************

# sonuc=0
# def toplama(sayi1,sayi2):
#     sonuc=sayi1+sayi2
#     print("Fonksiyon içinde toplam.....:",sonuc)
#     return sonuc
# toplama(17,80)
# print("Fonksiyon dışı toplama......:",sonuc)
# **************************************************************************************
#  Tarih nesnesi
# python dilinde zaman bilgisi tutmak için eklendiğinde ait bir veri tipi bulunmaz. Bunun için yin "datetime"modülü kullanılır.
# Date time kullanılan sınıflar:

# "datetime" : tarihle ilgili nitelikleri ve fonksiyonları barındıran sınıftır.
# "datetime.time": zamanla ilgili nitelikleri ve fonksiyonları barındıran sınıftır.

# datetime.datetime : date ve time sınıflarının birleşiminden ve ilave birkaç fonksiyondan oluşur.

# datetime.timedelta: iki date, time veya datetimenesnesi arasında ki zaman farkını mikrosaniye cinsinden veren sınıftır.

# datetime.tzinfo: date ve time sınıfının saat dilimi ve özelliklerini tutmakö için oluşturulmuş temel sınıftır.
# **************************************************************************************
# TARİH VE SAAT

# from datetime import datetime
# an=datetime.now()
# print("Tarih ve saat...:",an)
# **************************************************************************************
# GÜN
# from datetime import datetime
# gun=datetime.today()
# print("Gün........:",gun)
# **************************************************************************************
# from datetime import datetime
# bugun= datetime.today()
# print(bugun.weekday)
# print(bugun.year)
# print(bugun.month)
# print(bugun.day)
# print(bugun.hour)
# print(bugun.minute)
# print(bugun.second)
# **************************************************************************************
# DOĞUM TARİHİ
# from datetime import datetime
# dogumTarihi=datetime(year=2002,month=7,day=3)
# print(dogumTarihi)
# **************************************************************************************
# DOĞUM TARİHİ 2
# from datetime import datetime
# dogumTarihi=datetime(year=2002,month=7,day=3,hour=10,minute=30,second=10)
# print(dogumTarihi)
# **************************************************************************************
# from datetime import datetime
# bugun = datetime.today()
# print("Bugünün tarihi.....:", bugun)
# yil = int (input("Doğum yılınızı giriniz...:"))
# ay = int (input("Doğum ayınızı giriniz...:"))
# gun = int (input("Doğum gününüzü giriniz...:"))
# dogum = datetime(year=yil, month=ay, day=gun)
# print("siz", dogum, " Tarihinde doğdunuz")

# yas = bugun-dogum
# print("siz", yas, "Gündür yaşıyorsunuz")
# **************************************************************************************
# import datetime
# bugun=datetime.date.today()
# gelecek=bugun+datetime.timedelta(days=150)
# print(gelecek)
# **************************************************************************************
# TURKÇE
# import datetime
# import locale
# locale.setlocale(locale.LC_ALL,'Turkish_Turkey.1254')
# an=datetime.datetime.now()
# print(an.strftime('%y')) #yıl
# print(an.strftime('%x')) #saat
# print(an.strftime('%d')) #ayın kaçıncı günü
# print(an.strftime('%A')) #gün ismi olarak
# print(an.strftime('%B')) #ay ismi olacak




