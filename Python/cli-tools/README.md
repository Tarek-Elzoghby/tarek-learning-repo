# CLI Tools (Command-Line Utilities)

This folder contains **command-line Python tools** built while learning and practicing
automation, file processing, and professional scripting patterns.

Each script in this folder is designed to be run from the terminal and follows
best practices such as input validation, structured output, and error handling.

---

## 🧰 Tools Included

### `pizza.py`
A command-line utility that:
- Accepts a CSV file as an argument
- Validates command-line input and file type
- Reads menu data from the CSV file
- Outputs a formatted ASCII table using the `tabulate` library
- Uses logging to record execution and error events

Example usage:
```bash
python pizza.py sicilian.csv
```
---

### `scourgify.py`
A command-line data-cleaning utility that:
- Accepts an input CSV file and an output CSV file as arguments
- Reads student data where names are stored as "Last, First"
- Splits names into separate first name and last name columns
- Writes cleaned data to a new CSV file
- Uses logging to track execution steps and errors

Example usage:
```bash
python scourgify.py scourgify.csv output.csv
```
---
### `shirt.py`
A command-line image processing utility that:
- Accepts an input image and output image as arguments
- Validates file extensions (`.jpg`, `.jpeg`, `.png`) and matching types
- Opens the input image and a `shirt.png` overlay
- Resizes/crops the input to match the shirt
- Pastes the shirt onto the input image
- Saves the result to the output file
- Logs execution steps and errors

Example usage:
```bash
python shirt.py input.jpg output.jpg
```

