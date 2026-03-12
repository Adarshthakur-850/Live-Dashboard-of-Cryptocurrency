# Live Cryptocurrency Trends Dashboard

A real-time dashboard to track cryptocurrency prices, trends, and market overview using CoinGecko API.

## Project Structure
- `src/`: Core logic (Data fetching, Processing, Visualization).
- `app.py`: Main Streamlit application.

## Features
- **Live Prices**: Fetches top coins by market cap.
- **Interactive Charts**: Price trends (Line) and Market Heatmap (Treemap).
- **Auto-Refresh**: Updates data every 60 seconds automatically.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
Run the dashboard:
```bash
streamlit run app.py
```
