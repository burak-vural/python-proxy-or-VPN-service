import socket
import ssl
import requests
from selenium import webdriver

def main():
    # Proxyleri listeleyelim
    proxy_list = ["192.168.1.10:8080", "192.168.1.11:8080", "192.168.1.12:8080"]

    # Kullanıcıdan proxy seçmesini isteyelim
    proxy_index = int(input("Hangi proxyden bağlanmak istersiniz? (1, 2, 3): "))

    # Proxy üzerinden bağlantı kuralım
    proxy = proxy_list[proxy_index - 1]
    proxy_address = proxy.split(":")[0]
    proxy_port = int(proxy.split(":")[1])

    # Chrome tarayıcısını başlatalım
    driver = webdriver.Chrome()

    # Google'a bağlanalım
    driver.get("https://www.google.com")

    # Sayfanın başlığını alalım
    title = driver.title

    # Tarayıcıyı kapatalım
    driver.close()

    # Başlığı yazdıralım
    print(title)

if __name__ == "__main__":
    main()



#------------------------------------------------------------------------------#

#Güvenlik: Proxy üzerinden bağlantı kurarken SSL/TLS
#Loglama: Tarayıcının etkinliğini loglamak için bir logger
#Engelleme: Belirli sitelere veya içeriklere erişimi engelle
#Ölçüm: Tarayıcının performansını ölçmek için bir metrikler sistemi





import socket
import ssl
import requests
from selenium import webdriver
import logging

def main():
    # Proxyleri listeleyelim
    proxy_list = ["192.168.1.10:8080", "192.168.1.11:8080", "192.168.1.12:8080"]

    # Kullanıcıdan proxy seçmesini isteyelim
    proxy_index = int(input("Hangi proxyden bağlanmak istersiniz? (1, 2, 3): "))

    # Proxy üzerinden bağlantı kuralım
    proxy = proxy_list[proxy_index - 1]
    proxy_address = proxy.split(":")[0]
    proxy_port = int(proxy.split(":")[1])

    # Proxy üzerinden bağlantı kurarken SSL/TLS kullanalım
    proxy_ssl = True if proxy_index == 1 else False

    # Tarayıcıyı başlatalım
    driver = webdriver.Chrome()

    # Proxy ayarlarını yapalım
    driver.set_proxy(proxy_address, proxy_port, proxy_ssl)

    # Google'a bağlanalım
    driver.get("https://www.google.com")

    # Sayfanın başlığını alalım
    title = driver.title

    # Tarayıcıyı kapatalım
    driver.close()

    # Başlığı yazdıralım
    print(title)

    # Loglama yapalım
    logger = logging.getLogger(__name__)
    logger.info("Proxy üzerinden bağlantı kuruldu.")
    logger.info("Sayfa başlığı: %s", title)

if __name__ == "__main__":
    main()
