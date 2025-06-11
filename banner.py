from colorama import Fore, Style

def banner():
    print(Fore.RED + Style.BRIGHT + "═" * 60)
    print(Fore.CYAN + Style.BRIGHT + "║{:^58}║".format("Faizan™ Stealth Tracker v1.0"))
    print(Fore.GREEN + "║{:^58}║".format("Power | Privacy | Precision"))
    print(Fore.RED + "═" * 60 + Style.RESET_ALL)
