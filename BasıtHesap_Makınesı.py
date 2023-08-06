sayı1=input("1.sayı")
sayı2=input("2.sayı")
sayı1=float(sayı1)
sayı2=float(sayı2)
 
sonuç="0" ;

ıslemTuru=input("(+,-,*,/):")
if (ıslemTuru=="+"):
   sonuç=sayı1+sayı2;
elif(ıslemTuru=="-"):
   sonuç==sayı1-sayı2;
elif(ıslemTuru=="*"):
   sonuç==sayı1*sayı2;
elif(ıslemTuru=="/"):
   sonuç==sayı1/sayı2;
   print(sonuç)