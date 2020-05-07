### Date created
This project and README file are created on 5/6/2020.

### Project Title
Bikeshare

### Description
Use Python to understand U.S. bikeshare data. Calculate statistics and build an interactive environment where a user chooses the data and filter for a dataset to analyze.

####
1. Function get_filters
    ######
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    ######
####

####
2. Function load_data
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
####

### Files used
Bikeshare.py

### Credits
https://pandas.pydata.org/pandas-docs/stable/
https://numpy.org/doc/stable/
https://docs.python.org/3/library/
