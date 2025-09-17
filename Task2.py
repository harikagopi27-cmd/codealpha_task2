prices = {"AAPL":190,"TSLA":250,"GOOG":2800,"MSFT":320,"AMZN":135}
portfolio,total = {},0
print("Available stocks:",".join(prices.keys())")
while True:
    stock = input("\nEnter stock (or 'done'): ").upper()
    if stock == "DONE":break
    if stock not in prices:
      print("Invalid stock");continue
    qty = int(input("Enter quantity:"))
    portfolio[stock] = portfolio.get(stock,0) + qty
    total += prices[stock] * qty
    print("\nPortfolio Summary:")
    for s,q in portfolio.items():
       print(f"{s}:{q} shares (${prices[s]*q})")
       print(f"\n Total Investment: ${total}")