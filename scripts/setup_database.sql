-- Financial Intelligence Platform - Database Setup
-- Creates Bronze/Silver/Gold layers

CREATE SCHEMA IF NOT EXISTS bronze;
CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS gold;

DROP TABLE IF EXISTS bronze.stock_prices CASCADE;
DROP TABLE IF EXISTS bronze.company_info CASCADE;

CREATE TABLE bronze.stock_prices (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    date DATE NOT NULL,
    open DECIMAL(12, 4),
    high DECIMAL(12, 4),
    low DECIMAL(12, 4),
    close DECIMAL(12, 4),
    adj_close DECIMAL(12, 4),
    volume BIGINT,
    source VARCHAR(50) DEFAULT 'yahoo_finance',
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(symbol, date)
);

CREATE TABLE bronze.company_info (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) UNIQUE NOT NULL,
    company_name VARCHAR(255),
    sector VARCHAR(100),
    industry VARCHAR(100),
    market_cap BIGINT,
    description TEXT,
    source VARCHAR(50) DEFAULT 'yahoo_finance',
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_stock_prices_symbol ON bronze.stock_prices(symbol);
CREATE INDEX idx_stock_prices_date ON bronze.stock_prices(date);
CREATE INDEX idx_stock_prices_symbol_date ON bronze.stock_prices(symbol, date);
