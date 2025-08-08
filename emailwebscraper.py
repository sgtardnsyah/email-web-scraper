import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Baca URL dari file
with open(r'C:\Users\Pamerindo\Documents\SIGIT\NGODING DER\Project kelar\Scraping Email From Website\urls.txt', 'r') as file:
    urls = [line.strip() for line in file if line.strip()]

results = []

for index, url in enumerate(urls):
    nomor = index + 1
    print(f"\n[{nomor}/{len(urls)}] Memproses: {url}")
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text(separator='\n')

            # Cari email
            emails = list(set(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)))

            result = {'WEBSITE': url}
            if emails:
                result['EMAIL 1'] = emails[0]
                if len(emails) > 1:
                    result['EMAIL 2'] = ' / '.join(emails[1:])
                else:
                    result['EMAIL 2'] = ''
                print(f"✅ Ditemukan {len(emails)} email: {', '.join(emails)}")
            else:
                result['EMAIL 1'] = ''
                result['EMAIL 2'] = ''
                print("❌ Tidak ada email ditemukan.")

            results.append(result)

        else:
            results.append({'WEBSITE': url, 'EMAIL 1': f'', 'EMAIL 2': ''})
            print(f"⚠️ Gagal diakses. Status code : {response.status_code}")
    except requests.exceptions.RequestException as e:
        results.append({'WEBSITE': url, 'EMAIL 1': f'', 'EMAIL 2': ''})
        print(f"🚫 Error saat mengakses : {e}")

# Simpan hasil
df = pd.DataFrame(results)
df.to_excel('email_scrape_results.xlsx', index=False)
print("\n📄 Selesai. Data diekspor ke 'email_scrape_results.xlsx'")