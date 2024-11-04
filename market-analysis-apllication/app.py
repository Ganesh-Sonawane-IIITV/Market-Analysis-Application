from flask import Flask, render_template, request
from serpapi import GoogleSearch
import yfinance as yf
import google.generativeai as genai

app = Flask(__name__)

# Set up API keys
GOOGLE_API_KEY = "AIzaSyC7UYmLOYWoycis970Gy6NSVluYbxszGDI"
SERPER_API_KEY = "bcb14438f8f0bee6c9d37affdd37c6cd88d35b5d68d09f68974b93a46af05538"

# Configure the GenAI API
genai.configure(api_key=GOOGLE_API_KEY)

def gather_market_data(company_name):
    search_params = {
        "q": f"{company_name} market analysis",
        "location": "United States",
        "api_key": SERPER_API_KEY,
    }
    search = GoogleSearch(search_params)
    results = search.get_dict()
    return results['organic_results'] if 'organic_results' in results else []

def fetch_financial_data(ticker):
    ticker_data = yf.Ticker(ticker)
    hist_data = ticker_data.history(period="2y")
    income_statement = ticker_data.financials
    balance_sheet = ticker_data.balance_sheet
    cash_flow = ticker_data.cashflow
    return hist_data, income_statement, balance_sheet, cash_flow

def generate_market_analysis_summary(market_data, hist_data, income_statement, balance_sheet, cash_flow):
    financial_data_summary = (
        f"Historical Data:\n{hist_data.head()}\n\n"
        f"Income Statement:\n{income_statement.head()}\n\n"
        f"Balance Sheet:\n{balance_sheet.head()}\n\n"
        f"Cash Flow Statement:\n{cash_flow.head()}"
    )
    role = "Financial Analyst"
    goal = "Analyze financial performance and metrics"
    backstory = "Expert financial analyst specializing in company valuation, financial modeling, and performance metrics."
    prompt = f"""{role}:
    Goal: {goal}
    Backstory: {backstory}
    
    Based on the following data, provide a market analysis summary:
    {market_data}\n
    {financial_data_summary}
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        company_name = request.form.get('company_name')
        ticker = request.form.get('ticker')

        # Gather market data and fetch financial data
        market_data = gather_market_data(company_name)
        hist_data, income_statement, balance_sheet, cash_flow = fetch_financial_data(ticker)

        # Generate market analysis summary
        market_analysis_summary = generate_market_analysis_summary(market_data, hist_data, income_statement, balance_sheet, cash_flow)

        return render_template('results.html', summary=market_analysis_summary)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
