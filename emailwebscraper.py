import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Read URLs from file in the current directory
with open('urls.txt', 'r') as file:
    urls = [line.strip() for line in file if line.strip()]

results = []

for index, url in enumerate(urls):
    number = index + 1
    print(f"\n[{number}/{len(urls)}] Processing: {url}")
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text(separator='\n')

            # Find emails
            emails = list(set(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)))

            result = {'WEBSITE': url}
            if emails:
                result['EMAIL 1'] = emails[0]
                if len(emails) > 1:
                    result['EMAIL 2'] = ' / '.join(emails[1:])
                else:
                    result['EMAIL 2'] = ''
                print(f"✅ Found {len(emails)} email(s): {', '.join(emails)}")
            else:
                result['EMAIL 1'] = ''
                result['EMAIL 2'] = ''
                print("❌ No emails found.")

            results.append(result)

        else:
            results.append({'WEBSITE': url, 'EMAIL 1': '', 'EMAIL 2': ''})
            print(f"⚠️ Failed to access. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        results.append({'WEBSITE': url, 'EMAIL 1': '', 'EMAIL 2': ''})
        print(f"🚫 Error accessing URL: {e}")

# Save results
df = pd.DataFrame(results)
df.to_excel('email_scrape_results.xlsx', index=False)

print("\n📄 Done. Data exported to 'email_scrape_results.xlsx'")
