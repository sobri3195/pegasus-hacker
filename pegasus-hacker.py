import os
import subprocess

# Daftar tools dari setiap kategori dengan URL GitHub terkait (sebisa mungkin resmi)
tools = {
    "Information_Gathering": [
        "https://github.com/nmap/nmap",
        "https://github.com/shodan/python-shodan",
        "https://github.com/Amass/amass",
        "https://github.com/lanmaster53/recon-ng",
        "https://github.com/OJ/gobuster",
    ],
    "Wireless_Hacking": [
        "https://github.com/aircrack-ng/aircrack-ng",
        "https://github.com/derv82/wifite",
        "https://github.com/kismetwireless/kismet",
        "https://github.com/the-tcpdump-group/tcpdump",
        "https://github.com/Aircrack-ng/rtl8812au",
    ],
    "Software_Engineering": [
        "https://github.com/gophish/gophish",
        "https://github.com/D4Vinci/HiddenEye",
        "https://github.com/An0nUD4Y/SocialFish",
        "https://github.com/UndeadSec/EvilURL",
        "https://github.com/kgretzky/evilginx2",
    ],
    "Exploitation": [
        "https://github.com/rapid7/metasploit-framework",
        "https://github.com/sqlmapproject/sqlmap",
        "https://github.com/zaproxy/zaproxy",
        "https://github.com/offensive-security/exploitdb",
        "https://github.com/CoreSecurity/impacket",
        "https://github.com/Cobalt-Strike",
    ],
    "Password_Cracking": [
        "https://github.com/magnumripper/JohnTheRipper",
        "https://github.com/hashcat/hashcat",
        "https://github.com/foofus/hydra",
        "https://github.com/medusa-project/medusa",
    ],
    "Forensics": [
        "https://github.com/sleuthkit/sleuthkit",
        "https://github.com/volatilityfoundation/volatility3",
        "https://github.com/pyFlag/guymager",
        "https://github.com/ReFirmLabs/binwalk",
        "https://github.com/wireshark/wireshark",
    ],
    "Vulnerability_Scanning": [
        "https://github.com/greenbone/openvas-scanner",
        "https://github.com/tenable/nessus-agent",
        "https://github.com/lcamtuf/afl",
        "https://github.com/wireghoul/scancode-toolkit",
    ],
    "Web_Application_Assessment": [
        "https://github.com/OWASP/OWASP-ZAP",
        "https://github.com/sullo/nikto",
        "https://github.com/wpscanteam/wpscan",
        "https://github.com/appsecco/retire-js",
    ],
}

# Fungsi untuk meng-clone repositori dari GitHub
def clone_repo(url):
    try:
        print(f"Cloning {url}...")
        subprocess.run(["git", "clone", url], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone {url}: {e}")

# Fungsi untuk menginstal semua tools
def install_all_tools():
    os.makedirs("tools", exist_ok=True)
    os.chdir("tools")

    for category, urls in tools.items():
        print(f"\nInstalling tools for {category}...\n")
        for url in urls:
            clone_repo(url)

if __name__ == "__main__":
    install_all_tools()
