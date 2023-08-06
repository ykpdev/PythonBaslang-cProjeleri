"""-10 ile +10 arasındaki sayılları ekrana yazmak için range denilen özel bir fonksiyon kullanılır
range= Belirtilen başlangıç değerinden başlayıp, her seferinde adım sayısı kadar arttırarak, 
bitiş değerine kadar olan sayıları bulunduran bir numpy dizisi döndürür
"""
for i in range(10,-11,-1): # Döngü 10 dan başlar 1 er azalır ve -10 da sonlanır -11 yazılmaz kuralldır.
    metin =str(i)+".sayı"
    print(metin)