#Yusuf Akbaş 2212010033 MAT353-ÖDEV
# Newton raphson yöntemi ile kök bulma
print("")
import math as mt
import matplotlib.pyplot as plt
def f(x):
    return mt.cos(x)-x
def f_turev(x):
    return -mt.sin(x)-1
x=1 # başlangıç sayısını f(0).f(1)<0 olmasından dolayı ve kökün
     # 1 e daha yakın olmasından dolayı 1 olarak seçtim.( f(0)=1  f(1)=-0,01__ )
h=0  #hatanın her seferinde atanacağı değer
t=0  #her yeni gelen kökü bir arka sıraya kaydırmak için kullandım
x_kok=0  #her defasında bulunan yeni kokun atandığı değerleer
iterasyon=0  #iterasyon sayımızı belirten değer
d_iterasyon=[]  #iterasyon kok ve hatanın kaydedildiği listeler
r_kok=[] 
h_hata=[]       
while iterasyon<100 and h<10**(-15) :   # Newton Raphson yönteminin formülü ve
                                         # elde edilen değerlerin listelere kaydedilmesi
    x_kok=x-f(x)/f_turev(x)
    iterasyon+=1
    d_iterasyon.append(iterasyon)
    r_kok.append(x_kok)
    h=x_kok-x
    h_hata.append(h)
    t=x
    x=x_kok
    if abs(h)>10**(-15):                 #elde edilen verillerin yazdırılması
        print('iterasyon=',iterasyon)
        print('kok=',x_kok)
        print('hata=',h)

#regula falsi metodu ile yaklaşık kök bulma
print("\nREGULA FALSİ YÖNTEMİ\n")
def g(x):
    return mt.cos(x)-x
'f(0).f(1)<0 olduğu için başlangıç aralığı [0,1] olarak seçilir'
iterasyon=0
a=0                  #1. sınır
b=1                  #"2. sınır"
s=0                  #elde edeceğimiz yeni sınır değer"
h=0                  #"hata hesabının aktarılacağı değer"
itrsn=[]                
hata=[]                #"verileri kaydedeceğimiz listeler"
sinir_a=[]
sinir_b=[]
sira=[]              # 0 olmayan hataların kaçıncı iterasyonda bittiğini gösterir
                                    # grafik çizerken kulanılacak
while iterasyon<100 :                         
    s  =  (a*g(b)-b*g(a))  /  (g(b)-g(a))       #"regula falsi formülü"
    iterasyon+=1
    itrsn.append(iterasyon)
    
    if g(s) * g(a) < 0 :
  
        h=abs(b-s)                    
        hata.append(h)                  
        b=s 
        sinir_a.append(a)                
        sinir_b.append(b)
        sira.append(iterasyon)
        
        if  h> 10**(-15):
            print("hata=",h)
            print("kok=",s)
            print(" sinir_a=",a)                #55 ve 83. satırlar arasında yapılmak istenen işaret kontrolü ve "
            print("sinir_b=",b)
            print("iterasyon=",iterasyon)        #"yeni değerin hangi sinirin yerini alacağının belirlenmesi"
    elif g(s) * g(b) < 0 :                         #" ona göre, oluşan yeni değerlerin kaydedilmesidir"
        h=abs(a-s)                                
        hata.append(h)                                ### tolerans aralığına girdiği sıradaki hatayı listeleyemedim###
        a=s
        sinir_a.append(a)
        sinir_b.append(b)
        sira.append(iterasyon)
        
        if h> 10**(-15):
            print("iterasyon=",iterasyon)
            print("hata=",h)
            print("kok=",s)
            print("sinir_a=",a)
            print("sinir_b=",b)
#grafik                                #grafik çizebilmek için ,gereken toleransa kadar
plt.semilogx(sira,hata)                 #olan iterasyon numaralarını sıra listesinde yazdırıp
plt.semilogx(d_iterasyon,h_hata)                              #grafik çzildi
plt.show()

'''' 
SONUÇ
Newton Raphson yöntemi, 4. adımda istenilen tolerans aralığında kökü bulmuştur

iterasyon= 4
kok= 0.7390851332151607
hata= -1.7012335984389892e-10

Regula Falsi yöntemi , 13. adımda istenilen tolerans aralığında kökü bulmuştur
iterasyon= 12
hata= 5.329070518200751e-15
kok= 0.7390851332151605

iterasyon= 13
hata= 0                 
kok= 0.7390851332151607

Newton Raphson yöntemi daha hızlı olduğu görülmüştür.


'''