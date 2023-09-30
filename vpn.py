import socket
import ssl

def proxy(client_socket, server_address, server_port):
    # İstemciden gelen bağlantıyı kabul et
    client_request = client_socket.recv(1024)

    # İstemci isteğini hedef sunucuya yönlendir
    server_socket = socket.create_connection(server_address, server_port)
    server_socket = ssl.wrap_socket(server_socket)
    server_socket.sendall(client_request)

    # Hedef sunucudan gelen yanıtı istemciye geri gönder
    server_response = server_socket.recv(1024)
    client_socket.sendall(server_response)

    server_socket.close()

def main():
    # Bir bağlantı noktası dinleyicisi oluştur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))
    server_socket.listen(1)

    # İstemci bağlantılarını kabul et ve proxy'yi çalıştır
    while True:
        client_socket, client_address = server_socket.accept()
        proxy(client_socket, "www.google.com", 443)

if __name__ == "__main__":
    main()
