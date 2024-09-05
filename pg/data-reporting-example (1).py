import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import StringIO

def fetch_data_from_api(url):
    """Fetch data from an API and return as a pandas DataFrame."""
    response = requests.get(url)
    response.raise_for_status()
    return pd.read_csv(StringIO(response.text))

def process_data(df):
    """Process the data: clean, filter, and calculate summary statistics."""
    # Remove rows with missing values
    df = df.dropna()
    
    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Filter data for the last 12 months
    last_year = df['date'].max() - pd.DateOffset(months=12)
    df = df[df['date'] > last_year]
    
    # Calculate monthly average sales
    monthly_sales = df.groupby(df['date'].dt.to_period("M"))['sales'].mean().reset_index()
    monthly_sales['date'] = monthly_sales['date'].dt.to_timestamp()
    
    return monthly_sales

def generate_report(data):
    """Generate a report with visualizations and summary statistics."""
    # Create a line plot of monthly sales
    plt.figure(figsize=(12, 6))
    plt.plot(data['date'], data['sales'])
    plt.title('Monthly Average Sales - Last 12 Months')
    plt.xlabel('Date')
    plt.ylabel('Average Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('monthly_sales.png')
    plt.close()

    # Calculate summary statistics
    total_sales = data['sales'].sum()
    avg_sales = data['sales'].mean()
    max_sales = data['sales'].max()
    min_sales = data['sales'].min()

    # Prepare report text
    report = f"""
    Sales Report Summary:
    ---------------------
    Total Sales: ${total_sales:.2f}
    Average Monthly Sales: ${avg_sales:.2f}
    Highest Monthly Sales: ${max_sales:.2f}
    Lowest Monthly Sales: ${min_sales:.2f}
    
    The monthly sales chart has been saved as 'monthly_sales.png'.
    """

    return report

def main():
    # API endpoint (replace with actual API URL)
    api_url = "https://api.example.com/sales_data"

    try:
        # Fetch data from API
        raw_data = fetch_data_from_api(api_url)

        # Process the data
        processed_data = process_data(raw_data)

        # Generate report
        report = generate_report(processed_data)

        # Print report
        print(report)

    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
