import time
import pandas as pd
import numpy as np
import collections as cl
'''The upload of .csv files from source into the editor''' 
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




    #User inputs for the data

    print('Please select the city you like to explorer data ')
    print('A: chicago')
    print('B: new york city')
    print('C: washington')


    # code block for cities

    cities = ['chicago', 'new york city', 'washington']

    while True:
        city = input('Enter a city: ')
        if city.lower() in cities:
            print('Data in city:', city)
            break
        else:
            print('Oopssy, Try again')



    # TO DO: get user input for month (all, january, february, ... , june)

    # code block for month

    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('choose a month from january to june: ')
        if month.lower() in months:
            print('Data in month:', month)
            break
        else:
            print('Ooopppsssy, you need to try again')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    # code block for days of week

    day_of_week = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print('select day of week as: monday,tuesday,...,sunday.')
    while True:
        day = input('Day of week: ')
        if day.lower() in day_of_week:
            print('WOW, you are feeling lucky with', day)
            break
        else:
            print('Hey!!!, NOT QUITE RIGHT, try again')

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    """The following code blocks compute the raw data and also calculate the statistics and describe information on the raw data as well"""

    # code block for the first ten dataset.
    print('Loading.. .. .. .. .. .. .. .. .. .. .. .. .. ... .. .. .. .. . .. .!')
    answer = input('Do you want to see first five dataset? (type: yes or no): ')
    x=0
    while True:
        if answer.lower() == 'yes':
            print(df[x: x + 5])
            x += 5
            answer = input('Do you want to see next five dataset? (type: yes or no): ')

           # print('Loading.....', answer).lower()
        elif answer != 'yes':
            print('no')
            break

    # code block for the full raw dataset.
    data = input('Would you like to see the Full data?(enter: yes or no): ')
    if data == 'yes':
        yes =df
        print('Loading.......', yes)
    elif data != 'yes':
        print('no')
    # code block for the data description.
    descriptions = input('would you care for more statistics description on data? (yes or no): ')
    if descriptions == 'yes':
        yes = df.describe()
        print('Loading....................', yes)
    elif descriptions != 'yes':
        print('no')


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()



    # TO DO: display the most common month

    # code block for common moth

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print('Most common month:', most_common_month)


    # TO DO: display the most common day of week

    # code block for common week

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_common_week_day = df['day_of_week'].mode()[0]
    print('Most common week day:', most_common_week_day)


    # TO DO: display the most common start hour

    # code block for common hour

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()
    print('Most common start hour:', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    #code block for commonly start station

    most_common_start_station = df['Start Station'].mode()[0]
    print('Most common start station:', most_common_start_station)


    # TO DO: display most commonly used end station

    #code block for commonly end station

    most_common_end_station = df['End Station'].mode()[0]
    print('Most common end station:', most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip

    # code block for frequently used start and end station
    frequently_combined_station = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    frequently_combined_station = pd.DataFrame(frequently_combined_station).values.reshape(1)
    print('Frequently Used Start Station and End Station:', frequently_combined_station)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    # code block for total time travelled
    travel_time = np.sum(df['Trip Duration'])
    print('Total travel time:', travel_time)


    # TO DO: display mean travel time

    # code for the average travel time
    mean_travel_time = np.mean(df['Trip Duration'])
    print('Mean travel time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    # code for user types counts
    users = df['User Type'].value_counts()
    print('Number of Users are:', users)


    # TO DO: Display counts of gender

    # code for gender counts
    try:


        gender_count = df['Gender'].fillna('No gender specification:').value_counts()
        print('Total Gender is:', gender_count)
    except:
        print('No data in Gender')



    # TO DO: Display earliest, most recent, and most common year of birth

    # code for common year of birth display
    try:
        el = np.min(df['Birth Year'])
        print('Earliest Birth Year:', el)
        mr = np.max(df['Birth Year'])
        print('Most Recent Birth Year:', mr)
        mc = df['Birth Year'].mode()[0]
        print('Most Common Birth Year:', mc)
    except:
        print('No data in Birth Year')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nI Would love us to explore again with more STYLE, shall we?: yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
