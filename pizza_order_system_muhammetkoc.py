# -*- coding: utf-8 -*-
"""pizza_order_system_muhammetkoc.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x67_T9XM0l70nwnNIT7xQx8iUXnYX2ex
"""

#gerekli kütüphaneler eklendi
import csv
import datetime
import time

#menü dosyası okunur
menu = open("menu.txt","r")
print(menu.read())

# Pizza sınıfı oluşturuldu
class Pizza():
  def __init__(self, description,cost):
    self.description = description
    self.cost = cost
    print("Sipariş Oluşturuldu...")
  def get_description(self):
    return self.description
  def get_cost(self):
    return self.cost

#classic pizza alt sınıfı oluşturuldu
class Classic_pizza(Pizza):
  def __init__(self):
    self.description= "Klasik pizza"
    self.cost=30
#Margarita pizza alt sınıfı oluşturuldu
class Margarita_pizza(Pizza):
  def __init__(self):
    self.description= "Margarita pizza"
    self.cost=40
#TürkPizza pizza alt sınıfı oluşturuldu
class TurkPizza_pizza(Pizza):
  def __init__(self):
    self.description= "TurkPizza"
    self.cost=50
#plain pizza alt sınıfı oluşturuldu
class Plain_pizza(Pizza):
  def __init__(self):
    self.description= "Sade pizza"
    self.cost=20

#decorator sınıfı oluşturuldu
class Decorator():
    def __init__(self,description,cost):
      self.description=description
      self.cost=cost
    def get_cost(self,base_cost):
        return self.cost + base_cost
    def get_description(self,base_description):
        return self.description +' '+ base_description

#decorator sınıfı kullanılarak sos alt sınıfları oluşturuldu
class Zeytin(Decorator):
  def __init__(self):
      self.description="Zeytinli"
      self.cost=10
class Mantar(Decorator):
  def __init__(self):
      self.description="Mantarli"
      self.cost=12
class Peynir(Decorator):
  def __init__(self):
      self.description="Peynirli"
      self.cost=14
class Et(Decorator):
  def __init__(self):
      self.description="Etli"
      self.cost=15
class Sogan(Decorator):
  def __init__(self):
      self.description="Soganli"
      self.cost=8
class Misir(Decorator):
  def __init__(self):
      self.description="Misirli"
      self.cost=11

#Menü seçimleri bir fonksiyon yardımıyla siparişi oluşturur
#Switch-case yapısına python sürümü(colab.google python =v3.9) uygun olmadığı için if-else kullanıldı
def total(pizza_base,sauce):
  if pizza_base== 1:
        pizza_base = Classic_pizza()
  elif pizza_base== 2:
        pizza_base = Margarita_pizza()
  elif pizza_base== 3:
        pizza_base = TurkPizza_pizza()
  else:
        pizza_base = Plain_pizza()
  if sauce== 11:
        sauce=Zeytin()
  elif sauce== 12:
        sauce=Mantar()
  elif sauce==  13:
        sauce=Peynir()
  elif sauce==  14:
        sauce=Et()
  elif sauce==  15:
        sauce=Sogan()
  else:
       sauce=Misir()
  total= Pizza(sauce.get_description(pizza_base.get_description()),sauce.get_cost(pizza_base.get_cost()))
  return total

#Müşterilerin tüm bigilerini içeren Customer sınıfı oluşturuldu
class Customer():
  def __init__(self,username,passport_number,card_number,card_date,card_cvv,order_description,order_cost,order_time):
    self.username=username
    self.passport_number=passport_number
    self.card_number= card_number
    self.card_date=card_date
    self.card_cvv= card_cvv
    self.order_description=order_description
    self.order_cost=order_cost
    self.order_time= order_time
  def get_username(self):
    return self.username
  def get_passport_number(self):
    return self.passport_number
  def get_card_number(self):
    return self.card_number
  def get_card_date(self):
    return self.card_date
  def get_card_cvv(self):
    return self.card_cvv
  def get_order_description(self):
    return self.order_description
  def get_order_cost(self):
    return self.order_cost
  def get_order_time(self):
    return self.order_time

#Müsterinin tüm bilgilerinin Customer sınıfına yazılmasını sağlar
def info(order):
  while(True):
    username= input("Kullanıcı adınızı giriniz: ")
    passport_number=input("Tc kimlik numaranızı giriniz: ")
    print("Şimdi ödeme için Banka kartı bilgilerinizi girmenizi isteyeceğiz.\n")
    card_number= input("Kart numarası: ")
    card_date= input("Kartınızın son kullanma tarihi(AA/YY): ")
    card_cvv=input("Kartınızın arkasında bulunan üç haneli güvenlik kodunu giriniz:")
    order_time=str(datetime.datetime.now())
    customer=Customer(username,passport_number,card_number,card_date,card_cvv,order.get_description(),order.get_cost(),order_time)
    print("\n\nÖnemli Not!!!\nBilgilerinizin doğruluğunu kontrol ediniz.Yanlışlık olduğunu düşünüyorsanız tekrar giriniz. Sorumluluk size aittir.\n")
    print(f"kullanıcı adı:{username}, Tc kimlik:{passport_number}, kart numamrası:{card_number}, kart s.k.t:{card_date}, \ncard cvv:{card_cvv}, sipariş:{order.get_description()}, tutar:{order.get_cost()}, sipariş zamanı:{order_time}")
    check=input("\n Devam edilsin mi?(e/h)")
    if check=='e' or check=='evet':
      return customer
      break
    else:
      print("Bilgilerinizi tekrar giriniz...\n\n")

#Müşteri bilgilerinin database dosyasına yazılmasını sağlar
def write_database(customer):
  with open('Orders_Database.csv', 'a', newline='') as file:
       writer = csv.writer(file,delimiter=';')
     
       writer.writerow(["Kullanici adi", "Tc Kimlik No", "Kart Numarasi","Kart SKT","Kart CVV","Siparis","Tutar","Tarih"])
       writer.writerow(list((customer.get_username(),customer.get_passport_number(),customer.get_card_number(),customer.get_card_date(),customer.get_card_cvv(),customer.get_order_description(),customer.get_order_cost(),customer.get_order_time())))
       writer.writerow([])

# kullanılmıyor -Customer sınıfından liste oluşturan fonksiyon
def create_list(customer):
  info_list=list((customer.get_username(),customer.get_passport_number(),customer.get_card_number(),customer.get_card_date(),customer.get_card_cvv(),customer.get_order_description(),customer.get_order_cost(),customer.get_order_time()))
  return info_list

def main():
  with open('menu.txt', 'r') as f:
    print("Müthiş pizzaya hoşgeldiniz! MüthişPizza  müthiş müşteri memmnuniyeti sunar!")
    while(True):
      while(True):
        for i in range(5):
          print(f.readline())
        while(True):
          pizza_base= int(input("(1,2,3,4):"))
          if pizza_base == 1 or pizza_base == 2 or pizza_base == 3 or pizza_base == 4:
            break
          print("Doğru bir giriş yapmadınız lütfen sadece 1,2,3,4 rakamlarını kullanın.")
          time.sleep(2)
        print("\n\n")
        for i in range(8):
          print(f.readline())
        f.seek(0)
        while(True):
          sauce= int(input("(11,12,13,14,15,16):"))
          if sauce == 11 or sauce == 12 or sauce == 13 or sauce == 14 or sauce==15 or sauce==16:
            break
          print("Doğru bir giriş yapmadınız lütfen sadece 11,12,13,14,15,16 rakamlarını kullanın.")
          time.sleep(2)
        order= total(pizza_base,sauce)
        print(f"\n\nSiparişiniz:{order.get_description()},sipariş tutarı:{order.get_cost()}")
        check=input("\n Seçimi onaylıyor musunuz?(e/h)")
        if check=='e' or check=='evet':
          customer=info(order)
          write_database(customer)
          break
        else:
          print("Tekrar seçim yapınız...\n\n")
      check=input("\n Başka bir sipariş oluşturmak istiyor musunuz?(e/h)")
      if check=='h' or check=='hayır':
        break
      else:
        print("Tekrar seçim yapınız...\n\n")

if __name__=="__main__":
  main()