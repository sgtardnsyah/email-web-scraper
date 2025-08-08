# EMAIL-WEB-SCRAPER

_Uncover Contacts Faster, Power Your Outreach Efforts_

[![last commit](https://img.shields.io/github/last-commit/sgtardnsyah/email-web-scraper)](https://github.com/sgtardnsyah/email-web-scraper)
[![python](https://img.shields.io/badge/python-100%25-blue)](https://python.org/)
[![pandas](https://img.shields.io/badge/pandas-yes-green)](https://pandas.pydata.org/)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Example Output](#example-output)
- [Disclaimer](#disclaimer)
- [Credits](#credits)

---

## Overview

**email-web-scraper** is a versatile developer tool designed to automate the extraction of email addresses from multiple websites, consolidating results into organized Excel reports.  
It streamlines data collection workflows, making outreach and contact discovery more efficient.

---

## Features

- **URL Management:** Centralized URL configuration for easier scraping management.
- **Structured Reporting:** Automatically compiles found emails into Excel files for easy analysis.
- **Automation:** Scrapes emails from multiple websites with minimal manual steps.
- **Dependency Handling:** Uses essential libraries for HTTP requests, HTML parsing, and data processing.
- **Seamless Integration:** Can be integrated into larger data collection or lead generation projects.

---

## Getting Started

### Prerequisites

- **Python** (recommended: Python 3.8+)
- **Pip** (for package management)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/sgtardnsyah/email-web-scraper.git
    cd email-web-scraper
    ```
2. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Prepare your `urls.txt` file:**  
   List the websites you want to scrape, one per line

2. **Run the script:**
 ```bash
 python emailwebscraper.py
 ```

3. **Get the results:**  
Results are saved as `email_scrape_results.xlsx` and can be opened in Excel or Google Sheets.

---

## Example Output

| WEBSITE              | EMAIL 1          | EMAIL 2      |
|----------------------|------------------|--------------|
| https://website1.com | info@abc.com     | hr@abc.com   |
| https://website2.com |                  |              |
| https://website3.com | hello@xyz.com    |              |

---

## Disclaimer

- **Use this script responsibly and in accordance with each website's terms of service.**
- Do not use for spam or any illegal purposes.

---

## Credits

Developed by [Cik (sigitardiansyah24)](https://github.com/sigitardiansyah24).  
Feel free to fork, modify, or contribute!

---
