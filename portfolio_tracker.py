import csv
import os
STOCK_PRICES={"AAPL": 180.00,"TSLA": 250.00,"MSFT": 420.00,"GOOGL": 175.00,"AMZN": 190.00,"NVDA": 130.00,"META": 500.00,"NFLX": 700.00,"ORCL": 160.00,"ADBE": 380.00}
CSV_FILE="portfolio.csv"
def display_header(title):
    """Display a consistent section header."""
    print("\n"+"="*65)
    print(title.center(65))
    print("="*65)
def display_available_stocks():
    """Display all stocks available in the hardcoded database."""
    display_header("AVAILABLE STOCKS")
    for symbol,price in STOCK_PRICES.items():
        print(f"{symbol:<10} ${price:>10.2f}")
    print("="*65)
def get_positive_integer(prompt):
    """Get a positive whole number from the user."""
    while True:
        try:
            value=int(input(prompt).strip())
            if value<=0:
                print("Please enter a quantity greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")
def get_stock_symbol():
    """Get and validate a stock symbol."""
    while True:
        symbol=input("Enter stock symbol: ").strip().upper()
        if symbol in STOCK_PRICES:
            return symbol
        print("Stock not found in the database.")
        print("Please choose a stock from the available list.")
def calculate_stock_value(symbol,quantity):
    """Calculate the total value of one stock holding."""
    return STOCK_PRICES[symbol]*quantity
def calculate_total_investment(portfolio):
    """Calculate the total investment across all holdings."""
    total=0
    for symbol,quantity in portfolio.items():
        total+=calculate_stock_value(symbol,quantity)
    return total
def calculate_allocation(portfolio,symbol):
    """Calculate the percentage allocation of one stock."""
    total=calculate_total_investment(portfolio)
    if total==0:
        return 0
    stock_value=calculate_stock_value(symbol,portfolio[symbol])
    return (stock_value/total)*100
def add_stock(portfolio):
    """Add a stock or increase an existing holding."""
    display_available_stocks()
    symbol=get_stock_symbol()
    quantity=get_positive_integer("Enter quantity: ")
    if symbol in portfolio:
        portfolio[symbol]+=quantity
        print(
            f"\nUpdated {symbol}: "
            f"{portfolio[symbol]} shares"
        )
    else:
        portfolio[symbol]=quantity
        print(
            f"\nAdded {quantity} shares of {symbol} "
            f"to your portfolio."
        )
    value=calculate_stock_value(symbol,portfolio[symbol])
    print(f"Current value of {symbol}: ${value:,.2f}")
def update_stock(portfolio):
    """Replace the quantity of an existing stock."""
    if not portfolio:
        print("\nYour portfolio is currently empty.")
        return
    display_portfolio(portfolio)
    symbol=input("\nEnter the stock symbol you want to update: ").strip().upper()
    if symbol not in portfolio:
        print("That stock is not currently in your portfolio.")
        return
    quantity=get_positive_integer(f"Enter new quantity for {symbol}: ")
    portfolio[symbol]=quantity
    print(
        f"\n{symbol} has been updated to "
        f"{quantity} shares."
    )
def remove_stock(portfolio):
    """Remove a stock completely from the portfolio."""
    if not portfolio:
        print("\nYour portfolio is currently empty.")
        return
    display_portfolio(portfolio)
    symbol=input("\nEnter the stock symbol you want to remove: ").strip().upper()
    if symbol not in portfolio:
        print("That stock is not in your portfolio.")
        return
    del portfolio[symbol]
    print(f"\n{symbol} has been removed from your portfolio.")
def display_portfolio(portfolio):
    """Display a detailed portfolio dashboard."""
    display_header("PORTFOLIO DASHBOARD")
    if not portfolio:
        print("Your portfolio is empty.")
        print("Add some stocks to see your portfolio.")
        print("="*65)
        return
    print(
        f"{'Stock':<10}"
        f"{'Quantity':>10}"
        f"{'Price':>15}"
        f"{'Value':>15}"
    )
    print("-"*65)
    for symbol,quantity in portfolio.items():
        price=STOCK_PRICES[symbol]
        value=calculate_stock_value(symbol,quantity)
        print(
            f"{symbol:<10}"
            f"{quantity:>10}"
            f"${price:>14,.2f}"
            f"${value:>14,.2f}"
        )
    print("-"*65)
    total=calculate_total_investment(portfolio)
    print(f"{'TOTAL INVESTMENT':<35}${total:>14,.2f}")
    print("="*65)
def display_insights(portfolio):
    """Display useful statistics about the portfolio."""
    display_header("PORTFOLIO INSIGHTS")
    if not portfolio:
        print("No portfolio data available.")
        print("="*65)
        return
    total=calculate_total_investment(portfolio)
    number_of_stocks=len(portfolio)
    total_shares=sum(portfolio.values())
    average_value=total/number_of_stocks
    largest_symbol=max(portfolio,key=lambda symbol:calculate_stock_value(symbol,portfolio[symbol]))
    largest_value=calculate_stock_value(largest_symbol,portfolio[largest_symbol])
    print(f"Number of different stocks : {number_of_stocks}")
    print(f"Total shares held          : {total_shares}")
    print(f"Total investment           : ${total:,.2f}")
    print(f"Average value per stock    : ${average_value:,.2f}")
    print(
        f"Largest holding            : "
        f"{largest_symbol} (${largest_value:,.2f})"
    )
    print("\nPortfolio Allocation")
    print("-"*65)
    for symbol,quantity in portfolio.items():
        percentage=calculate_allocation(portfolio,symbol)
        print(
            f"{symbol:<10} "
            f"{percentage:>6.2f}%"
        )
    print("="*65)
def search_stock(portfolio):
    """Show details about one stock."""
    display_header("STOCK LOOKUP")
    symbol=input("Enter stock symbol to search: ").strip().upper()
    if symbol not in STOCK_PRICES:
        print("Stock not found in the database.")
        return
    price=STOCK_PRICES[symbol]
    print(f"\nStock: {symbol}")
    print(f"Price: ${price:,.2f}")
    if symbol in portfolio:
        quantity=portfolio[symbol]
        value=calculate_stock_value(symbol, quantity)
        allocation=calculate_allocation(portfolio,symbol)
        print(f"Quantity owned: {quantity}")
        print(f"Portfolio value: ${value:,.2f}")
        print(f"Portfolio allocation: {allocation:.2f}%")
    else:
        print("You do not currently own this stock.")
def save_portfolio(portfolio):
    """Save portfolio data to a CSV file."""
    if not portfolio:
        print("\nThere is no portfolio data to save.")
        return
    try:
        with open(CSV_FILE,"w",newline="",encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerow(["Stock Symbol","Quantity","Price","Total Value"])
            for symbol, quantity in portfolio.items():
                price=STOCK_PRICES[symbol]
                value=calculate_stock_value(symbol,quantity)
                writer.writerow([symbol,quantity,f"{price:.2f}",f"{value:.2f}"])
        print(
            f"\nPortfolio successfully saved to "
            f"'{CSV_FILE}'."
        )
    except OSError as error:
        print(f"Unable to save portfolio: {error}")
def load_portfolio():
    """Load portfolio data from the CSV file."""
    portfolio={}
    if not os.path.exists(CSV_FILE):
        print(
            "\nNo saved portfolio found."
        )
        return portfolio
    try:
        with open(
            CSV_FILE,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:
            reader=csv.DictReader(file)
            for row in reader:
                symbol=row["Stock Symbol"].strip().upper()
                quantity=int(row["Quantity"])
                if symbol in STOCK_PRICES and quantity>0:
                    portfolio[symbol]=quantity
        print(
            f"\nPortfolio loaded successfully "
            f"from '{CSV_FILE}'."
        )
    except (OSError, ValueError, KeyError) as error:
        print(f"Unable to load portfolio: {error}")
    return portfolio
def display_menu():
    """Display the main menu."""
    print("\n"+"="*65)
    print("STOCK PORTFOLIO TRACKER".center(65))
    print("="*65)
    print("1. View Portfolio")
    print("2. Add Stock")
    print("3. Update Stock")
    print("4. Remove Stock")
    print("5. Search Stock")
    print("6. Portfolio Insights")
    print("7. View Available Stocks")
    print("8. Save Portfolio to CSV")
    print("9. Load Portfolio from CSV")
    print("10. Exit")
    print("="*65)
def main():
    """Run the Stock Portfolio Tracker."""
    portfolio={}
    display_header("WELCOME TO STOCK PORTFOLIO TRACKER")
    print("Build and manage your investment portfolio.")
    print("Prices are predefined sample values for this project.")
    print("No live market data or financial advice is provided.")
    while True:
        display_menu()
        choice=input("Enter your choice (1-10): ").strip()
        if choice=="1":
            display_portfolio(portfolio)
        elif choice=="2":
            add_stock(portfolio)
        elif choice=="3":
            update_stock(portfolio)
        elif choice=="4":
            remove_stock(portfolio)
        elif choice=="5":
            search_stock(portfolio)
        elif choice=="6":
            display_insights(portfolio)
        elif choice=="7":
            display_available_stocks()
        elif choice=="8":
            save_portfolio(portfolio)
        elif choice=="9":
            loaded_portfolio=load_portfolio()
            if loaded_portfolio:
                portfolio=loaded_portfolio
        elif choice=="10":
            print("\nThank you for using Stock Portfolio Tracker!")
            print("Goodbye! 👋")
            break
        else:
            print(
                "\nInvalid choice. "
                "Please select an option from 1 to 10.")
if __name__=="__main__":
    main()