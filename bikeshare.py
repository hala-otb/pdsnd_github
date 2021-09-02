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

    while True:
        city=input('enter which city (new york city, chicago or washington) ').lower()
        if city not in CITY_DATA:
            print('Wrong entry, please choose from (chicago, new york city, washington)')
        else:
             break


    # TO DO: get user input for month (all, january, february, ... , june)

    month=input('enter which month (from january to june) or all for all months ').lower()
    months =['january','february','march','april','may','june']
    while month != 'all' and month not in months:
        month=input('Wrong entry, please choose month from january to june')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('enter which day you want ?').lower()
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while day != 'all' and day not in days:
        day=input('Wrong entry, please enter correct day ')

    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df['month'].mode()[0]
    print(' The most common month; ', most_month)

    # TO DO: display the most common day of week
    most_day = df['day_of_week'].mode()[0]
    print(' The most common day; ', most_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_hour = df['hour'].mode()[0]
    print(' The most common hour; ', most_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_st = df['Start Station'].mode()[0]
    print('The most commonly used start station:', most_start_st)

    # TO DO: display most commonly used end station
    most_end_st = df['End Station'].mode()[0]
    print('The most commonly used end station:', most_end_st)

    # TO DO: display most frequent combination of start station and end station trip
    most_start_end= (df['Start Station'] + 'to' + df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station trip:', most_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time is:', total_time, 'seconds')

    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('The average travel time is:', avg_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print( ' counts of user types is : ', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
      gender_count = df['Gender'].value_counts()
      print('Gender Types:', gender_count)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('earliest year of birth :', df['Birth Year'].min())
        print('most recent year of birth :', df['Birth Year'].max())
        print(' most common year of birth :', df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_display(df):
    raw_display= input('you want see 5 lines of raw data?')
    start_loc= 0
    while raw_display.lower() == 'yes':
        print(df.iloc[start_loc: start_loc+5])
        start_loc +=5
        raw_display= input('you want see next 5 lines of raw data?')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
