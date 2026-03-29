import pyperclip
from utils.url_decoder import decode_url


def main():
    
    encoded_url = input("Введіть URL: ")

    
    decoded_url = decode_url(encoded_url)

    
    print("\nДекодований URL:")
    print(decoded_url)

    
    pyperclip.copy(decoded_url)
    print("\n✔ Скопійовано в буфер обміну!")


if __name__ == "__main__":
    main()