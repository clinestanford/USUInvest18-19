#!/bin/bash


python StockData.py >> logs/20190211.stockData.log;

python api-fetcher.py >> logs/20190212.cryptoData.log;






