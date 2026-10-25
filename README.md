# Data Engineering Practice

My practice work while learning data engineering with Python, pandas, SQL and GitHub. Each folder covers one topic, with the code, the data it uses, and the output it makes.

## What's inside
| Folder | What I practised |
|---|---|
| `Basics` | Python basics: lists, loops, if/else, functions, error handling, dictionaries, f-strings |
| `Numpy_basics` | numpy arrays, maths on arrays, filtering, missing values |
| `pandas_basics` | Reading CSV files, selecting, filtering, sorting, adding columns, groupby |
| `Clean_&_Join(Pandas)` | Cleaning messy data (duplicates, blanks, text case) and joining tables (inner, left, right) |
| `Pandas-Sql` | Saving tables into a SQLite database and querying them with SQL |
| `Matplotlib` | Bar and pie charts from sales data |
| `Seaborn_basics` | Cleaner-looking bar charts with seaborn, including colour by category |
| `Python_basics` | A small pipeline: read sales data, add a tax column, save the result |

## Mini pipeline (Python_basics/read_data.py)
1. **Extract:** read `sales.csv`
2. **Transform:** add a `price_with_tax` column (price plus 10% tax, rounded to 2 decimals)
3. **Load:** save the result to `clean_sales.csv`

## Skills shown
- Reading and writing CSV files
- Cleaning data: duplicates, missing values, inconsistent text
- Joining tables with pandas and with SQL
- Saving data into a SQLite database
- Making charts with matplotlib and seaborn
- Using Git and GitHub: commits, folders, branches and pull requests

## How to run
1. Install Python, then install the tools with `pip install pandas numpy matplotlib seaborn`
2. Put the script and its CSV file (from the `Data` folder) in the same folder
3. Run the script with `python script_name.py`

## Tools used
Python, pandas, numpy, SQLite, matplotlib, seaborn, GitHub

## Author
Vinay Simha M K
