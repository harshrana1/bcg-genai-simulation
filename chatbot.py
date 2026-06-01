"""
BCG GenAI Consulting – GFC AI-Powered Financial Chatbot
Task 2: Rule-Based Chatbot Prototype
Analyst: Harsh | Manager: Aisha
"""

import pandas as pd

# ── Financial Data (from Task 1 10-K Analysis) ──────────────────────────
financial_data = {
    "Microsoft": {
        2023: {"revenue": 211915, "net_income": 72361, "total_assets": 411976,
               "total_liabilities": 205753, "operating_cash_flow": 87582},
        2024: {"revenue": 245122, "net_income": 88136, "total_assets": 512163,
               "total_liabilities": 243686, "operating_cash_flow": 118548},
        2025: {"revenue": 281724, "net_income": 101832, "total_assets": 619003,
               "total_liabilities": 275524, "operating_cash_flow": 136162},
    },
    "Tesla": {
        2023: {"revenue": 96773,  "net_income": 14974, "total_assets": 106618,
               "total_liabilities": 43009, "operating_cash_flow": 13256},
        2024: {"revenue": 97690,  "net_income": 7153,  "total_assets": 122070,
               "total_liabilities": 48390, "operating_cash_flow": 14923},
        2025: {"revenue": 94827,  "net_income": 3855,  "total_assets": 137806,
               "total_liabilities": 54941, "operating_cash_flow": 14747},
    },
    "Apple": {
        2023: {"revenue": 383285, "net_income": 96995, "total_assets": 352583,
               "total_liabilities": 290437, "operating_cash_flow": 110543},
        2024: {"revenue": 391035, "net_income": 93736, "total_assets": 364980,
               "total_liabilities": 308030, "operating_cash_flow": 118254},
        2025: {"revenue": 416161, "net_income": 112010, "total_assets": 359241,
               "total_liabilities": 285508, "operating_cash_flow": 111482},
    },
}

COMPANIES = list(financial_data.keys())
LATEST_YEAR = 2025


# ── Helper Functions ─────────────────────────────────────────────────────
def get_company_from_query(query):
    """Detect which company the user is asking about."""
    query_lower = query.lower()
    for company in COMPANIES:
        if company.lower() in query_lower:
            return company
    return None


def format_usd(amount):
    """Format number as USD millions string."""
    return f"${amount:,.0f} million"


def pct_change(old, new):
    """Calculate percentage change."""
    return ((new - old) / old) * 100


# ── Core Chatbot Logic ───────────────────────────────────────────────────
def simple_chatbot(user_query):
    """
    Rule-based financial chatbot.
    Matches user queries to predefined financial responses.
    """
    query = user_query.strip().lower()
    company = get_company_from_query(query)

    # ── Query 1: Total Revenue ───────────────────────────────────────────
    if "total revenue" in query or "revenue" in query:
        if company:
            rev = financial_data[company][LATEST_YEAR]["revenue"]
            rev_prev = financial_data[company][LATEST_YEAR - 1]["revenue"]
            change = pct_change(rev_prev, rev)
            direction = "increased" if change > 0 else "decreased"
            return (f"{company}'s total revenue in FY{LATEST_YEAR} was {format_usd(rev)}. "
                    f"This {direction} by {abs(change):.1f}% compared to FY{LATEST_YEAR-1} "
                    f"({format_usd(rev_prev)}).")
        else:
            # Show all companies
            response = f"Total Revenue for FY{LATEST_YEAR}:\n"
            for c in COMPANIES:
                response += f"  • {c}: {format_usd(financial_data[c][LATEST_YEAR]['revenue'])}\n"
            return response.strip()

    # ── Query 2: Net Income ──────────────────────────────────────────────
    elif "net income" in query or "profit" in query:
        if company:
            ni = financial_data[company][LATEST_YEAR]["net_income"]
            ni_prev = financial_data[company][LATEST_YEAR - 1]["net_income"]
            change = pct_change(ni_prev, ni)
            direction = "increased" if change > 0 else "decreased"
            margin = (ni / financial_data[company][LATEST_YEAR]["revenue"]) * 100
            return (f"{company}'s net income in FY{LATEST_YEAR} was {format_usd(ni)} "
                    f"(profit margin: {margin:.1f}%). "
                    f"Net income {direction} by {abs(change):.1f}% vs FY{LATEST_YEAR-1} "
                    f"({format_usd(ni_prev)}).")
        else:
            response = f"Net Income for FY{LATEST_YEAR}:\n"
            for c in COMPANIES:
                ni = financial_data[c][LATEST_YEAR]["net_income"]
                margin = (ni / financial_data[c][LATEST_YEAR]["revenue"]) * 100
                response += f"  • {c}: {format_usd(ni)} (margin: {margin:.1f}%)\n"
            return response.strip()

    # ── Query 3: Total Assets ────────────────────────────────────────────
    elif "total assets" in query or "assets" in query:
        if company:
            assets = financial_data[company][LATEST_YEAR]["total_assets"]
            liab = financial_data[company][LATEST_YEAR]["total_liabilities"]
            equity = assets - liab
            ratio = (liab / assets) * 100
            return (f"{company}'s total assets in FY{LATEST_YEAR}: {format_usd(assets)}. "
                    f"Total liabilities: {format_usd(liab)} ({ratio:.1f}% of assets). "
                    f"Shareholders' equity: {format_usd(equity)}.")
        else:
            response = f"Total Assets for FY{LATEST_YEAR}:\n"
            for c in COMPANIES:
                response += f"  • {c}: {format_usd(financial_data[c][LATEST_YEAR]['total_assets'])}\n"
            return response.strip()

    # ── Query 4: Operating Cash Flow ─────────────────────────────────────
    elif "cash flow" in query or "operating cash" in query:
        if company:
            ocf = financial_data[company][LATEST_YEAR]["operating_cash_flow"]
            ocf_prev = financial_data[company][LATEST_YEAR - 1]["operating_cash_flow"]
            change = pct_change(ocf_prev, ocf)
            direction = "increased" if change > 0 else "decreased"
            return (f"{company}'s cash flow from operations in FY{LATEST_YEAR} was "
                    f"{format_usd(ocf)}. This {direction} by {abs(change):.1f}% "
                    f"from FY{LATEST_YEAR-1} ({format_usd(ocf_prev)}).")
        else:
            response = f"Operating Cash Flow for FY{LATEST_YEAR}:\n"
            for c in COMPANIES:
                response += f"  • {c}: {format_usd(financial_data[c][LATEST_YEAR]['operating_cash_flow'])}\n"
            return response.strip()

    # ── Query 5: Financial Health / Summary ──────────────────────────────
    elif "financial health" in query or "summary" in query or "overview" in query:
        if company:
            d = financial_data[company][LATEST_YEAR]
            margin = (d["net_income"] / d["revenue"]) * 100
            debt_ratio = (d["total_liabilities"] / d["total_assets"]) * 100
            rev_growth = pct_change(
                financial_data[company][2023]["revenue"], d["revenue"])
            ni_growth = pct_change(
                financial_data[company][2023]["net_income"], d["net_income"])
            return (f"=== {company} Financial Health Summary (FY{LATEST_YEAR}) ===\n"
                    f"  Revenue:            {format_usd(d['revenue'])}\n"
                    f"  Net Income:         {format_usd(d['net_income'])}\n"
                    f"  Profit Margin:      {margin:.1f}%\n"
                    f"  Total Assets:       {format_usd(d['total_assets'])}\n"
                    f"  Debt/Asset Ratio:   {debt_ratio:.1f}%\n"
                    f"  Operating CF:       {format_usd(d['operating_cash_flow'])}\n"
                    f"  2-Year Rev Growth:  {rev_growth:+.1f}%\n"
                    f"  2-Year NI Growth:   {ni_growth:+.1f}%")
        else:
            response = f"=== Financial Health Summary FY{LATEST_YEAR} ===\n"
            for c in COMPANIES:
                d = financial_data[c][LATEST_YEAR]
                margin = (d["net_income"] / d["revenue"]) * 100
                response += f"\n{c}:\n"
                response += f"  Revenue: {format_usd(d['revenue'])} | "
                response += f"Net Income: {format_usd(d['net_income'])} | "
                response += f"Margin: {margin:.1f}%\n"
            return response.strip()

    # ── Query 6: Compare Companies ───────────────────────────────────────
    elif "compare" in query or "best" in query or "highest" in query:
        response = f"=== Company Comparison FY{LATEST_YEAR} ===\n"
        response += f"\n{'Company':<12} {'Revenue':>18} {'Net Income':>15} {'Margin':>10} {'OCF':>18}\n"
        response += "-" * 75 + "\n"
        for c in COMPANIES:
            d = financial_data[c][LATEST_YEAR]
            margin = (d["net_income"] / d["revenue"]) * 100
            response += (f"{c:<12} {format_usd(d['revenue']):>18} "
                         f"{format_usd(d['net_income']):>15} "
                         f"{margin:>9.1f}% "
                         f"{format_usd(d['operating_cash_flow']):>18}\n")
        response += "\n💡 Microsoft leads in growth, Apple in revenue & OCF, Tesla faces margin pressure."
        return response

    # ── Query 7: Help / Available queries ────────────────────────────────
    elif "help" in query or "what can you" in query or "queries" in query:
        return """I can answer the following financial queries:
  1. "What is the total revenue?" (add company name for specific data)
  2. "How has net income changed?" (add company name for specific data)
  3. "What are the total assets?" (add company name for specific data)
  4. "What is the operating cash flow?" (add company name for specific data)
  5. "Give me a financial health summary of [company]"
  6. "Compare all companies"

Available companies: Microsoft, Tesla, Apple
Example: "What is Microsoft's total revenue?" """

    # ── Default: Unrecognized query ───────────────────────────────────────
    else:
        return ("Sorry, I can only provide information on predefined financial queries. "
                "Type 'help' to see what I can answer.")


# ── Main Loop ────────────────────────────────────────────────────────────
def main():
    print("=" * 60)
    print("  BCG GenAI – GFC Financial Chatbot (Task 2 Prototype)")
    print("  Companies: Microsoft | Tesla | Apple (FY2023-2025)")
    print("  Type 'help' for available queries | 'exit' to quit")
    print("=" * 60)

    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit", "bye"):
            print("Chatbot: Goodbye! Thank you for using GFC Financial Chatbot.")
            break
        response = simple_chatbot(user_input)
        print(f"\nChatbot: {response}")


if __name__ == "__main__":
    main()
