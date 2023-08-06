"""İnput metodu  ile elde edilen veriler string veri türüdür """


"""sayı1=input("sayı1 gir")
sayı2=input("sayı2 gir")
sonuc=sayı1+sayı2
print(sonuc)"""


"""Yukarı kod da sayıların veri türü belirtilmemiş bu nedenle input metodu girilen değeri string olduğunu bildiği için girilen değerleri yan yana yazar"""
"""int, double,float gibi veri türü kullanılırsa (+,-,*,/) gibi matematik işlemleri yapılabilir  """


s1=input("Sayı1")
s2=input("Sayı2")
s1=int(s1)     #girilen değerler int veri türündedir 
s2=int(s2)
sonuc=s1+s2
print(sonuc)