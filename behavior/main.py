import requests
import pandas as pd
import streamlit as st
from config import settings

def get_data(url: str):
    """Retrieve data from FastAPI endpoint and return as a DataFrame."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
    data_dict = response.json()
    
    data = pd.DataFrame(list(data_dict.items()), columns=['Date', 'Amount'])
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    return data

def visualize_daily_expenses(data: pd.DataFrame):
    """Visualize daily expenses with Streamlit."""
    st.title('Daily Expenses')
    st.line_chart(data)

def main():
    daily_expenses_url = f"{settings.USER_BEHAVIOR_URL}/{settings.DAILY_EXPENSES}"
    daily_expenses_data = get_data(daily_expenses_url)
    visualize_daily_expenses(daily_expenses_data)


if __name__ == "__main__":
    main()
