from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    # Proxyleri listeleyelim
    proxy_list = [
        "145.239.85.58:9300",
        "82.196.11.105:1080",
        "81.171.24.199:3128",
        "185.12.143.143:8080",
    ]

    # Selenium tarayıcı sürücüsü için seçenekler nesnesi oluştur
    options = Options()

    # User-Agent ayarını yapalım (Google Chrome olarak)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")

    # Hangi proxyden bağlanmak istersiniz? Proxy adreslerini tek tek dene
    for proxy in proxy_list:
        proxy_address = proxy.split(":")[0]
        proxy_port = proxy.split(":")[1]

        # Proxy üzerinden bağlantı kurarken SSL/TLS kullanalım
        proxy_ssl = False

        # Proxy özelliklerini seçenekler nesnesi ile ayarla
        options.add_argument("--proxy-server=http://" + proxy)
        options.add_argument("--proxy-server=https://" + proxy)

        # Selenium tarayıcı sürücüsünü başlat
        driver = webdriver.Chrome(options=options)

        try:
            # Bağlantıyı kontrol etmek için Google'a git
            driver.get("https://www.google.com")
            print(f"Başarılı bir şekilde {proxy} adresi ile Google'a bağlandı.")
            break  # Başarılı bir proxy bulundu, döngüyü sonlandır
        except Exception as e:
            print(f"{proxy} adresi ile bağlantı kurulamadı. Hata: {e}")
            driver.quit()  # Bağlantı başarısız, tarayıcıyı kapat

    # Programı durduralım
    exit()

if __name__ == "__main__":
    main()
