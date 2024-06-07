# RentScrape Project

## Overview
RentScrape is a data pipeline project designed to scrape rental data from a website, store it in a local MinIO database, and use DuckDB combined with dbt to clean and transform the data. The cleaned data is then loaded into Metabase to create interactive dashboards.

## Features
- **Data Scraping**: Uses Python to scrape rental data from a specified website.
- **Data Storage**: Stores the scraped data into a CSV file in a local MinIO database.
- **Data Cleaning**: Utilizes DuckDB and dbt to clean and transform the data.
- **Data Visualization**: Loads the cleaned data into Metabase to create and display dashboards.


## Setup and Installation

### Prerequisites
- Python 3.x
- MinIO
- DuckDB
- dbt (Data Build Tool)
- Metabase


## Acknowledgements
- [MinIO](https://min.io/)
- [DuckDB](https://duckdb.org/)
- [dbt](https://www.getdbt.com/)
- [Metabase](https://www.metabase.com/)

