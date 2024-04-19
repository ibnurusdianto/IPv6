import socket
try:
    import colorama
    colorama.init()  # Initialize colorama for Windows
except ImportError:
    pass 

# warna
green = "\033[92m"  # Green text
yellow = "\033[93m"  # Yellow text
red = "\033[91m"  # Red text
cyan = "\033[96m"  # Cyan text
reset = "\033[0m"  # Reset text color

def periksa_dukungan_ipv6(domain):
    try:
        # Check Jika IPv6 support
        hasil = socket.getaddrinfo(domain, None, socket.AF_INET6)
        if hasil:
            print(green + "[+] Situs web mendukung IPv6" + reset)
        else:
            print(yellow + "[-] Situs web tidak mendukung IPv6" + reset)

    except socket.gaierror:
        print(red + "[-] Domain situs web mungkin tidak valid atau mengalami masalah DNS" + reset)

if __name__ == "__main__":
    while True:
        domain = input(cyan + "Masukkan domain situs web (atau ketik 'quit' untuk keluar): " + reset)
        if domain == 'quit':
            break
        periksa_dukungan_ipv6(domain)
