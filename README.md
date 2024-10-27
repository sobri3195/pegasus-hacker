
Pegasus Hacker

## Deskripsi
`pegasus-hacker` adalah alat otomatisasi untuk mengunduh dan menginstal berbagai tools keamanan siber langsung dari GitHub. Tools dikelompokkan dalam kategori seperti Information Gathering, Wireless Hacking, Exploitation, Password Cracking, dan lainnya, membantu praktisi keamanan melakukan berbagai aktivitas mulai dari pengujian penetrasi hingga analisis forensik.

⚠️ Peringatan: Gunakan tools ini secara etis dan hanya pada sistem atau jaringan yang Anda miliki atau telah mendapatkan izin eksplisit. Penyalahgunaan tools ini dapat melanggar hukum.

## Fitur
- Information Gathering: Mengumpulkan informasi dari jaringan dan layanan publik.
- Wireless Hacking: Analisis dan eksploitasi jaringan nirkabel.
- Software Engineering Tools: Phishing dan rekayasa sosial.
- Exploitation Tools: Menerapkan eksploitasi terhadap target.
- Password Cracking: Memecahkan kata sandi dan hash.
- Forensics: Investigasi forensik pada sistem atau perangkat.
- Vulnerability Scanning: Pemindaian celah keamanan.
- Web Application Assessment: Pengujian keamanan aplikasi web.

## Cara Instalasi

1. Clone repository ini:
   git clone https://github.com/sobri3195/pegasus-hacker.git
   cd pegasus-hacker

2. Install dependencies:
   pip install -r requirements.txt

3. Jalankan script untuk menginstal semua tools:
   python pegasus_hacker.py

## Tools Per Kategori

1. Information Gathering:
   - Nmap: https://github.com/nmap/nmap
   - Shodan: https://github.com/shodan/python-shodan
   - Amass: https://github.com/Amass/amass
   - Recon-NG: https://github.com/lanmaster53/recon-ng
   - Gobuster: https://github.com/OJ/gobuster

2. Wireless Hacking:
   - Aircrack-ng: https://github.com/aircrack-ng/aircrack-ng
   - Wifite: https://github.com/derv82/wifite
   - Kismet: https://github.com/kismetwireless/kismet
   - TCPDump: https://github.com/the-tcpdump-group/tcpdump

3. Software Engineering Tools:
   - GoPhish: https://github.com/gophish/gophish
   - HiddenEye: https://github.com/D4Vinci/HiddenEye
   - SocialFish: https://github.com/An0nUD4Y/SocialFish
   - EvilURL: https://github.com/UndeadSec/EvilURL
   - Evilginx2: https://github.com/kgretzky/evilginx2

4. Exploitation Tools:
   - Metasploit: https://github.com/rapid7/metasploit-framework
   - SQLMap: https://github.com/sqlmapproject/sqlmap
   - OWASP ZAP: https://github.com/zaproxy/zaproxy
   - ExploitDB: https://github.com/offensive-security/exploitdb

5. Password Cracking:
   - John The Ripper: https://github.com/magnumripper/JohnTheRipper
   - Hashcat: https://github.com/hashcat/hashcat
   - Hydra: https://github.com/foofus/hydra
   - Medusa: https://github.com/medusa-project/medusa

6. Forensics:
   - SleuthKit: https://github.com/sleuthkit/sleuthkit
   - Volatility: https://github.com/volatilityfoundation/volatility3
   - Guymager: https://github.com/pyFlag/guymager
   - Binwalk: https://github.com/ReFirmLabs/binwalk
   - Wireshark: https://github.com/wireshark/wireshark

7. Vulnerability Scanning:
   - OpenVAS: https://github.com/greenbone/openvas-scanner
   - Nessus: https://github.com/tenable/nessus-agent
   - LYNIS: https://github.com/CISOfy/lynis

8. Web Application Assessment:
   - OWASP ZAP: https://github.com/OWASP/OWASP-ZAP
   - Nikto: https://github.com/sullo/nikto
   - WPScan: https://github.com/wpscanteam/wpscan
   - Retire.js: https://github.com/appsecco/retire-js

## Cara Kerja Tools

Script `pegasus_hacker.py` akan melakukan:
1. Membuat folder bernama `tools/`.
2. Untuk setiap kategori, script akan mengunduh repository yang terdaftar melalui git clone.
3. Semua repository akan disimpan dalam folder `tools/<kategori>/`.

## Catatan Penting
- Beberapa tools seperti Cobalt Strike memerlukan lisensi untuk penggunaan penuh.
- Pastikan Anda memiliki izin sah untuk menjalankan alat ini di jaringan atau sistem yang Anda uji.
- Beberapa tools mungkin memerlukan hak akses root/administrator.

## Kontribusi
Jika Anda ingin menambahkan tools atau memperbaiki bug:
1. Fork repository ini.
2. Buat branch baru:
   git checkout -b feature-branch
3. Commit perubahan Anda dan kirim pull request.

## Lisensi
Project ini dilisensikan di bawah lisensi MIT.

## Kontak
Dibuat oleh: Muhammad Sobri Maulana
