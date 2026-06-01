# 🤖 BCG X GenAI Job Simulation – Financial Chatbot & Data Analysis

![BCG X](https://img.shields.io/badge/BCG%20X-GenAI%20Consulting-006400?style=for-the-badge)
![Forage](https://img.shields.io/badge/Forage-Job%20Simulation-00BFFF?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

> **Completed:** June 1, 2026 &nbsp;|&nbsp; **Issued by:** Forage &nbsp;|&nbsp; **Program:** BCG X GenAI Consulting Job Simulation

---

## 📋 Overview

This repository contains my work from the **BCG X GenAI Job Simulation** on Forage, where I worked as an analyst on BCG's GenAI Consulting team for a fictional client — **Global Finance Corp. (GFC)**.

The goal was to build an **AI-powered financial chatbot** that transforms complex 10-K filing data into clear, conversational financial insights for non-technical users.

---

## 🗂️ Project Structure

```
bcg-genai-simulation/
│
├── chatbot.py                          # Main rule-based financial chatbot
├── test_chatbot.py                     # Test suite (12 test cases)
├── test_results.txt                    # All test outputs
├── documentation.md                   # Chatbot documentation & usage guide
│
├── notebooks/
│   └── BCG_Task1_Final.ipynb          # Financial data analysis notebook
│
└── data/
    ├── financial_data.csv             # Extracted financial data (CSV)
    └── BCG_Financial_Data_Harsh.xlsx  # Raw financial data from 10-K filings
```

---

## 🚀 Tasks Completed

### ✅ Task 1 – Data Extraction & Financial Analysis
- Manually extracted financial data from **10-K filings** of **Microsoft, Tesla, and Apple** (FY2023–FY2025) via SEC EDGAR
- Analyzed 5 key financial metrics:
  - Total Revenue
  - Net Income
  - Total Assets
  - Total Liabilities
  - Cash Flow from Operating Activities
- Performed data cleaning, preprocessing, and exploratory analysis using **Python & pandas**
- Built visualizations to identify trends and year-over-year growth patterns

### ✅ Task 2 – AI-Powered Financial Chatbot Development
- Designed and built a **rule-based chatbot** in Python that provides conversational financial insights
- Chatbot supports **7 query types** including revenue lookup, net income analysis, asset overview, cash flow analysis, full financial health summary, and multi-company comparisons
- Implemented **intent detection** (what metric?) + **entity recognition** (which company?) logic
- Wrote a **12-case test suite** to validate all query responses

---

## 💬 Sample Chatbot Interaction

```
You: What is Microsoft's total revenue?
Bot: Microsoft's total revenue in FY2025 was $281,724 million.
     This increased by 14.9% compared to FY2024 ($245,122 million).

You: Give me a financial health summary of Tesla
Bot: === Tesla Financial Health Summary (FY2025) ===
     Revenue:           $94,827 million
     Net Income:        $3,855 million
     Profit Margin:     4.1%
     Total Assets:      $137,806 million
     Debt/Asset Ratio:  39.9%
     Operating CF:      $14,747 million
     2-Year Rev Growth: -2.0%
     2-Year NI Growth:  -74.3%

You: Compare all companies
Bot: [Side-by-side comparison table of Microsoft, Tesla, Apple]
```

---

## 🛠️ Tech Stack

| Tool | Usage |
|------|-------|
| Python 3.x | Core programming language |
| Pandas | Data manipulation & analysis |
| Matplotlib | Data visualization |
| Jupyter Notebook | Analysis & reporting |
| SEC EDGAR | Data source (10-K filings) |
| Git & GitHub | Version control |

---

## 📊 Companies & Data Coverage

| Company | Ticker | Data Source | Years Covered |
|---------|--------|-------------|---------------|
| Microsoft | MSFT | SEC EDGAR / Annual Report | FY2023 – FY2025 |
| Tesla | TSLA | SEC EDGAR / 10-K Filing | FY2023 – FY2025 |
| Apple | AAPL | SEC EDGAR / 10-K Filing | FY2023 – FY2025 |

---

## ▶️ How to Run

```bash
# Clone the repo
git clone https://github.com/harshrana1/bcg-genai-simulation.git
cd bcg-genai-simulation

# Run the chatbot interactively
python chatbot.py

# Run the test suite
python test_chatbot.py
```

---

## 🏆 Certificate

This project was completed as part of the **BCG X GenAI Job Simulation** on Forage.

- 📅 **Completed:** June 1, 2026
- 🔖 **Enrolment Verification Code:** Gc7vaMiagXdPkiFKH
- ✅ **Issued by:** Forage | BCG X

---

## 👤 Author

**Harsh Rana**
- GitHub: [@harshrana1](https://github.com/harshrana1)

---

*BCG X GenAI Consulting Team | GFC AI Chatbot Project | Forage Job Simulation*
