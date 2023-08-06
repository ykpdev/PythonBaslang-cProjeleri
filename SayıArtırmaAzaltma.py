"""Kullanıcı tarafınfan + girildiği zaman sayı arttırma - girildiği zaman sayı azaltma işlemi yapılmaktadır
Bunun için kullanıcıdan sürekli olarak + ve - basması beklenilmektedir 
Başka bir karaktere basıldığında program çıkış yapacaktır.
"""
# while döngüsü kullanmamız gerekir sonzuz bir döngü oluşturmak için
"""Bir sayı tanımlanması yapılır kullanıcıdan bu sayıyı arttırma ve azaltma işlemi yapılması istenmektedir
farklı bir karektere basılırsa çıkış işlemi yapılacaktır
"""

sayı=0



while True:
    durum=input()   
    if(durum=="+"):
        sayı=sayı+1;
    elif(durum=="-"):
        sayı=sayı-1;
    else:
        quit()

    print(sayı)
