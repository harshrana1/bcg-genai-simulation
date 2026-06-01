# GFC Financial Chatbot – Documentation
## BCG GenAI Consulting | Task 2 | Analyst: Harsh

---

## Overview
This is a rule-based AI-powered financial chatbot prototype developed for Global Finance Corp. (GFC) as part of BCG's GenAI Consulting project. The chatbot transforms analyzed 10-K financial data into interactive, conversational insights.

---

## How It Works
The chatbot uses **rule-based if-else logic** to match user queries to predefined financial responses. It detects:
1. **Intent** — what metric the user wants (revenue, net income, assets, etc.)
2. **Entity** — which company (Microsoft, Tesla, Apple)

Based on these two factors, it fetches the relevant data and returns a formatted, human-readable response.

---

## Predefined Queries (7 supported)

| # | Query Pattern | Description |
|---|--------------|-------------|
| 1 | "What is the total revenue?" | Revenue for all or specific company |
| 2 | "How has net income changed?" | Net income + profit margin |
| 3 | "What are the total assets?" | Assets, liabilities, equity |
| 4 | "What is the operating cash flow?" | OCF with YoY change |
| 5 | "Give me a financial health summary of [company]" | Full metrics summary |
| 6 | "Compare all companies" | Side-by-side comparison table |
| 7 | "help" | Lists all available queries |

**Available Companies:** Microsoft, Tesla, Apple  
**Data Coverage:** FY2023, FY2024, FY2025 (from 10-K filings)

---

## Files Included

| File | Description |
|------|-------------|
| `chatbot.py` | Main chatbot script |
| `test_chatbot.py` | Test suite (12 test cases) |
| `test_results.txt` | Output of all test runs |
| `documentation.md` | This file |

---

## How to Run

```bash
# Run the chatbot interactively
python chatbot.py

# Run tests
python test_chatbot.py
```

---

## Sample Interaction

```
You: What is Microsoft's total revenue?
Chatbot: Microsoft's total revenue in FY2025 was $281,724 million.
         This increased by 14.9% compared to FY2024 ($245,122 million).

You: Give me a financial health summary of Tesla
Chatbot: === Tesla Financial Health Summary (FY2025) ===
  Revenue:           $94,827 million
  Net Income:        $3,855 million
  Profit Margin:     4.1%
  Total Assets:      $137,806 million
  Debt/Asset Ratio:  39.9%
  Operating CF:      $14,747 million
  2-Year Rev Growth: -2.0%
  2-Year NI Growth:  -74.3%
```

---

## Limitations

1. **Rule-based only** — Cannot understand paraphrased or complex natural language queries
2. **Predefined queries** — Only responds to specific query patterns listed above
3. **Static data** — Data is hardcoded from 10-K filings; not connected to live financial APIs
4. **No memory** — Does not retain context between queries (stateless)
5. **Text-only** — No visual charts or graphs (future enhancement)
6. **Three companies only** — Limited to Microsoft, Tesla, and Apple

---

## Future Enhancements
- NLP integration for natural language understanding
- Real-time data via SEC EDGAR API
- Flask web interface for browser-based interaction
- Machine learning for improved query matching
- Data visualization (charts, graphs)
- Multi-turn conversation with context memory

---

## Data Sources
- **Microsoft**: https://www.microsoft.com/investor/reports/ar25/index.html
- **Tesla**: https://stocklight.com/stocks/us/nasdaq-tsla/tesla/annual-reports/nasdaq-tsla-2026-10K-26574326.pdf
- **Apple**: https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm

---
*BCG GenAI Consulting Team | GFC AI Chatbot Project*
