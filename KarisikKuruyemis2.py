for i in range(1,11):
  for s in range(1,11):
    print( i,"x",s,"=",i*s,)
  print("- - - - - - - - - - -")
  

while True:
  print("Harf Notu Hesaplama Uygulamasına Hoş Geldiniz")  
  print("Lütfen Sınav Sonuçlarınızı 100'lük sisteme göre yazınız")
  vize = input("Vize Notunuz => ")
  final = input("Final Notunuz => ")

  ortalama = (0.6*float(final))+(0.4*float(vize))
  print(f"Ortalamanız {ortalama:.2f} Geldi.")
 

  if(ortalama > 100):
    print("Notunuzu Yanlış girdiniz. Tekrar Deneyiniz.\n")
    continue
  elif(ortalama >= 90):
      print("Harf Notunuz: AA")
      break
  elif(ortalama >=85):
      print("Harf Notunuz: BA")
      break
  elif(ortalama >=80):
      print("Harf Notunuz: BB")
      break
  elif(ortalama >=75):
      print("Harf Notunuz: CB")
      break
  elif(ortalama >=70):
      print("Harf Notunuz: CC")
      break
  elif(ortalama >=65):
      print("Harf Notunuz: DC")
      break
  elif(ortalama >=60):
      print("Harf Notunuz: DD")
      break
  elif(ortalama >=55):
      print("Harf Notunuz: FD")
      break
  elif(ortalama < 55) and (ortalama >=0):
      print("Harf Notunuz: FF")
      break
  else:
      print("Notunuzu Yanlış girdiniz. Tekrar Deneyiniz.\n")
      continue
      






def toplama(x, y):
    return x + y
def cikarma(x, y):
    return x - y
def carpma(x, y):
    return (x) * (y)
def bölme(x, y):
    return (x) / (y)
print("- - - - - - - - - - - - - - - - - -")
print("Hesap Makinesine Hoş Geldiniz.")

while True:
  print("""Lütfen Yapmak İstediğiniz İşlemi Seçiniz
           1- Toplama
           2- Çıkarma
           3- Çarpma
           4- Bölme
           9- Çıkış""")
  secim = input("=> ")
  if secim == "1" or secim == "2" or secim== "3" or secim=="4":
    while True:
      try:
          print("\nKüsüratlı Sayıları Nokta (.) İle Belirtiniz Örn: 1.2")
          sayi1=float(input("İlk Sayıyı Giriniz => "))
          sayi2=float(input("İkinci Sayıyı Giriniz => "))
          break
      except  ValueError:
          print("Hatalı Sayı Girişi. Lütfen Tekrar Sayı Girişi Yapınız.")
          continue
    if secim == "1":
      print(sayi1,"+",sayi2,"=",toplama(sayi1,sayi2)) 
    elif secim == "2":
      print(sayi1,"-",sayi2,"=",cikarma(sayi1,sayi2))
    elif secim == "3":
      print(sayi1,"x",sayi2,"=",carpma(sayi1,sayi2))
    elif secim == "4":
      if sayi2 == 0:
        print("Bir Sayının 0 (Sıfır) İle Bölümü Tanımsızdır.")
        continue
      print(sayi1,"/",sayi2,"=",bölme(sayi1,sayi2))

  elif secim == "9":
    break   
  else:
    print("Yanlış Tuşlama Yaptınız. Tekrar Deneyiniz.")

koltuk_numaraları = """                                                             
                                                                       /\\
                                                                  /          \\
                                                               /                 \\
                                                            /                       \\
---------------------------------------------------------------------------------------------------------------------------------
||        | 10 |       | 9 |       | 8 |       | 7 |       | 6 |       | 5 |       | 4 |       | 3 |       | 2 |       | 1 |   |||  (KOKPİT)                                                                                                  
---------------------------------------------------------------------------------------------------------------------------------
                                                              \                   /             
                                                                 \             /
                                                                    \        /
                                                                        \/
""" 

koltuklar = [0,0,0,0,0,0,0,0,0,0]
dolu_koltuk_numaraları = []
boş_koltuk_numaraları = []

print("Uçak Bileti Alma Programına Hoş Geldiniz")

while True:
  print("""
         1- Bilet Al
         2- Hızlı Bilet Al
         3- Mevcut Koltuk Durumu Öğrenme
         4- Bilet İptali
         5- Çıkış""")
  tuslama = input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz => ")
  if tuslama == "1" or "2" or "3" or "4":
    if tuslama == "5":
      break
    while True:
     if  tuslama == "1":
      print(koltuk_numaraları)
      b = int(input("İstediğiniz Koltuğu Seçiniz => "))-1
      if b ==  0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        if koltuklar[b] == 0:
          dolu_koltuk_numaraları.append(b+1)
          koltuklar.insert(b,1)
          del koltuklar[b+1]
          print(b+1,". Koltuğu Başarılı Bir Şekilde Aldınız.")
          break
        elif koltuklar[b] == 1:
          print("Maalesef Seçtiğiniz Koltuk Dolu. Başka Bir Koltuk Deneyiniz.")
     elif tuslama == "2":
      print("Hızlı Bilet Al Seçildi. Boş Olan Herhangi Bir Koltuk Seçiliyor...")
      for i in range(10):
        if koltuklar[i] == 0:
          koltuklar.insert(i,1)
          dolu_koltuk_numaraları.append(i+1)
          del koltuklar[i+1]
          print(i+1,". Koltuğu Başarılı Bir Şekilde Aldınız.")
          break
      break
     
     elif tuslama == "3":
      boş_koltuk_numaraları=[]
      print(koltuk_numaraları)
      print("Koltuk Numarası Öğrenme Programına Hoş Geldiniz.")
      print("Dolu Koltuk Numaraları",dolu_koltuk_numaraları)
      print("Dolu Koltuk Sayısı",(koltuklar.count(1)))
      for i in range(10):
        if i+1 in dolu_koltuk_numaraları:
          continue
        else:
          boş_koltuk_numaraları.append(i+1)
          
      print("Boş Koltuk Sayısı:",(koltuklar.count(0)))
      print(boş_koltuk_numaraları)
      break
      
     elif tuslama == "4":
          print(koltuk_numaraları)
          try:
            ksil=int(input("İptal Etmek İstediğiniz Koltuk Numarası => "))
          except ValueError:
            print("Hatalı Giriş.")
          if koltuklar[ksil-1] == 0:
            print("İptal Etmek İstediğiniz Koltuk Zaten Boştur.")
            break
          
          koltuklar[ksil-1] = 0 
          dolu_koltuk_numaraları.remove(ksil)
          boş_koltuk_numaraları.append(ksil)
          print("{} Numaralı Koltuk Başarıyla İptal Edildi.".format(ksil))
          break
     else:
          print("Yanlış Tuşlama Yaptınız. Tekrar Deneyiniz.")  
              
     break
    
      
      
      

  
  else:
    print("Yanlış Tuşlama Yaptınız. Tekrar Deneyiniz.")




