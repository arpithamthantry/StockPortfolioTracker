# Stock Portfolio Tracker

A Python-based console application for managing and analyzing a stock portfolio using predefined stock prices.

## Features

- Add stocks to a portfolio
- Update existing stock quantities
- Remove stocks from the portfolio
- View complete portfolio details
- Search for individual stocks
- Calculate total investment value
- Calculate portfolio allocation percentages
- Identify the largest portfolio holding
- Calculate average investment per stock
- Save portfolio data to a CSV file
- Load saved portfolio data from a CSV file
- Input validation and error handling
- Menu-driven user-friendly interface

## Technologies Used

- Python 3
- Dictionaries
- Functions
- Loops and conditional statements
- CSV file handling
- File handling
- Exception handling

## Available Stocks

The application uses predefined sample stock prices:

| Stock | Sample Price |
|-------|-------------:|
| AAPL | $180.00 |
| TSLA | $250.00 |
| MSFT | $420.00 |
| GOOGL | $175.00 |
| AMZN | $190.00 |
| NVDA | $130.00 |
| META | $500.00 |
| NFLX | $700.00 |
| ORCL | $160.00 |
| ADBE | $380.00 |

> Note: The prices are hardcoded sample values as required by the CodeAlpha task. They are not live market prices and the application does not provide financial advice.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Clone or download this repository.
3. Open the project folder in a terminal.
4. Run:

    python portfolio_tracker.py

## How to Use

1. Start the application.
2. Select an option from the main menu.
3. Choose a stock from the available stock list.
4. Enter the quantity of shares.
5. The application calculates the value of the holding.
6. Add, update, remove, or search for stocks as required.
7. View portfolio insights and allocation percentages.
8. Save the portfolio to a CSV file.
9. Load the saved portfolio whenever needed.
10. Exit the application when finished.

## Portfolio Insights

The application provides useful portfolio statistics, including:

- Total investment
- Number of different stocks
- Total shares held
- Average value per stock
- Largest portfolio holding
- Portfolio allocation percentage for each stock

## Data Storage

Portfolio information can be saved to a CSV file using the built-in save option.

The saved file contains:

- Stock symbol
- Quantity
- Stock price
- Total holding value

The saved portfolio can later be loaded back into the application.

## Example

Suppose the portfolio contains:

- 10 AAPL shares
- 3 TSLA shares

The application calculates:

- AAPL value = $1,800.00
- TSLA value = $750.00
- Total investment = $2,550.00

It can also calculate the percentage allocation of each holding and identify the largest holding.

## Project Highlights

This project goes beyond the basic stock investment calculation by providing a complete portfolio management experience through a menu-driven interface.

It demonstrates practical use of:

- Python data structures
- Modular programming
- Input validation
- Arithmetic calculations
- File persistence
- CSV processing
- Error handling
- User interaction

**Task:** Stock Portfolio Tracker

## Author

**Arpitha M Thantry**
