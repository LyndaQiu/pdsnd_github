import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Which city are you interested to explor: Chicago, New York City or Washington?")
    city = city.strip().lower()
    while (city != 'chicago' and city != 'new york city' and city != 'washington'):
        city = input ("Please input one of these three cities: Chicago, New York City or Washington:")
        city = city.strip().lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month are you interested to explor: all, January, February, March, April, May, June?")
    month = month.strip().lower()
    while (month != 'all' and month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month != 'june'):
        month = input ("Please input one of these month choices: all, January, February, March, April, May, June:")
        month = month.strip().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which week day are you interested to explor: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday?")
    day = day.strip().lower()
    while (day != 'all' and day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday'):
        day = input ("Please input one of these day choices: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday:")
        day = day.strip().lower()

    print('-'*40)
    return city.strip().replace(' ', '_'), month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print("input city={}, month={}, day={}".format(city, month, day))

    df = pd.read_csv(city + '.csv')

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    print('Finish loading data...')
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    if (df['month'].mode()[0] <= 6):
        most_common_month = months[df['month'].mode()[0] - 1]
        print ('\nThe most common month is: {}\n'.format(most_common_month))
    else:
        print ('\nThere is no most common month.\n')

    # TO DO: display the most common day of week
    print ('\nThe most common day of week is: {}\n'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print ('\nThe most common start hour is: {}\n'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print ('\nThe most commonly used start station is: {}\n'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print ('\nThe most commonly used end station is: {}\n'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    # Combine 'Start Station' and 'End Station' to be a combined column, the text is separated by '#'
    df['comb_station'] = df['Start Station'] + "#" + df['End Station']
    most_freq_comb_station = df['comb_station'].mode()[0]
    stations = most_freq_comb_station.split('#')

    print ('\nThe most frequent combination of start station and end station trip is from "{}" to "{}".\n'.format(stations[0], stations[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_seconds = df['Trip Duration'].sum()
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)
    print ('\nTotal travel time is {} years, {} days, {} hours, {} minutes, {} seconds\n'.format(years, days, hours, minutes, seconds))

    # TO DO: display mean travel time
    print ('\nMean travel time is {} seconds\n'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        print('\nCounts of user types:\n')
        print(df['User Type'].value_counts())
    else:
        print('\nThere"s no User Types column.\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('\nCounts of gender:\n')
        print(df['Gender'].value_counts())
    else:
        print('\nThere"s no Gender column.\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        min_year = int(df['Birth Year'].min())
        max_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print('\nEarliest year of birth is: {}'.format(min_year))
        print('\nMost recent year of birth is: {}'.format(max_year))
        print('\nMost common year of birth is: {}'.format(most_common_year))
    else:
        print('\nThere"s no Birth Year column.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """
    Displays raw data until user wants to discontine
    Display 5 lines of raw data at a time.
    """
    show_rawdata = input("Do you want to see raw data: Yes or No?")
    show_rawdata = show_rawdata.strip().lower()
    while (show_rawdata != 'yes' and show_rawdata != 'no'):
        show_rawdata = input("Do you want to see raw data: Yes or No?")
        show_rawdata = show_rawdata.strip().lower()

    while(show_rawdata == 'yes'):
        print(df.iloc[0:5])
        show_rawdata = input("Do you want to see more 5 lines of raw data: Yes or No?")
        show_rawdata = show_rawdata.strip().lower()
        print('-'*40)

def main():
    """
    Main function loop will keep analysis until the user likes to restart.
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
