#FERRAMENTA CONSTRUIDA PELO SRJARE337
import socket
import sys
import time
from colorama import Fore, Style, init, Back

init(autoreset=True)

common_subdomains = [subdomains.txt]


def styled_print(text, color=Fore.GREEN, delay=0.01, bold=False):
    style = color
    if bold:
        style += Style.BRIGHT

    sys.stdout.write(style)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

def loading_animation():
    animation_frames = ['|', '/', '-', '\\']
    for _ in range(10):
        for frame in animation_frames:
            sys.stdout.write(f"\r{Fore.YELLOW}Carregando enumeração {frame}")
            sys.stdout.flush()
            time.sleep(0.2)
    sys.stdout.write(f"\r{Fore.GREEN}Carregamento Completo! \n")
    print(Style.RESET_ALL)

def check_subdomain(domain, subdomain):
    try:
        full_domain = f"{subdomain}.{domain}"
        ip = socket.gethostbyname(full_domain)
        return ip
    except socket.error:
        return None

def enumerate_subdomains(domain):
    active_subdomains = []
    start_time = time.time()

    styled_print(f'\nIniciando a enumeração de subdomínios para {domain}...', Fore.LIGHTYELLOW_EX, bold=True)
    loading_animation()

    for subdomain in common_subdomains:
        ip = check_subdomain(domain, subdomain)
        if ip:
            active_subdomains.append((subdomain, ip))

    end_time = time.time()
    duration = end_time - start_time

    styled_print(f'\nSubdomínios ativos para {domain}:', Fore.LIGHTGREEN_EX, bold=True)
    for index, (subdomain, ip) in enumerate(active_subdomains, start=1):
        styled_print(f'{index}. {subdomain}.{domain} - {ip}', Fore.LIGHTGREEN_EX, delay=0.02, bold=True)

    styled_print(f'\nDuração da enumeração: {duration:.2f} segundos', Fore.CYAN, bold=True)

def print_credits():
    styled_print('\nFerramenta desenvolvida por SrJare337', Fore.RED, bold=True)
    styled_print('Versão: V1.1', Fore.RED, bold=True)

def print_intro():
    border_length = 60
    title = "🔥HACKER SUBDOMAIN ENUMERATOR🔥"
    credits = "Ferramenta desenvolvida por SrJare337"
    padding_title = (border_length - len(title) - 4) // 2
    padding_credits = (border_length - len(credits) - 4) // 2
    border = "=" * border_length
    middle_line_title = f" {' ' * padding_title}{title} {' ' * padding_title} "
    middle_line_credits = f" {' ' * padding_credits}{credits} {' ' * padding_credits} "

    print(Back.BLACK + Fore.GREEN + border)
    styled_print(middle_line_title, Fore.LIGHTCYAN_EX, bold=True)
    styled_print(middle_line_credits, Fore.LIGHTCYAN_EX, bold=True)
    print(Fore.GREEN + border)

if __name__ == "__main__":
    print_intro()
    domain = input(Fore.CYAN + "Digite o domínio para verificar (exemplo.com): " + Style.RESET_ALL).strip()

    enumerate_subdomains(domain)
    print_credits()
