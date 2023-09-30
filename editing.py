import socket
import ssl
from selenium import webdriver

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

    # ChromeDriver'ın yolunu belirleyelim
    chromedriver_path = "C:/path/to/chromedriver.exe"  # ChromeDriver'ın tam yolu

    # Tarayıcıyı başlatalım
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=http://{}:{}'.format(proxy_address, proxy_port))
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

    # Useragent ayarlarını yapalım
    driver.execute_cdp_cmd("Network.setUserAgentOverride", {
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    })

    # Bağlantı kuralım
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
