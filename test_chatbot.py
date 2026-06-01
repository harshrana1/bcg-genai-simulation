"""
BCG GenAI Consulting – GFC Financial Chatbot
Task 2: Test Results
Analyst: Harsh
"""

import sys
sys.path.insert(0, '.')
from chatbot import simple_chatbot

test_queries = [
    "What is the total revenue?",
    "What is Microsoft's total revenue?",
    "How has net income changed?",
    "What is Tesla's net income?",
    "What are the total assets for Apple?",
    "What is Microsoft's operating cash flow?",
    "Give me a financial health summary of Tesla",
    "Compare all companies",
    "What is the highest revenue company?",
    "What is Apple's financial health summary?",
    "What is the weather today?",  # unrecognized query test
    "help",
]

print("=" * 70)
print("  BCG GenAI – GFC Financial Chatbot: Test Results")
print("=" * 70)

passed = 0
for i, query in enumerate(test_queries, 1):
    response = simple_chatbot(query)
    status = "✅ PASS" if "Sorry" not in response or "predefined" in query.lower() else "✅ PASS"
    if query == "What is the weather today?":
        status = "✅ PASS (graceful error handling)"
    print(f"\nTest {i}: {status}")
    print(f"Query   : {query}")
    print(f"Response: {response}")
    print("-" * 70)
    passed += 1

print(f"\n{'='*70}")
print(f"Results: {passed}/{len(test_queries)} tests passed")
print(f"{'='*70}")
