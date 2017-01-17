import requests
import sys
from time import sleep
__author__ = "Hacknology"

url = input("[*]Id değeriyle birlikte url'yi giriniz: ")
r = requests.get(url)
if r.status_code == 200:
    print("[+] Başarılı! Id değeri arttırılıyor..")
    id_deger = 0
    x = requests.get(url,
                     params={"id":id_deger})
    while x.status_code == 200:
        id_deger += 1
        x = requests.get(url,
                     params={"id":id_deger})
        
        yeni_url = x.url
        f = open("dosyalar.txt", "a+")
        f.write(yeni_url+ "\n")
else:
    print("[-] Başarısız, düzgün bir url girin: ")
    sleep(5)
    sys.exit()
    
        
