"""Girilen sayının tek veya çift olduğunu belirlemek için mod ifadesi kullanılır MOD alma Python dilinde % ifadei ile sağlanır   """
sayı=input("sayı gir")
sayı=int(sayı)
sonuc="";

if(sayı % 2 ==0): #mod 2 demek girilen sayıyı 2 ye böl kalan 0 ise sayı çift tir
   sonuc="çift";
else:  
   sonuc="tek";
print(sonuc)