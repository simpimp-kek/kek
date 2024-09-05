import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime, timedelta

def fetch_data_from_api(start_date, end_date, latitude, longitude):
    """Fetch temperature data from the Open-Meteo API."""
    url = f"https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "Europe/London"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def process_data(data):
    """Process the API data into a pandas DataFrame."""
    df = pd.DataFrame({
        'date': pd.to_datetime(data['daily']['time']),
        'max_temp': data['daily']['temperature_2m_max'],
        'min_temp': data['daily']['temperature_2m_min']
    })
    df['avg_temp'] = (df['max_temp'] + df['min_temp']) / 2
    return df

def generate_report(data):
    """Generate a report with visualizations and summary statistics."""
    # Create a line plot of average temperature
    plt.figure(figsize=(12, 6))
    plt.plot(data['date'], data['avg_temp'])
    plt.title('Daily Average Temperature - Last 30 Days')
    plt.xlabel('Date')
    plt.ylabel('Average Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('temperature_trend.png')
    plt.close()

    # Calculate summary statistics
    avg_temp = data['avg_temp'].mean()
    max_temp = data['max_temp'].max()
    min_temp = data['min_temp'].min()

    # Prepare report text
    report = f"""
    Weather Report Summary for London:
    ----------------------------------
    Period: {data['date'].min().strftime('%Y-%m-%d')} to {data['date'].max().strftime('%Y-%m-%d')}
    Average Temperature: {avg_temp:.1f}°C
    Highest Temperature: {max_temp:.1f}°C
    Lowest Temperature: {min_temp:.1f}°C
    
    The temperature trend chart has been saved as 'temperature_trend.png'.
    """

    return report

def main():
    # Set location (London)
    latitude = 51.5074
    longitude = -0.1278

    # Set date range (last 30 days)
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=30)

    try:
        # Fetch data from API
        raw_data = fetch_data_from_api(start_date, end_date, latitude, longitude)

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
