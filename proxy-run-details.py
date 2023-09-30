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
