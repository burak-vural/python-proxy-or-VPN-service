import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    # Proxyleri listeleyelim
    proxy_list = [
        "de.proxymesh.com:8080",
        "fr.proxymesh.com:8080",
        "it.proxymesh.com:8080",
        "es.proxymesh.com:8080",
    ]

    # Kullanıcıdan proxy seçmesini isteyelim
    proxy_index = int(input("Hangi proxyden bağlanmak istersiniz? (1, 2, 3, 4): "))

    # Proxy üzerinden bağlantı kuralım
    proxy = proxy_list[proxy_index - 1]
    proxy_address = proxy.split(":")[0]
    proxy_port = int(proxy.split(":")[1])

    # Proxy üzerinden bağlantı kurarken SSL/TLS kullanalım
    proxy_ssl = False

    # Selenium tarayıcı sürücüsü için seçenekler nesnesi oluştur
    options = Options()

    # Proxy özelliklerini seçenekler nesnesi ile ayarla
    options.add_argument('--proxy-server=http://{}:{}'.format(proxy_address, proxy_port))

    # Selenium tarayıcı sürücüsü başlat
    driver = selenium.webdriver.Chrome(options=options)

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
