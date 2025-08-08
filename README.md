# Email Web Scraper 📧

<p align="center">
  <a href="https://github.com/sgtardnsyah/email-web-scraper/commits/main">
    <img src="https://img.shields.io/github/last-commit/sgtardnsyah/email-web-scraper?logo=git&color=informational" alt="last commit">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-100%25-blue?logo=python" alt="python 100%">
  </a>
  <a href="https://github.com/sgtardnsyah/email-web-scraper/search?l=python">
    <img src="https://img.shields.io/github/languages/count/sgtardnsyah/email-web-scraper?color=blue" alt="languages">
  </a>
</p>

---

**Email Web Scraper** is a simple yet powerful Python tool to extract email addresses from a list of websites, save them to Excel, and speed up your data collection!

---

## 🚀 Built With

<p align="center">
  <a href="https://daringfireball.net/projects/markdown/">
    <img src="https://img.shields.io/badge/Markdown-000000?logo=markdown&logoColor=white" alt="Markdown">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://pandas.pydata.org/">
    <img src="https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white" alt="pandas">
  </a>
</p>


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

| Package         | Link                                                                |
|-----------------|---------------------------------------------------------------------|
| Python 3.x      | [python.org](https://www.python.org/)                               |
| requests        | [requests](https://pypi.org/project/requests/)                      |
| beautifulsoup4  | [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)          |
| pandas          | [pandas](https://pypi.org/project/pandas/)                          |
| openpyxl        | [openpyxl](https://pypi.org/project/openpyxl/)                      |

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


## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

> **Happy scraping! 😊**
