import requests
from bs4 import BeautifulSoup
import pandas as pd

def balancesheet(ticker):
    current_year = 2024
    url = 'https://stockanalysis.com/stocks/' + str(ticker) + '/financials/balance-sheet/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    financial_data = []

    if soup.title.text != '404 Not Found':
        financial_table = soup.find("table", class_="w-full border-separate border-spacing-0 whitespace-nowrap")
        if financial_table:
            rows = financial_table.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                if cells and len(cells) > 1:
                    title = cells[0].get_text(strip=True)
                    for i in range(1, len(cells)):
                        year_cell = current_year - i
                        financials_cell = cells[i].get_text(strip=True)
                        financial_data.append((title, year_cell, financials_cell))

    df = pd.DataFrame(financial_data, columns=['Balance Sheet', 'Year', 'Financials'])
    df['Balance Sheet'] = pd.Categorical(df['Balance Sheet'], categories=pd.unique(df['Balance Sheet']), ordered=True)
    pivot_df = df.pivot(index='Balance Sheet', columns='Year', values='Financials')
    pivot_df = pivot_df.drop(columns=[col for col in pivot_df.columns if 'Upgrade' in pivot_df[col].unique()])

    return pivot_df

def incomestatement(ticker):
    current_year = 2024
    url = 'https://stockanalysis.com/stocks/'+str(ticker)+'/financials/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Initialize a list to hold all financial data
    financial_data = []

    if soup.title.text != '404 Not Found':
        # Find the table containing financial data
        financial_table = soup.find("table", class_="w-full border-separate border-spacing-0 whitespace-nowrap")

        if financial_table:
            # Find all rows (tr elements) in the table
            rows = financial_table.find_all("tr")

            for row in rows:
                cells = row.find_all("td")
                if cells and len(cells) > 1:  # Ensure there are enough cells for year and revenue
                    title = cells[0].get_text(strip=True)
                    for i in range(1, len(cells)):  
                        year_cell = current_year - i
                        financials_cell = cells[i].get_text(strip=True)
                        financial_data.append((title, year_cell, financials_cell))

    # Convert the list of tuples into a pandas DataFrame
    df = pd.DataFrame(financial_data, columns=['Income Statement', 'Year', 'Financials'])

    # To maintain the order of data as entered, set 'Title' as a categorical variable with its own order
    df['Income Statement'] = pd.Categorical(df['Income Statement'], categories=pd.unique(df['Income Statement']), ordered=True)

    # Pivot the DataFrame to get the desired format
    pivot_df = df.pivot(index='Income Statement', columns='Year', values='Financials')

    # Check if any column contains 'Upgrade' and remove it
    pivot_df = pivot_df.drop(columns=[col for col in pivot_df.columns if 'Upgrade' in pivot_df[col].unique()])

    

    # Display the pivoted DataFrame
    return pivot_df
    #only display current year
    #return print(pivot_df[[2023]])


def cashflow(ticker):
    current_year = 2024
    url = 'https://stockanalysis.com/stocks/' + str(ticker) + '/financials/cash-flow-statement/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    financial_data = []

    if soup.title.text != '404 Not Found':
        financial_table = soup.find("table", class_="w-full border-separate border-spacing-0 whitespace-nowrap")
        if financial_table:
            rows = financial_table.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                if cells and len(cells) > 1:
                    title = cells[0].get_text(strip=True)
                    for i in range(1, len(cells)):
                        year_cell = current_year - i
                        financials_cell = cells[i].get_text(strip=True)
                        financial_data.append((title, year_cell, financials_cell))

    df = pd.DataFrame(financial_data, columns=['Cash Flow', 'Year', 'Financials'])
    df['Cash Flow'] = pd.Categorical(df['Cash Flow'], categories=pd.unique(df['Cash Flow']), ordered=True)
    pivot_df = df.pivot(index='Cash Flow', columns='Year', values='Financials')
    pivot_df = pivot_df.drop(columns=[col for col in pivot_df.columns if 'Upgrade' in pivot_df[col].unique()])

    return pivot_df


def ratios(ticker):
    current_year = 2024
    url = 'https://stockanalysis.com/stocks/' + str(ticker) + '/financials/ratios/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    financial_data = []

    if soup.title.text != '404 Not Found':
        financial_table = soup.find("table", class_="w-full border-separate border-spacing-0 whitespace-nowrap")
        if financial_table:
            rows = financial_table.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                if cells and len(cells) > 1:
                    title = cells[0].get_text(strip=True)
                    for i in range(1, len(cells)):
                        year_cell = current_year - i
                        financials_cell = cells[i].get_text(strip=True)
                        financial_data.append((title, year_cell, financials_cell))

    df = pd.DataFrame(financial_data, columns=['Ratios', 'Year', 'Financials'])
    df['Ratios'] = pd.Categorical(df['Ratios'], categories=pd.unique(df['Ratios']), ordered=True)
    pivot_df = df.pivot(index='Ratios', columns='Year', values='Financials')
    pivot_df = pivot_df.drop(columns=[col for col in pivot_df.columns if 'Upgrade' in pivot_df[col].unique()])

    return pivot_df

#Enter company ticker to display the DataFrame
def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    company = input('Enter ticker: ')
    print("")
    print(balancesheet(company),"\n")
    print(incomestatement(company),"\n")
    print(cashflow(company),"\n")
    print(ratios(company),"\n")
    #only display current year
    #print(incomestatement(company)[[2023]])

if __name__ == '__main__':
    main()

