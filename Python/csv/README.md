# CSV File Handling in Python

This folder contains Python scripts that demonstrate reading from and writing to CSV files using the built-in `csv` module.  
These examples focus on practical data automation scenarios with proper input validation and error handling.

---

## Scripts

### `reader.py`
Reads the `sales.csv` file and prints each row in a structured format:


- Uses `csv.DictReader`
- Iterates over CSV data as dictionaries
- Demonstrates clear and readable data output

### `writer.py`
Creates or updates `sales.csv` by taking user input for items, quantity, and price.

- Uses `csv.DictWriter`
- Writes headers and calculates `total_price`
- Includes input validation (`int` for quantity, `float` for price)
- Supports graceful exit via `EOFError`

---

## Sample Data

`sales.csv`:

```csv
item,quantity,price,total_price
apple,10,0.5,5.0
banana,5,0.3,1.5
orange,8,0.6,4.8

---

## Key Concepts

- File I/O with context managers (with statement)
- Reading CSVs using csv.DictReader
- Writing CSVs using csv.DictWriter
- Input validation and basic error handling
- Automating data recording tasks