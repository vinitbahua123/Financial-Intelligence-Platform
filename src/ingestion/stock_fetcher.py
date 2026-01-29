"""
Stock Data Fetcher
Downloads historical stock data from Yahoo Finance
"""

import yfinance as yf
import pandas as pd
from datetime import datetime
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.utils.database import get_db_engine
from sqlalchemy import text

def fetch_stock_data(symbol, start_date, end_date):
    """Fetch stock data for a single symbol"""
    print(f"  📥 Fetching {symbol}...", end=" ")
    
    try:
        stock = yf.Ticker(symbol)
        df = stock.history(start=start_date, end=end_date)
        
        if df.empty:
            print(f"❌ No data")
            return None
        
        # Prepare data for database
        df = df.reset_index()
        df['symbol'] = symbol
        df['source'] = 'yahoo_finance'
        df['ingestion_timestamp'] = datetime.now()
        
        # Rename columns to match database
        df = df.rename(columns={
            'Date': 'date',
            'Open': 'open',
            'High': 'high',
            'Low': 'low',
            'Close': 'close',
            'Volume': 'volume'
        })
        
        # Add adj_close (same as close for now)
        df['adj_close'] = df['close']
        
        # Select only required columns
        df = df[['symbol', 'date', 'open', 'high', 'low', 'close', 'adj_close', 
                 'volume', 'source', 'ingestion_timestamp']]
        
        print(f"✅ {len(df)} records")
        return df
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def load_to_database(df, table_name='bronze.stock_prices'):
    """Load dataframe to database"""
    if df is None or df.empty:
        return 0
    
    engine = get_db_engine()
    
    try:
        # Use pandas to_sql with if_exists='append'
        df.to_sql(
            name='stock_prices',
            schema='bronze',
            con=engine,
            if_exists='append',
            index=False,
            method='multi'
        )
        return len(df)
    except Exception as e:
        print(f"    ⚠️  Warning: {e}")
        return 0


def fetch_all_stocks(symbols, start_date, end_date):
    """Fetch data for multiple stocks"""
    print(f"\n{'='*60}")
    print(f"📊 FETCHING STOCK DATA")
    print(f"{'='*60}")
    print(f"Symbols: {', '.join(symbols)}")
    print(f"Period: {start_date} to {end_date}")
    print(f"{'='*60}\n")
    
    total_records = 0
    successful = 0
    
    for symbol in symbols:
        df = fetch_stock_data(symbol, start_date, end_date)
        if df is not None:
            records = load_to_database(df)
            total_records += records
            successful += 1
    
    print(f"\n{'='*60}")
    print(f"✅ COMPLETE!")
    print(f"{'='*60}")
    print(f"Successfully fetched: {successful}/{len(symbols)} stocks")
    print(f"Total records loaded: {total_records:,}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    # Stock symbols to fetch
    symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 
               'META', 'NVDA', 'JPM', 'V', 'WMT']
    
    # Date range (5 years)
    start_date = '2019-01-01'
    end_date = '2024-12-31'
    
    fetch_all_stocks(symbols, start_date, end_date)
