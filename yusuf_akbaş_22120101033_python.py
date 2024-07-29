'''yusuf akbas odev1'''


a=float(input("para girisi yapiniz"))
if a==0 :
    print("sifir  girdiniz")
if (a/200)>0:
    b=int(a/200)
    print(b,"tane 200")
            
if (a%200)>=100:
    print("1 tane 100")
        
if (a%100)>=50:
    print("1 tane 50")
        
if (a%50)>=20:
    c=a%50
    if int(c/20)>1 :
        print("2 tane 20")        
    elif int(c/20)==1:  
        print("1 tane 20")   
c=a%50
if (c%20)>=10:
    print("1 tane 10")
            
if(a%10)>=5:
    print("1 tane 5")
d=int(c%5)       
if int(d)!=0 : 
    print(d,"tane 1")  
d=c%1       
if d%1<1:
    if d%1!=0:        
        print("1 tane 0,5")


'''yusuf akbas odev2'''


class insan:
    def __init__(self, isim, yas):
        self.isim ="yusuf"
        self.yas =19
    def bilgi_goster(self):
        print("Isim:",self.isim,"\n" "Yas:",self.yas)


class calisan(insan):
    def __init__(self, isim, yas, calisan_id, maas):
        super().__init__(isim, yas)
        self.calisan_id =1234
        self.maas =50000
    def bilgi_goster(self):
        print("isim:",self.isim,"\n""yas:",self.yas,'''
calisan_id:''',self.calisan_id,"\n""maas:",self.maas)


class yonetici(calisan):
    def __init__(self, isim, yas, calisan_id, maas, takim_calisan_sayisi):
        super().__init__(isim, yas, calisan_id, maas)
        self.takim_calisan_sayisi =12
    def bilgi_goster(self):
        print("isim:",self.isim,"\n""yas:",self.yas,"\n""calisan_id:",self.calisan_id,'''
maas:''',self.maas,"\ntakim calisan sayisi",self.takim_calisan_sayisi)
 

print("insan icin bilgileri_göster ciktisi")       
yusuf=insan("g",33)
yusuf.bilgi_goster()


print("\ncalisan icin bilgileri_göster ciktisi")
yusuf=calisan("g",3,4,7)
yusuf.bilgi_goster()


print("\nyonetici icin bilgileri göster ciktisi")
yusuf=yonetici("a",5,9,3,1)
yusuf.bilgi_goster()


     
    
    