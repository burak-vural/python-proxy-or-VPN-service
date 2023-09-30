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

#------------------------------------------------------------------------------#

# Add User Agent

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

    # Useragent ayarlarını yapalım
    driver.set_user_agent(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    )

    # Ülkeyi seçelim
    country_code = input("Hangi ülkenin IP adresini kullanmak istersiniz? (TR, US, FR, JP): ")

    # Proxy adresini güncelleyelim
    proxy_address = f"{country_code}.proxymesh.com:8080"

    # Bağlantı kuralım
    driver.set_proxy(proxy_address, proxy_port, proxy_ssl)
    driver.get("https://www.google.com")

    # Kullanıcıdan tarayıcıyı kapatmasını isteyelim
    while True:
        decision = input("Tarayıcıyı kapatmak ister misiniz? (E/H): ")
        if decision == "E":
            driver.quit()
            break

    # Programı durduralım
    exit()

if __name__ == "__main__":
    main()

#------------------------------------------------------------------------------#

EU-RU IP Adress

import socket
import ssl
import requests
from selenium import webdriver
import random
import logging

def main():
    # Proxyleri listeleyelim
    proxy_list = [
        "192.168.1.10:8080",
        "192.168.1.11:8080",
        "192.168.1.12:8080",
    ]

    # Proxyleri güncelleyelim
    proxy_list[0] = "es.proxymesh.com:8080"
    proxy_list[1] = "fr.proxymesh.com:8080"
    proxy_list[2] = "gr.proxymesh.com:8080"
    proxy_list[3] = "ru.proxymesh.com:8080"

    # Kullanıcıdan proxy seçmesini isteyelim
    proxy_index = int(input("Hangi proxyden bağlanmak istersiniz? (1, 2, 3, 4): "))

    # Proxy üzerinden bağlantı kuralım
    proxy = proxy_list[proxy_index - 1]
    proxy_address = proxy.split(":")[0]
    proxy_port = int(proxy.split(":")[1])

    # Proxy üzerinden bağlantı kurarken SSL/TLS kullanalım
    proxy_ssl = True if proxy_index == 1 else False

    # Tarayıcıyı başlatalım
    driver = webdriver.Chrome()

    # Useragent ayarlarını yapalım
    driver.set_user_agent(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    )

    # Bağlantı kuralım
    driver.set_proxy(proxy_address, proxy_port, proxy_ssl)
    driver.get("https://www.google.com")

    # Kullanıcıdan tarayıcıyı kapatmasını isteyelim
    while True:
        decision = input("Tarayıcıyı kapatmak ister misiniz? (E/H): ")
        if decision == "E":
            driver.quit()
            break

    # Programı durduralım
    exit()

if __name__ == "__main__":
    main()

#------------------------------------------------------------------------------#

#cybersecurity

import socket
import ssl
import requests
from selenium import webdriver
import random
import logging

def main():
    # Proxyleri listeleyelim
    proxy_list = [
        "de.proxymesh.com:8080",
        "fr.proxymesh.com:8080",
        "it.proxymesh.com:8080",
        "es.proxymesh.com:8080",
    ]

    # Proxyleri güncelleyelim
    proxy_list[0] = "de.proxymesh.com:8080"
    proxy_list[1] = "fr.proxymesh.com:8080"
    proxy_list[2] = "it.proxymesh.com:8080"
    proxy_list[3] = "es.proxymesh.com:8080"

    # Kullanıcıdan proxy seçmesini isteyelim
    proxy_index = int(input("Hangi proxyden bağlanmak istersiniz? (1, 2, 3, 4): "))

    # Proxy üzerinden bağlantı kuralım
    proxy = proxy_list[proxy_index - 1]
    proxy_address = proxy.split(":")[0]
    proxy_port = int(proxy.split(":")[1])

    # Proxy üzerinden bağlantı kurarken SSL/TLS kullanalım
    proxy_ssl = False

    # Tarayıcıyı başlatalım
    driver = webdriver.Chrome()

    # Useragent ayarlarını yapalım
    driver.set_user_agent(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    )

    # Bağlantı kuralım
    driver.set_proxy(proxy_address, proxy_port, proxy_ssl)
    driver.get("https://www.google.com")

    # Kullanıcıdan tarayıcıyı kapatmasını isteyelim
    while True:
        decision = input("Tarayıcıyı kapatmak ister misiniz? (E/H): ")
        if decision == "E":
            driver.quit()
            break

    # Programı durduralım
    exit()

if __name__ == "__main__":
    main()
