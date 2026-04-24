# Get data from CSVs
# In this exercise, you'll create a dataframe from a CSV file. The United States makes available CSV files containing tax data by ZIP or postal code, allowing us to analyze income information in different parts of the country. We'll focus on a subset of the data, vt_tax_data_2016.csv, which has select tax statistics by ZIP code in Vermont in 2016.

# To load the data, you'll need to import the pandas library, then read vt_tax_data_2016.csv and assign the resulting dataframe to a variable. Then we'll have a look at the data.

# Import the pandas library as pd.
# Use read_csv() to load vt_tax_data_2016.csv and assign it to the variable data.
# View the first few lines of the dataframe with the head() method. This code has been written for you.

# Import pandas as pd
import pandas as pd

# Read the CSV and assign it to the variable data
data = pd.read_csv('vt_tax_data_2016.csv')

# View the first few lines of data
print(data.head())

# _________________________________________________________________

# Get data from other flat files
# While CSVs are the most common kind of flat file, you will sometimes find files that use different delimiters. read_csv() can load all of these with the help of the sep keyword argument. By default, pandas assumes that the separator is a comma, which is why we do not need to specify sep for CSVs.

# The version of Vermont tax data here is a tab-separated values file (TSV), so you will need to use sep to pass in the correct delimiter when reading the file. Remember that tabs are represented as \t. Once the file has been loaded, the remaining code groups the N1 field, which contains income range categories, to create a chart of tax returns by income category.

# Import pandas with the alias pd.
# Load vt_tax_data_2016.tsv, making sure to set the correct delimiter with the sep keyword argument.

# Import pandas with the alias pd
import pandas as pd

# Load TSV using the sep keyword argument to set delimiter
data = pd.read_csv('vt_tax_data_2016.tsv', sep = '\t')

# Plot the total number of tax returns by income group
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()
plt.show()

# _________________________________________________________________

# Import a subset of columns
# The Vermont tax data contains 147 columns describing household composition, income sources, and taxes paid by ZIP code and income group. Most analyses don't need all these columns. In this exercise, you will create a dataframe with fewer variables using read_csv()s usecols argument.

# Let's focus on household composition to see if there are differences by geography and income level. To do this, we'll need columns on income group, ZIP code, tax return filing status (e.g., single or married), and dependents. The data uses codes for variable names, so the specific columns needed are in the instructions.

# pandas has already been imported as pd.

# Create a list of columns to use: zipcode, agi_stub (income group), mars1 (number of single households), MARS2 (number of households filing as married), and NUMDEP (number of dependents).
# Create a dataframe from vt_tax_data_2016.csv that uses only the selected columns.

# Create list of columns to use
cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']

# Create dataframe from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols = cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())

# _________________________________________________________________

# Import a file in chunks
# When working with large files, it can be easier to load and process the data in pieces. Let's practice this workflow on the Vermont tax data.

# The first 500 rows have been loaded as vt_data_first500. You'll get the next 500 rows. To do this, you'll employ several keyword arguments: nrows and skiprows to get the correct records, header to tell pandas the data does not have column names, and names to supply the missing column names. You'll also want to use the list() function to get column names from vt_data_first500 to reuse.

# pandas has been imported as pd.

# Use nrows and skiprows to make a dataframe, vt_data_next500, with the next 500 rows.
# Set the header argument so that pandas knows there is no header row.
# Name the columns in vt_data_next500 by supplying a list of vt_data_first500's columns to the names argument.

# Create dataframe of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv", 
                       		  nrows = 500,
                       		  skiprows = 500,
                       		  header = None,
                       		  names = list(vt_data_first500))

print(vt_data_next500.shape)

# View the Vermont dataframes to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())

# _________________________________________________________________

# Specify data types
# When loading a flat file, pandas infers the best data type for each column. Sometimes its guesses are off, particularly for numbers that represent groups or qualities instead of quantities.

# Looking at the data dictionary for vt_tax_data_2016.csv reveals two such columns. The agi_stub column contains numbers that correspond to income categories, and zipcode has 5-digit values that should be strings -- treating them as integers means we lose leading 0s, which are meaningful. Let's specify the correct data types with the dtype argument.

# pandas has been imported for you as pd.
    
# Load vt_tax_data_2016.csv with no arguments and view the dataframe's dtypes attribute. Note the data types of zipcode and agi_stub.
# Create a dictionary, data_types, specifying that agi_stub is "category" data and zipcode is string data.
# Reload the CSV with the dtype argument and the dictionary to set the correct column data types.
# View the dataframe's dtypes attribute.

# Load csv with no additional arguments
data = pd.read_csv("vt_tax_data_2016.csv")

# Print the data types
print(data.dtypes)

# Create dict specifying data types for agi_stub and zipcode
data_types = {'agi_stub' : 'category',
			  'zipcode' : str}

# Load csv using dtype to set correct data types
data = pd.read_csv("vt_tax_data_2016.csv", dtype = data_types)

# Print data types of resulting frame
print(data.dtypes.head())

# _________________________________________________________________

# Set custom NA values
# Part of data exploration and cleaning consists of checking for missing or NA values and deciding how to account for them. This is easier when missing values are treated as their own data type. and there are pandas functions that specifically target such NA values. pandas automatically treats some values as missing, but we can pass additional NA indicators with the na_values argument. Here, you'll do this to ensure that invalid ZIP codes in the Vermont tax data are coded as NA.

# pandas has been imported as pd.

# Create a dictionary, null_values, specifying that 0s in the zipcode column should be considered NA values.
# Load vt_tax_data_2016.csv, using the na_values argument and the dictionary to make sure invalid ZIP codes are treated as missing.

# Create dict specifying that 0s in zipcode are NA values
null_values = {'zipcode' : 0}

# Load csv using na_values keyword argument
data = pd.read_csv("vt_tax_data_2016.csv", 
                   na_values = null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])

# _________________________________________________________________

# Skip bad data
# In this exercise you'll use read_csv() parameters to handle files with bad data, like records with more values than columns. By default, trying to import such files triggers a specific error, pandas.errors.ParserError.

# Some lines in the Vermont tax data here are corrupted. In order to load the good lines, we need to tell pandas to skip errors. We also want pandas to warn us when it skips a line so we know the scope of data issues.

# pandas has been imported as pd. The exercise code will try to read the file. If there is a pandas.errors.ParserError, the code in the except block will run.

# Try to import the file vt_tax_data_2016_corrupt.csv without any keyword arguments.
# Import vt_tax_data_2016_corrupt.csv with the error_bad_lines parameter set to skip bad records.
# Update the import with the warn_bad_lines parameter set to issue a warning whenever a bad record is skipped.

try:
  # Import the CSV without any keyword arguments
  data = pd.read_csv('vt_tax_data_2016_corrupt.csv')
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")

try:
  # Import CSV with error_bad_lines set to skip bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines = False)
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")

try:
  # Set warn_bad_lines to issue warnings about bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines=False, 
                     warn_bad_lines = True)
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")

# _________________________________________________________________

# Get data from a spreadsheet
# In this exercise, you'll create a dataframe from a "base case" Excel file: one with a single sheet of tabular data. The fcc_survey.xlsx file here has a sample of responses from FreeCodeCamp's annual New Developer Survey. This survey asks participants about their demographics, education, work and home life, plus questions about how they're learning to code. Let's load all of it.

# pandas has not been pre-loaded in this exercise, so you'll need to import it yourself before using read_excel() to load the spreadsheet.

# Load the pandas library as pd.
# Read in fcc_survey.xlsx and assign it to the variable survey_responses.
# Print the first few records of survey_responses.

# Load pandas as pd
import pandas as pd

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel("fcc_survey.xlsx")

# View the head of the dataframe
print(survey_responses.head())

# _________________________________________________________________

# Load a portion of a spreadsheet
# Spreadsheets meant to be read by people often have multiple tables, e.g., a small business might keep an inventory workbook with tables for different product types on a single sheet. Even tabular data may have header rows of metadata, like the New Developer Survey data here. While the metadata is useful, we don't want it in a dataframe. You'll use read_excel()'s skiprows keyword to get just the data. You'll also create a string to pass to usecols to get only columns AD and AW through BA, about future job goals.

# pandas has been imported as pd.

# Create a single string, col_string, specifying that pandas should load column AD and the range AW through BA.
# Load fcc_survey_headers.xlsx', setting skiprows and usecols to skip the first two rows of metadata and get only the columns in col_string.
# View the selected column names in the resulting dataframe.

# Create string of lettered columns to load
col_string = ('AD, AW:BA')

# Load data with skiprows and usecols set
survey_responses = pd.read_excel("fcc_survey_headers.xlsx", 
                        skiprows = 2, 
                        usecols = col_string)

# View the names of the columns selected
print(survey_responses.columns)

# _________________________________________________________________

# Select a single sheet
# An Excel workbook may contain multiple sheets of related data. The New Developer Survey response workbook has sheets for different years. Because read_excel() loads only the first sheet by default, you've already gotten survey responses for 2016. Now, you'll create a dataframe of 2017 responses using read_excel()'s sheet_name argument in a couple different ways.

# pandas has been imported as pd.

# Create a dataframe from the second workbook sheet by passing the sheet's position to sheet_name.

# Create a dataframe from the 2017 sheet by providing the sheet's name to read_excel().

# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name = 1)

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name = '2017')

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

# _________________________________________________________________

# Select multiple sheets
# So far, you've read Excel files one sheet at a time, which lets you customize import arguments for each sheet. But if an Excel file has some sheets that you want loaded with the same parameters, you can get them in one go by passing a list of their names or indices to read_excel()'s sheet_name keyword. To get them all, pass None. You'll practice both methods to get data from fcc_survey.xlsx, which has multiple sheets of similarly-formatted data.

# pandas has been loaded as pd.

# Load both the 2016 and 2017 sheets by name with a list and one call to read_excel().
# Load the 2016 sheet by its position (0) and 2017 by name. Note the sheet names in the result.
# Load all sheets in the Excel file without listing them all.

# Load both the 2016 and 2017 sheets by name
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name = ['2016', '2017'])

# View the data type of all_survey_data
print(type(all_survey_data))

# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name = [0, '2017'])

# View the sheet names in all_survey_data
print(all_survey_data.keys())

# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name = None)

# View the sheet names in all_survey_data
print(all_survey_data.keys())

# _________________________________________________________________

# Work with multiple spreadsheets
# Workbooks meant primarily for human readers, not machines, may store data about a single subject across multiple sheets. For example, a file may have a different sheet of transactions for each region or year in which a business operated.

# The FreeCodeCamp New Developer Survey file is set up similarly, with samples of responses from different years in different sheets. Your task here is to compile them in one dataframe for analysis.

# pandas has been imported as pd. All sheets have been read into the ordered dictionary responses, where sheet names are keys and dataframes are values, so you can get dataframes with the values() method.

# Create an empty dataframe, all_responses.
# Set up a for loop to iterate through the values in the responses dictionary.
# Concatenate each dataframe to all_responses and reassign the result to the same variable name.

# Create an empty dataframe
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in responses.values():
  # Print the number of rows being added
  print("Adding {} rows".format(df.shape[0]))
  # Concatenate all_responses and df, assign result
  all_responses = pd.concat([all_responses, df])

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()

# _________________________________________________________________

# Set Boolean columns
# Datasets may have columns that are most accurately modeled as Boolean values. However, pandas usually loads these as floats by default, since defaulting to Booleans may have undesired effects like turning NA values into Trues.

# fcc_survey_subset.xlsx contains a string ID column and several True/False columns indicating financial stressors. You'll evaluate which non-ID columns have no NA values and therefore can be set as Boolean, then tell read_excel() to load them as such with the dtype argument.

# pandas is loaded as pd.

# Count NA values in each column of survey_data with isna() and sum(). Note which columns besides ID.x, if any, have zero NAs.

# Load the data
survey_data = pd.read_excel("fcc_survey_subset.xlsx")

# Count NA values in each column
print(survey_data.isna().sum())

# Set read_excel()'s dtype argument to load the HasDebt column as Boolean data.
# Supply the Boolean column name to the print statement to view financial burdens by group.

# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("fcc_survey_subset.xlsx",
                            dtype = {'HasDebt' : bool})

# View financial burdens by Boolean group
print(survey_data.groupby('HasDebt').sum())

# _________________________________________________________________

# Set custom true/false values
# In Boolean columns, pandas automatically recognizes certain values, like "TRUE" and 1, as True, and others, like "FALSE" and 0, as False. Some datasets, like survey data, can use unrecognized values, such as "Yes" and "No".

# For practice purposes, some Boolean columns in the New Developer Survey have been coded this way. You'll make sure they're properly interpreted with the help of the true_values and false_values arguments.

# pandas is loaded as pd. You can assume the columns you are working with have no missing values.

# Load the Excel file, specifying "Yes" as a true value and "No" as a false value.

# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel("fcc_survey_yn_data.xlsx",
                              dtype={"HasDebt": bool,
                              "AttendedBootCampYesNo": bool},
                              true_values = ["Yes"],
                              false_values = ["No"])

# View the data
print(survey_subset.head())

# _________________________________________________________________

# Parse simple dates
# pandas does not infer that columns contain datetime data; it interprets them as object or string data unless told otherwise. Correctly modeling datetimes is easy when they are in a standard format -- we can use the parse_dates argument to tell read_excel() to read columns as datetime data.

# The New Developer Survey responses contain some columns with easy-to-parse timestamps. In this exercise, you'll make sure they're the right data type.

# pandas has been loaded as pd.

# Load fcc_survey.xlsx, making sure that the Part1StartTime column is parsed as datetime data.
# View the first few values of the survey_data.Part1StartTime to make sure it contains datetimes.

# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("fcc_survey.xlsx",
                            parse_dates = ["Part1StartTime"])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())

# _________________________________________________________________

# Get datetimes from multiple columns
# Sometimes, datetime data is split across columns. A dataset might have a date and a time column, or a date may be split into year, month, and day columns.

# A column in this version of the survey data has been split so that dates are in one column, Part2StartDate, and times are in another, Part2StartTime. Your task is to use read_excel()'s parse_dates argument to combine them into one datetime column with a new name.

# pandas has been imported as pd.

# Create a dictionary, datetime_cols indicating that the new column Part2Start should consist of Part2StartDate and Part2StartTime.
# Load the survey response file, supplying the dictionary to the parse_dates argument to create a new Part2Start column.
# View summary statistics about the new Part2Start column with the describe() method.

# Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start": ["Part2StartDate", "Part2StartTime"]}


# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("fcc_survey_dts.xlsx",
                            parse_dates = datetime_cols)

# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())

# _________________________________________________________________

# Parse non-standard date formats
# So far, you've parsed dates that pandas could interpret automatically. But if a date is in a non-standard format, like 19991231 for December 31, 1999, it can't be parsed at the import stage. Instead, use pd.to_datetime() to convert strings to dates after import.

# The New Developer Survey data has been loaded as survey_data but contains an unparsed datetime field. We'll use to_datetime() to convert it, passing in the column to convert and a string representing the date format used.

# For more on date format codes, see this reference. Some common codes are year (%Y), month (%m), day (%d), hour (%H), minute (%M), and second (%S).

# pandas has been imported as pd.

# Parse Part2EndTime using pd.to_datetime(), the format keyword argument, and the format string you just identified. Assign the result back to the Part2EndTime column.
# Print the head of Part2EndTime to confirm the column now contains datetime values.

# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"],
                                   format='%m%d%Y %H:%M:%S')

# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"], 
                                             format="%m%d%Y %H:%M:%S")

# Print first few values of Part2EndTime
print(survey_data.Part2EndTime.head())

# _________________________________________________________________

# Connect to a database
# In order to get data from a database with pandas, you first need to be able to connect to one. In this exercise, you'll practice creating a database engine to manage connections to a database, data.db. To do this, you'll use sqlalchemy's create_engine() function.

# create_engine() needs a string URL to the database. For SQLite databases, that string consists of "sqlite:///", then the database file name.

# Import the create_engine() function from sqlalchemy.
# Use create_engine() to make a database engine for data.db.
# Run the last line of code to show the names of the tables in the database.

# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine("sqlite:///data.db")

# View the tables in the database
print(engine.table_names())

# _________________________________________________________________

# Load entire tables
# In the last exercise, you saw that data.db has two tables. weather has historical weather data for New York City. hpd311calls is a subset of call records made to the city's 311 help line about housing issues.

# In this exercise, you'll use the read_sql() function in pandas to load both tables. read_sql() accepts a string of either a SQL query to run, or a table to load. It also needs a way to connect to the database, like the engine in the provided code.

# Use read_sql() to load the hpd311calls table by name, without any SQL.
# Use read_sql() and a SELECT * ... SQL query to load the entire weather table.

# Load libraries
import pandas as pd
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine('sqlite:///data.db')

# Load hpd311calls without any SQL
hpd_calls = pd.read_sql('hpd311calls', engine)

# View the first few rows of data
print(hpd_calls.head())

# Create the database engine
engine = create_engine("sqlite:///data.db")

# Create a SQL query to load the entire weather table
query = """
SELECT * 
  FROM weather;
"""

# Load weather with the SQL query
weather = pd.read_sql(query, engine)

# View the first few rows of data
print(weather.head())

# _________________________________________________________________

# Selecting columns with SQL
# Datasets can contain columns that are not required for an analysis, like the weather table in data.db does. Some, such as elevation, are redundant, since all observations occurred at the same place, while others contain variables we are not interested in. After making a database engine, you'll write a query to SELECT only the date and temperature columns, and pass both to read_sql() to make a dataframe of high and low temperature readings.

# pandas has been loaded as pd, and create_engine() has been imported from sqlalchemy.

# Note: The SQL checker is quite picky about column positions and expects fields to be selected in the specified order.

# Create a database engine for data.db.
# Write a SQL query that SELECTs the date, tmax, and tmin columns from the weather table.
# Make a dataframe by passing the query and engine to read_sql() and assign the resulting dataframe to temperatures.

# Create database engine for data.db
engine = create_engine("sqlite:///data.db")

# Write query to get date, tmax, and tmin from weather
query = """
SELECT date, 
       tmax, 
       tmin
  FROM weather;
"""

# Make a dataframe by passing query and engine to read_sql()
temperatures = pd.read_sql(query, engine)

# View the resulting dataframe
print(temperatures)

# _________________________________________________________________

# Selecting rows
# SQL WHERE clauses return records whose values meet the given criteria. Passing such a query to read_sql() results in a dataframe loaded with only records we are interested in, so there is less filtering to do later on.

# The hpd311calls table in data.db has data on calls about various housing issues, from maintenance problems to information requests. In this exercise, you'll use SQL to focus on calls about safety.

# pandas has been loaded as pd, and a database engine, engine, has been created for data.db.

# Create a query that selects all columns of records in hpd311calls that have 'SAFETY' as their complaint_type.
# Use read_sql() to query the database and assign the result to the variable safety_calls.
# Run the last section of code to create a graph of safety call counts in each borough.

# Create query to get hpd311calls records about safety
query = """
SELECT *
FROM hpd311calls
WHERE complaint_type = 'SAFETY';
"""

# Query the database and assign result to safety_calls
safety_calls = pd.read_sql(query, engine)

# Graph the number of safety calls by borough
call_counts = safety_calls.groupby('borough').unique_key.count()
call_counts.plot.barh()
plt.show()

# _________________________________________________________________

# Filtering on multiple conditions
# So far, you've selectively imported records that met a single condition, but it's also common to filter datasets on multiple criteria. In this exercise, you'll do just that.

# The weather table contains daily high and low temperatures and precipitation amounts for New York City. Let's focus on inclement weather, where there was either an inch or more of snow or the high was at or below freezing (32° Fahrenheit). To do this, you'll need to build a query that uses the OR operator to look at values in both columns.

# pandas is loaded as pd, and a database engine, engine, has been created.

# Create a query that selects records in weather where tmax is less than or equal to 32 degrees OR snow is greater than or equal to 1 inch.
# Use read_sql() to query the database and assign the result to the variable wintry_days.
# View summary statistics with the describe() method to make sure all records in the dataframe meet the given criteria.

# Create query for records with max temps <= 32 or snow >= 1
query = """
SELECT *
  FROM weather
  WHERE tmax <= 32
  OR snow >= 1;
"""

# Query database and assign result to wintry_days
wintry_days = pd.read_sql(query, engine)

# View summary stats about the temperatures
print(wintry_days.describe())

# _________________________________________________________________

# Getting distinct values
# Sometimes an analysis doesn't need every record, but rather unique values in one or more columns. Duplicate values can be removed after loading data into a dataframe, but it can also be done at import with SQL's DISTINCT keyword.

# Since hpd311calls contains data about housing issues, we would expect most records to have a borough listed. Let's test this assumption by querying unique complaint_type/borough combinations.

# pandas has been imported as pd, and the database engine has been created as engine.

# Note: The SQL checker is quite picky about column positions and expects fields to be selected in the specified order.

# Create a query that gets DISTINCT values for borough and complaint_type (in that order) from hpd311calls.
# Use read_sql() to load the results of the query to a dataframe, issues_and_boros.
# Print the dataframe to check if the assumption that all issues besides literature requests appear with boroughs listed.

# Create query for unique combinations of borough and complaint_type
query = """
SELECT DISTINCT borough, 
       complaint_type
  FROM hpd311calls;
"""

# Load results of query to a dataframe
issues_and_boros = pd.read_sql(query, engine)

# Check assumption about issues and boroughs
print(issues_and_boros)

# _________________________________________________________________

# Counting in groups
# In previous exercises, you pulled data from tables, then summarized the resulting dataframes in pandas to create graphs. By using COUNT and GROUP BY in a SQL query, we can pull those summary figures from the database directly.

# The hpd311calls table has a column, complaint_type, that categorizes call records by issue, such as heating or plumbing. In order to graph call volumes by issue, you'll write a SQL query that COUNTs records by complaint type.

# pandas has been imported as pd, and the database engine for data.db has been created as engine.

# Create a SQL query that gets the complaint_type column and counts of all records from hpd311calls, grouped by complaint_type.
# Create a dataframe with read_sql() of call counts by issue, calls_by_issue.
# Run the last section of code to graph the number of calls for each housing issue.

# Create query to get call counts by complaint_type
query = """
SELECT complaint_type, 
     COUNT(*)
  FROM hpd311calls
  GROUP BY complaint_type;
"""

# Create dataframe of call counts by issue
calls_by_issue = pd.read_sql(query, engine)

# Graph the number of calls for each housing issue
calls_by_issue.plot.barh(x="complaint_type")
plt.show()

# _________________________________________________________________

# Working with aggregate functions
# If a table contains data with higher granularity than is needed for an analysis, it can make sense to summarize the data with SQL aggregate functions before importing it. For example, if you have data of flood event counts by month but precipitation data by day, you may decide to SUM precipitation by month.

# The weather table contains daily readings for four months. In this exercise, you'll practice summarizing weather by month with the MAX, MIN, and SUM functions.

# pandas has been loaded as pd, and a database engine, engine, has been created.

# Create a query to pass to read_sql() that will get months and the MAX value of tmax by monthfrom weather.
# Modify the query to also get the MIN tmin value for each month.
#    Modify the query to also get the total precipitation (prcp) for each month.

# Create a query to get month and max tmax by month
query = """
SELECT month, 
       MAX(tmax)
  FROM weather 
  GROUP BY month;"""

# Get dataframe of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)

# Create a query to get month, max tmax, and min tmin by month
query = """
SELECT month, 
	   MAX(tmax), 
       MIN(tmin)
  FROM weather 
 GROUP BY month;
"""

# Get dataframe of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)

# Create query to get temperature and precipitation by month
query = """
SELECT month, 
        MAX(tmax), 
        MIN(tmin),
        SUM(prcp)
  FROM weather 
 GROUP BY month;
"""

# Get dataframe of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)

# _________________________________________________________________

# Joining tables
# Tables in relational databases usually have key columns of unique record identifiers. This lets us build pipelines that combine tables using SQL's JOIN operation, instead of having to combine data after importing it.

# The records in hpd311calls often concern issues, like leaks or heating problems, that are exacerbated by weather conditions. In this exercise, you'll join weather data to call records along their common date columns to get everything in one dataframe. You can assume these columns have the same data type.

# pandas is loaded as pd, and the database engine, engine, has been created.

# Note: The SQL checker is picky about join table order -- it expects specific tables on the left and the right.

# Complete the query to join weather to hpd311calls by their date and created_date columns, respectively.
# Query the database and assign the resulting dataframe to calls_with_weather.
# Print the first few rows of calls_with_weather to confirm all columns were joined.

# Query to join weather to call records by date columns
query = """
SELECT * 
  FROM hpd311calls
  JOIN weather 
  ON hpd311calls.created_date = weather.date;
"""

# Create dataframe of joined tables
calls_with_weather = pd.read_sql(query, engine)

# View the dataframe to make sure all columns were joined
print(calls_with_weather.head())

# _________________________________________________________________

# Joining and filtering
# Just as you might not always want all the data in a single table, you might not want all columns and rows that result from a JOIN. In this exercise, you'll use SQL to refine a data import.

# Weather exacerbates some housing problems more than others. Your task is to focus on water leak reports in hpd311calls and assemble a dataset that includes the day's precipitation levels from weather to see if there is any relationship between the two. The provided SQL gets all columns in hpd311calls, but you'll need to modify it to get the necessary weather column and filter rows with a WHERE clause.

# pandas is loaded as pd, and the database engine, engine, has been created.

# Complete query to get the prcp column in weather and join weather to hpd311calls on their date and created_date columns, respectively.
# Use read_sql() to load the results of the query into the leak_calls dataframe.

# Query to get hpd311calls and precipitation values
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
  ON hpd311calls.created_date = weather.date;"""

# Load query results into the leak_calls dataframe
leak_calls = pd.read_sql(query, engine)

# View the dataframe
print(leak_calls.head())

# Modify query to get only rows that have 'WATER LEAK' as their complaint_type.

# Query to get water leak calls and daily precipitation
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
    ON hpd311calls.created_date = weather.date
  WHERE hpd311calls.complaint_type = 'WATER LEAK';"""

# Load query results into the leak_calls dataframe
leak_calls = pd.read_sql(query, engine)

# View the dataframe
print(leak_calls.head())

# _________________________________________________________________

# Joining, filtering, and aggregating
# In this exercise, you'll use what you've learned to assemble a dataset to investigate how the number of heating complaints to New York City's 311 line varies with temperature.

# In addition to the hpd311calls table, data.db has a weather table with daily high and low temperature readings for NYC. We want to get each day's count of heat/hot water calls with temperatures joined in. This can be done in one query, which we'll build in parts.

# In part one, we'll get just the data we want from hpd311calls. Then, in part two, we'll modify the query to join in weather data.

# pandas has been imported as pd, and the database engine has been created as engine.

# Complete the query to get created_date and counts of records whose complaint_type is HEAT/HOT WATER from hpd311calls by date.
# Create a dataframe,df, containing the results of the query.

# Query to get heat/hot water call counts by created_date
query = """
SELECT hpd311calls.created_date, 
       COUNT(*)
  FROM hpd311calls 
  WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER'
  GROUP BY hpd311calls.created_date;
"""

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())

# Modify the query to join tmax and tmin from the weather table. (There is only one record per date in weather, so we do not need SQL's MAX and MIN functions here.) Join the tables on created_date in hpd311calls and date in weather.

# Modify query to join tmax and tmin from weather by date
query = """
SELECT hpd311calls.created_date, 
	   COUNT(*), 
       weather.tmax,
       weather.tmin
  FROM hpd311calls 
       JOIN weather
       ON hpd311calls.created_date = weather.date
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
 GROUP BY hpd311calls.created_date;
 """

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())

# _________________________________________________________________

# Load JSON data
# Many open data portals make available JSONs datasets that are particularly easy to parse. They can be accessed directly via URL. Each object is a record, all objects have the same set of attributes, and none of the values are nested objects that themselves need to be parsed.

# The New York City Department of Homeless Services Daily Report is such a dataset, containing years' worth of homeless shelter population counts. You can view it in the console before loading it to a dataframe with pandas's read_json() function.

# Get a sense of the contents of dhs_daily_report.json, which are printed in the console.
# Load pandas as pd.
# Use read_json() to load dhs_daily_report.json to a dataframe, pop_in_shelters.
# View summary statistics about pop_in_shelters with the dataframe's describe() method.

# Load pandas as pd
import pandas as pd

# Load the daily report to a dataframe
pop_in_shelters = pd.read_json("dhs_daily_report.json")

# View summary stats about pop_in_shelters
print(pop_in_shelters.describe())

# _________________________________________________________________

# Work with JSON orientations
# JSON isn't a tabular format, so pandas makes assumptions about its orientation when loading data. Most JSON data you encounter will be in orientations that pandas can automatically transform into a dataframe.

# Sometimes, like in this modified version of the Department of Homeless Services Daily Report, data is oriented differently. To reduce the file size, it has been split formatted. You'll see what happens when you try to load it normally versus with the orient keyword argument. The try/except block will alert you if there are errors loading the data.

# pandas has been loaded as pd.

# Try loading dhs_report_reformatted.json without any keyword arguments.
# Load dhs_report_reformatted.json to a dataframe with orient specified.

try:
    # Load the JSON without keyword arguments
    df = pd.read_json("dhs_report_reformatted.json")
    
    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
    
except ValueError:
    print("pandas could not parse the JSON.")

try:
    # Load the JSON with orient specified
    df = pd.read_json("dhs_report_reformatted.json",
                      orient = 'split')
    
    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
    
except ValueError:
    print("pandas could not parse the JSON.")

# _________________________________________________________________

# Get data from an API
# In this exercise, you'll use requests.get() to query the Yelp Business Search API for cafes in New York City. requests.get() needs a URL to get data from. The Yelp API also needs search parameters and authorization headers passed to the params and headers keyword arguments, respectively.

# You'll need to extract the data from the response with its json() method, and pass it to pandas's DataFrame() function to make a dataframe. Note that the necessary data is under the dictionary key "businesses".

# pandas (as pd) and requests have been loaded. Authorization data is in the dictionary headers, and the needed API parameters are stored as params.

# Get data about New York City cafes from the Yelp API (api_url) with requests.get(). The necessary params and headers information has been provided.
# Extract the JSON data from the response with its json() method, and assign it to data.
# Load the cafe listings to the dataframe cafes with pandas's DataFrame() function. The listings are under the "businesses" key in data.
# Print the dataframe's dtypes to see what information you're getting.

api_url = "https://api.yelp.com/v3/businesses/search"

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url, 
                headers=headers, 
                params=params)

# Extract JSON data from the response
data = response.json()

# Load data to a dataframe
cafes = pd.DataFrame(data["businesses"])

# View the data's dtypes
print(cafes.dtypes)

# _________________________________________________________________

# Set API parameters
# Formatting parameters to get the data you need is an integral part of working with APIs. These parameters can be passed to the get() function's params keyword argument as a dictionary.

# The Yelp API requires the location parameter be set. It also lets users supply a term to search for. You'll use these parameters to get data about cafes in NYC, then process the result to create a dataframe.

# pandas (as pd) and requests have been loaded. The API endpoint is stored in the variable api_url. Authorization data is stored in the dictionary headers.

# Create a dictionary, parameters, with the term and location parameters set to search for "cafe"s in "NYC".
# Query the Yelp API (api_url) with requests's get() function and the headers and params keyword arguments set. Save the result as response.
# Extract the JSON data from response with the appropriate method. Save the result as data.
# Load the "businesses" values in data to the dataframe cafes and print the head.

# Create dictionary to query API for cafes in NYC
parameters = {'term' : "cafe",
          	  'location' : "NYC"}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                headers = headers,
                params = parameters)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print head
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())

# _________________________________________________________________

# Set request headers
# Many APIs require users provide an API key, obtained by registering for the service. Keys typically are passed in the request header, rather than as parameters.

# The Yelp API documentation says "To authenticate API calls with the API Key, set the Authorization HTTP header value as Bearer api_key."

# You'll set up a dictionary to pass this information to get(), call the API for the highest-rated cafes in NYC, and parse the response.

# pandas (as pd) and requests have been loaded. The API endpoint is stored as api_url, and the key is api_key. Parameters are in the dictionary params.

# Create a dictionary, headers, that passes the formatted key string to the "Authorization" header value.
# Query the Yelp API (api_url) with get() and the necessary headers and parameters. Save the result as response.
# Extract the JSON data from response. Save the result as data.
# Load the "businesses" values in data to the dataframe cafes and print the names column.

# Create dictionary that passes Authorization and key string
headers = {'Authorization': "Bearer {}".format(api_key)}

# Query the Yelp API with headers and params set
response = requests.get(api_url, headers = headers, params = params)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print names
cafes = pd.DataFrame(data["businesses"])
print(cafes.name)

# _________________________________________________________________

# Flatten nested JSONs
# A feature of JSON data is that it can be nested: an attribute's value can consist of attribute-value pairs. This nested data is more useful unpacked, or flattened, into its own dataframe columns. The pandas.io.json submodule has a function, json_normalize(), that does exactly this.

# The Yelp API response data is nested. Your job is to flatten out the next level of data in the coordinates and location columns.

# pandas (as pd) and requests have been imported. The results of the API call are stored as response.

# Load the json_normalize() function from pandas' io.json submodule.
# Isolate the JSON data from response and assign it to data.
# Use json_normalize() to flatten and load the businesses data to a dataframe, cafes. Set the sep argument to use underscores (_), rather than periods.
# Show the data head.

# Load json_normalize()
from pandas.io.json import json_normalize

# Isolate the JSON data from the API response
data = response.json()

# Flatten business data into a dataframe, replace separator
cafes = json_normalize(data["businesses"],
             sep = "_")

# View data
print(cafes.head())

# _________________________________________________________________

# Handle deeply nested data
# Last exercise, you flattened data nested down one level. Here, you'll unpack more deeply nested data.

# The categories attribute in the Yelp API response contains lists of objects. To flatten this data, you'll employ json_normalize() arguments to specify the path to categories and pick other attributes to include in the dataframe. You should also change the separator to facilitate column selection and prefix the other attributes to prevent column name collisions. We'll work through this in steps.

# pandas (as pd) and json_normalize() have been imported. JSON-formatted Yelp data on cafes in NYC is stored as data.

# Use json_normalize() to flatten records under the businesses key in data, setting underscores (_) as separators.
# Specify the record_path to the categories data.
# Set the meta keyword argument to get business name, alias, rating, and the attributes nested under coordinates: latitude and longitude.
# Add "biz_" as a meta_prefix to prevent duplicate column names.

# Flatten businesses records and set underscore separators
flat_cafes = json_normalize(data["businesses"],
                  sep = "_")

# View the data
print(flat_cafes.head())

# Specify record path to get categories data
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path = "categories")

# View the data
print(flat_cafes.head())

# Load other business attributes and set meta prefix
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=["name", 
                                  "alias",  
                                  "rating",
                          		  ["coordinates", "latitude"], 
                          		  ["coordinates", "longitude"]],
                    		meta_prefix="biz_")

# View the data
print(flat_cafes.head())

# _________________________________________________________________

# Concatenate dataframes
# In this exercise, you’ll practice concatenating records by creating a dataset of the 100 highest-rated cafes in New York City according to Yelp.

# APIs often limit the amount of data returned, since sending large datasets can be time- and resource-intensive. The Yelp Business Search API limits the results returned in a call to 50 records. However, the offset parameter lets a user retrieve results starting after a specified number. By modifying the offset, we can get results 1-50 in one call and 51-100 in another. Then, we can append the dataframes.

# pandas (as pd), requests, and json_normalize() have been imported. The 50 top-rated cafes are already in a dataframe, top_50_cafes.

# Add an "offset" parameter to params so that the Yelp API call will get cafes 51-100.
# Concatenate the results of the API call to top_50_cafes, setting ignore_index so rows will be renumbered.
# Print the shape of the resulting dataframe, cafes, to confirm there are 100 records.

# Add an offset parameter to get cafes 51-100
params = {"term": "cafe", 
          "location": "NYC",
          "sort_by": "rating", 
          "limit": 50,
          "offset": 50}

result = requests.get(api_url, headers=headers, params=params)
next_50_cafes = json_normalize(result.json()["businesses"])
# Concatenate the results, setting ignore_index to renumber rows
cafes = pd.concat([top_50_cafes, next_50_cafes], ignore_index=True)

# Print shape of cafes
print(cafes.shape)

# _________________________________________________________________

# Merge dataframes
# In the last exercise, you built a dataset of the top 100 cafes in New York City according to Yelp. Now, you'll combine that with demographic data to investigate which neighborhood has the most good cafes per capita.

# To do this, you'll merge two datasets with the DataFrame merge() method. The first,crosswalk, is a crosswalk between ZIP codes and Public Use Micro Data Sample Areas (PUMAs), which are aggregates of census tracts and correspond roughly to NYC neighborhoods. Then, you'll merge in pop_data, which contains 2016 population estimates for each PUMA.

# pandas (as pd) has been imported, as has the cafes dataframe from last exercise.

# Use the DataFrame method to merge cafes and crosswalk on location_zip_code and zipcode, respectively. Assign the result to cafes_with_pumas.
# Merge pop_data into cafes_with_pumas on their puma fields. Save the result as cafes_with_pop.

# Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(crosswalk, left_on = "location_zip_code", right_on = "zipcode")

# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(pop_data, on = "puma")

# View the data
print(cafes_with_pop.head())