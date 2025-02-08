import socket
try:
    import colorama
    colorama.init()  # Initialize colorama for Windows
except ImportError:
    pass 

# Warna dan Emoji
green = "\033[92m"  # Green text
yellow = "\033[93m"  # Yellow text
red = "\033[91m"  # Red text
cyan = "\033[96m"  # Cyan text
reset = "\033[0m"  # Reset text color
check_mark = "✅"
cross_mark = "❌"
warning_sign = "⚠️"
information_source = "ℹ️"

def periksa_dukungan_ipv6(domain):
    try:
        # Memeriksa dukungan IPv6
        hasil = socket.getaddrinfo(domain, None, socket.AF_INET6)
        if hasil:
            ipv6_addresses = [addr[4][0] for addr in hasil]
            ipv6_addresses_str = "\n".join(ipv6_addresses)
            print(green + f"{check_mark} Situs web mendukung IPv6:\n{ipv6_addresses_str}" + reset)
        else:
            print(yellow + f"{cross_mark} Situs web tidak mendukung IPv6" + reset)

    except socket.gaierror:
        print(red + f"{warning_sign} Domain situs web mungkin tidak valid atau mengalami masalah DNS" + reset)

if __name__ == "__main__":
    print(cyan + f"{information_source} Program memeriksa dukungan IPv6 untuk domain situs web" + reset)
    while True:
        domain = input(cyan + "Masukkan domain situs web (atau ketik 'quit' untuk keluar): " + reset)
        if domain.lower() == 'quit':
            print(cyan + f"{information_source} Keluar dari program..." + reset)
            break
        periksa_dukungan_ipv6(domain)
