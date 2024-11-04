# Market Analysis Application

This is a web application for financial market analysis, built with Flask. It allows users to gather and analyze market data for a specified company using SERP API for market information, Yahoo Finance API for financial data, and Google Generative AI to generate summaries.

## Project Structure

```plaintext
market_analysis_app/
├── app.py                      # Main Flask application script
├── requirements.txt            # Dependencies for the project
├── templates/
│   ├── index.html              # HTML template for the home page
│   └── result.html             # HTML template for the results page
├── static/
│   ├── css/
│   │   └── styles.css          # Optional external CSS for styling
│   └── images/
│       ├── logo.svg            # Logo image displayed in the header
│       └── crypto-analysis.png # Image shown on the home page
└── README.md                   # Project documentation (this file)
```
### Functionality Provided

1. **Company Market Analysis**:
   - **Input**: Users enter a company name and ticker symbol.
   - **Output**: The app provides a market analysis summary, using data gathered from SERP API and Yahoo Finance.

2. **Market Data Gathering**:
   - Uses **SERP API** to perform a Google search on the company name to gather relevant articles or market information.

3. **Financial Data Retrieval**:
   - Uses **Yahoo Finance (yfinance)** to retrieve historical data, income statements, balance sheets, and cash flow statements for the specified ticker symbol.

4. **AI-Based Market Summary Generation**:
   - Uses **Google Generative AI API** to analyze the gathered data and generate a financial summary based on historical and current data.
  
## APIs Used

- **SERP API**: Provides Google search results for market analysis.
- **Yahoo Finance API**: Accessed via the `yfinance` package to fetch financial data.
- **Google Generative AI API**: Utilized to generate a market summary based on financial and market data.

## Installation Requirements

1. Ensure you have Python installed.

2. Clone or download the project repository.

3. Install the necessary libraries by creating a `requirements.txt` file with the following contents:

   ```plaintext
   Flask==2.1.1
   yfinance==0.2.10
   serpapi==2.0.0
   google-generativeai
   ```
4. Install these dependencies with the following command:
   ```bash
   pip install -r requirements.txt
   ```
## Setting Up API Keys
1. Create a ```.env ```file in the project root directory.
2. Add your API keys to this file:
```
GOOGLE_API_KEY="your_google_api_key"
SERPER_API_KEY="your_serper_api_key"
```
3. In ```app.py```, make sure to import and load these environment variables:
```
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
```
##Running the Project
1. Start the Flask Application:
   ```
   python app.py
   ```
2. The application will be available at ```http://127.0.0.1:5000``` by default.
3. Use the Application:
     1. Open your browser and go to ```http://127.0.0.1:5000```.
     2. Enter the company name and ticker symbol in the input form.
     3. Submit the form to receive a generated market analysis summary.
## Video demo
  [Watch Video](https://drive.google.com/file/d/1BwiqEAd27ylaIJZTOoiVaTB-DcccJbpL/view?usp=sharing)

   

