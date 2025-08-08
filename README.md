
# Email Web Scraper 📧

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/your-username/your-repository-name/pulls)
[![Issues](https://img.shields.io/github/issues/your-username/your-repository-name.svg)](https://github.com/your-username/your-repository-name/issues)
[![Stars](https://img.shields.io/github/stars/your-username/your-repository-name.svg)](https://github.com/your-username/your-repository-name/stargazers)

---

## Description

**Email Web Scraper** is a simple yet powerful Python tool for extracting email addresses from a list of websites. It reads URLs from a `urls.txt` file, scrapes each website for email addresses, and exports the results into an Excel file. Perfect for lead generation, data collection, or any use case where you need to gather contact information from multiple online sources efficiently.

---

## Features ✨

- **Bulk Scraping:** Processes multiple URLs from `urls.txt` in one go.
- **Email Extraction:** Uses regex to find and extract all valid email addresses from webpage content.
- **Dual Email Columns:** Organizes found emails into two columns: `EMAIL 1` (the first found) and `EMAIL 2` (additional emails, separated by a slash).
- **Error Handling:** Gracefully handles request timeouts, connection errors, and non-200 status codes—ensuring uninterrupted scraping.
- **Progress Tracking:** Console output shows progress, emails found, and errors encountered.
- **Excel Export:** Automatically saves results in a formatted `.xlsx` file for easy viewing and use.

---

## Requirements 🛠️

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [pandas](https://pypi.org/project/pandas/)
- [openpyxl](https://pypi.org/project/openpyxl/)

**Install all dependencies with:**

```bash
pip install -r requirements.txt
```

---

## How to Use 🚀

Follow these simple steps to get started:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your target URLs

Open or create the file `urls.txt` in the project directory.  
List **one website URL per line**. For example:

```
https://website1.com
https://website2.com
https://website3.com
```

### 4. Run the scraper

```bash
python emailwebscraper.py
```

### 5. Check your results

- When the script finishes, you’ll see a new file named **`email_scrape_results.xlsx`** in the same directory.
- The results will be organized in a table format, for example:

    | WEBSITE              | EMAIL 1         | EMAIL 2      |
    |----------------------|-----------------|--------------|
    | https://website1.com | info@abc.com    | hr@abc.com   |
    | https://website2.com |                 |              |
    | https://website3.com | hello@xyz.com   |              |

---

### Sample Console Output

The script will display progress in your terminal, like:

```
Processing: https://website1.com ... [2 emails found]
Processing: https://website2.com ... [no emails found]
Processing: https://website3.com ... [1 email found]
All done! Results saved to email_scrape_results.xlsx
```

---

### Troubleshooting

- **No emails found?**  
  Make sure the websites have public email addresses visible in their content.

- **Encountering errors?**  
  The script will skip problematic URLs and continue.  
  All errors will be displayed in the console for your review.

---

> **Happy scraping! 😊**
