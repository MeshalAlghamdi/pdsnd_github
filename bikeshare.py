import time, sys
import pandas as pd
import numpy as np
#-----------------------------------------------------------------
"""
Read data from data files for analysis
"""
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

#------------------------City Filters Section--------------------------

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print("\n\n *^* Exploring chicago, new york city and washington bikeshare data! *^*\n")
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input ("\nType a city name (new york, chicago, washington) OR (Exit) to close the Program\n\n").lower()
        if city not in ('new york', 'chicago', 'washington', 'exit'):
            print("\nInvalid Input! \n")
            continue
        else:
            if city == 'exit':
                print("Exiting! Have a good day")
                sys.exit()
            break
            

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nType a month (January, Fepruary, March, April, May, June) Or All OR (Exit) to close the Program \n\n").lower()
        if month not in('january','fepruary','march','april','may','june','all','exit'):
           print("\nInvalid Input! \n")
           continue
        else:
            if month == 'exit':
                print("Exiting! Have a good day")
                sys.exit()
            break
                

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nType a day (Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday) Or All OR (Exit) to close the Program\n\n").lower()
        if day not in('saturday','sunday','monday','tuesday','wednesday','thursday','friday','all','exit'):
            print("\nInvalid Input! \n")
            continue
        else:
            if day == 'exit':
                print("Exiting! Have a good day")
                sys.exit()
            break
            

    print('-'*40)
    return city, month, day

#-----------------------------End------------------------------
#-----------------------------Statics Section--------------------------

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most Common Month:", most_common_month)


    # TO DO: display the most common day of week
    Most_Common_day = df['day_of_week'].mode()[0]
    print("Most Common day:", Most_Common_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Most_Common_Hour = df['hour'].mode()[0]
    print("Most Common Hour:", Most_Common_Hour)


    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)

#-------------------------------End-------------------------------
#-----------------------------------------------------------------
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print("Total travel time:", round(total_travel_time/86400), " Days")


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time:", int(round(mean_travel_time/60)), " Minutes")


    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)

#-----------------------------------------------------------------

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    
    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Type:\n', gender_types)
    except KeyError:
      print("\nGender Type:\nNo data available for this month.")

    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest = df['Birth Year'].min()
      print('\nEarliest Year:', int(earliest))
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Recent = df['Birth Year'].max()
      print('\nMost Recent Year:', int(Recent))
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Common = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', int(Common))
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)
    
#-----------------------------------------------------------------

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)


    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip
	df['Most Common Trip'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    most_common_trip = df['Most Common Trip'].mode()[0]
    print("\nMost Common Trip:",most_common_trip)
    
    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)
       
#-----------------------------------------------------------------

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
    # load data into dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Load the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Create extra columns for month and day of the week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filtering by month
    if month.lower() != 'all':
   	# Get an int from month index
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # create the new dataframe for the month
        df = df[df['month'] == month]

    # filtering by day of week
    if day.lower() != 'all':
    # create the new dataframe for the day of the week
        df = df[df['day_of_week'] == day.title()]


    return df

#-----------------------------------------------------------------

def display_raw_data(df):
    print("\n\n *^* Displaying Raw Data! *^*\n")
    show_rows = 5
    rows_start = 0
    rows_end = show_rows - 1 
    raw_data = input('\nDisplay Raw Data? yes or no OR Exit to close the Program \n').lower()
    if raw_data == 'exit':
                print("Exiting! Have a good day")
                sys.exit()
    elif raw_data.lower() == 'yes':
        city = input('\nType a city name (new york, chicago, washington) OR (Exit) to close the Program\n\n').lower()
        if city == 'exit':
                print("Exiting! Have a good day")
                sys.exit()
        df = pd.read_csv(CITY_DATA[city])

    while True:
        if raw_data.lower() == 'yes':
            # display 5 rows at a time
            print('\nDisplaying rows ',(rows_start ) ," to ", (rows_end ))
            print('\n', df.iloc[rows_start : rows_end + 1])
            rows_start += show_rows
            rows_end += show_rows
            print('.'*90)
            raw_data = input('\nWould you like to see the next 5 rows? yes or no OR Exit to close the Program\n').lower()
            if raw_data == 'exit':
                print("Exiting! Have a good day")
                sys.exit()
            continue
        else:
            print("** Awesome **")
            break

def main():
    print('\nHello! Let\'s explore chicago, new york city and washington bikeshare data!')
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while restart not in('yes','no'):
            print("\nInvalid Input")
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
            if restart == 'no':
                print("Exiting! Have a good day")
                sys.exit()
            elif restart == 'yes':
                 break
            else:
                continue
            


if __name__ == "__main__":
    main()
