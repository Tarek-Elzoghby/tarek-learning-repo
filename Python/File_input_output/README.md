# File I/O Automation Scripts

This folder contains Python scripts demonstrating practical file handling and command-line argument usage.  
These examples focus on automating file-based tasks with proper input validation and error handling.

---

## Scripts

### `line_counter.py`
Counts the number of non-empty, non-comment lines in a Python file provided as a command-line argument.

**Features:**
- Accepts a single Python file as a command-line argument
- Validates:
  - Missing or extra arguments
  - File existence
  - File type (`.py` only)
- Ignores comments (`# ...`) and blank lines
- Returns a line count to the console
- Uses `sys.exit()` with distinct codes for different error types

**Usage:**

```bash
python lines.py 
