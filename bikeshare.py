import time
import pandas as pd
import numpy as np
import datetime as dt

"""
Requires pandas0.23.0 or higher
pip install -r requirements.txt
"""

CITY_DATA = { 'chicago': 'chicago_copy.csv',
              'new york city': '~/documents/flatiron/python_practice/new_york_city.csv',
              'washington': '~/documents/flatiron/python_practice/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("\n\nHello! Let\'s explore some US bikeshare data!")

    # get user input for city (chicago, new york city, washington)
    while True:
        try:
            city = input("\n\nWhich city would you like view: \n\n(C)hicago, (N)ew York or (W)ashington\n\n: ").lower().strip()
            if city == "chicago" or city == "c":
                city = "chicago"
                city_1 ="chicago"
            elif city == "new york" or city == "n":
                city = "new york city"
                city_1 = "new york city"
            elif city == 'washington' or city == "w":
                city = 'washington'
                city_1 = 'washington'
            else :
                print("-"*40)
                print("\nSorry, I didn't recognize that. \n\nI wish every city had bike share"
                      " available. \n\nFor now I can only show you data from:"
                      "\n(C)hicago, (N)ew York, or (W)ashington. \n\nLet's give it another try.\n\n")
                print("-"*40)
                city = input("\n\nWhich city would you like view: \n\n(C)hicago, (N)ew York or (W)ashington\n\n: ").lower().strip()

    # get user input for month
            month = input("\n\nI love that place. \n\nNow what month would you like to look at?\n\n"
                         "You can input 'all' or a specific month: January, February, "
                         "March, April, May, or June?\n\n: ").title().strip()
            if month == "January" or month == "Jan":
                month = "January"
            elif month == "February" or month == "Feb":
                month = "February"
            elif month == 'March' or month == "Mar":
                month = 'March'
            elif month == 'April' or month == "Apr":
                month = 'April'
            elif month == 'May' or month == "May":
                month = 'May'
            elif month == 'June' or month == "Jun":
                month = 'June'
            elif month == 'All' or month == "A" or month == '':
                month = 'All'
            else :
                print("-"*40)
                print("\nSorry, I didn't recognize that. \n\nWe only have those first 6 "
                      "months of data available. \n\nFor now, I can show you data from:"
                      "\nJanuary, February, March, Aril, May, or June \n\nLet's give it another try.")
                print("-"*40)
                month = input("\n\nNow what month would you like to look at?\n\n"
                         "You can input 'all' or a specific month: January, February, "
                         "March, April, May, or June?\n\n: ").title().strip()

    #Now ask for input to select the Day to filter

            day = input("\n\nWould you like to see all the results or only certain days of the week?\n\n"
                "Or, you can just input 'all' to see everything.\n\n"
                "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All\n\n: ").title().strip()
            if day == "Monday" or day == "Mon" or day == "M":
                day = "Monday"
            elif day == "Tuesday" or day == "Tue" or day == "T":
                day = "Tuesday"
            elif day == 'Wednesday' or day == "Wed" or day == "W":
                day = 'Wednesday'
            elif day == 'Thursday' or day == "Thu" or day == "Th":
                day = 'Thursday'
            elif day == 'Friday' or day == "Fri" or day == "F":
                day = 'Friday'
            elif day == 'Saturday' or day == "Sat" or day == "Sa":
                day = 'Saturday'
            elif day == 'Sunday' or day == "Sun" or day == "Su":
                day = 'Sunday'
            elif day == 'All' or day == "A" or day == '':
                day = 'All'
            else:
                print("-"*40)
                print("\nSorry, I didn't recognize that. \n\nThe Beatles weren't being literal"
                      " about those 8 days a week.\n\nFor now, I can show you data from:"
                      "\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday \n\nLet's give it another try.")
                print("-"*40)
                day = input("\n\nWould you like to see all the results or only certain days of the week?\n\n"
                "Or, you can just input 'all' to see everything.\n\n"
                "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All\n\n: ").title().strip()
        except ValueError:
            print ("\nSorry, I didn't understand that.\n")
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month_name'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        #months = ['January', 'February', 'March', 'April', 'May', 'June']
        #month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month_name'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]


    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel.
    !!! Need to solve "all" problem. If I've filtered month, it should not print 'common month'. """

    print("\nCalculating The Most Frequent times of travel...\n")
    start_time = time.time()

    # display the most common month
    if month == 'All':
        mode_month = (df['month_name'].mode().iloc[0])
        print("--> The most common month to ride was {}.\n\n".format(mode_month))
    else:
        print("--> You have selected to see only the rides that happened in {}.\n\n".format(month))

    # display the most common day of week
    if day == 'All':
        mode_day = (df['day_of_week'].mode().iloc[0])
        print("--> The most common day to ride was {}.\n\n".format(mode_day))
    else:
        print("--> You have selected to see only the rides that happened on {}s. \n\n".format(day))

    # display the most common start hour
    mode_hour = df['Start Time'].dt.hour.mode()
    mode_hour = int(mode_hour)
    if mode_hour == 0:
        am_pm = 'am'
        twelve_hour = 12
    elif 1 <= mode_hour < 13:
        am_pm = 'am'
        twelve_hour = mode_hour
    elif 13 <= mode_hour < 24:
        am_pm = 'pm'
        twelve_hour = mode_hour - 12
    print('--> The most common start hour is {}:00{}.\n\n'.format(twelve_hour, am_pm))

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start = df['Start Station'].mode().iloc[0]
    print("--> The most commonly used station to start a ride was: {}.\n\n".format(start))


    # display most commonly used end station
    finish = df['End Station'].mode().iloc[0]
    print("--> The most commonly used station to end a ride was: {}.\n\n".format(finish))


    # display most frequent combination of start station and end station trip
    combo = df['Start Station'] + ' to ' + df['End Station']
    print("--> The most popular combination of stations to start and end a ride was: {}.\n\n".format(combo.describe()['top']))


    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df['Trip Duration'].sum()
    minute, second = divmod(total, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 60)
    week, day = divmod(day, 7)
    year, week = divmod(week, 52)
    print("--> The total time these users spent on bikes was {} year(s), {} weeks, {} days, {} hours, {} minutes and {}"
          " seconds.\n\n".format(year, week, day, hour, minute, second))

    # display mean travel time
    ave = round(df['Trip Duration'].mean())
    minute, second = divmod(ave, 60)
    hour, minute = divmod(minute, 60)
    print("--> The average time these users spent on bikes was {} hour(s), {} minutes and {}"
          " seconds.\n\n".format(hour, minute, second))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    customers = df.groupby('User Type')['User Type'].count().to_string(header = False)
    print("--> Here is a count of each ride by user type: \n\n", customers, "\n\n")


    # Display counts of gender
    if "Gender" in df.columns:
        gender = df.groupby('Gender')['Gender'].count().to_string(header = False)
        print("--> Here is a count of the users by gender: \n\n", gender, "\n\n")
    else:
        print("--> The data from this city did not include gender\n\n")

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        old = df['Birth Year'].min()
        print("--> Our oldest rider was born in: ", int(old), "\n\n")

        young = df['Birth Year'].max()
        print("--> Our youngest rider was born in: ", int(young), "\n\n")

        middle = df['Birth Year'].mode()
        print("--> Our most common rider was born in: ", int(middle), "\n\n")
    else:
        print("--> The data from this city did not include age.\n\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df, start):
    '''Raw data is displayed upon request by the user in this manner:
    Script should prompt the user if they want to see 5 lines of raw data,
    display that data if the answer is 'yes', and continue these prompts and
    displays until the user says 'no
    '''
    raw = input("\nWould you like to view individual trip data?\n"
                "(Y)es or (N)o: ")
    raw = raw.lower()
    while True:
        if raw == 'yes' or raw == 'y':
            print(df.iloc[start:start+5])
            start += 5
            return display_data(df, start)
        elif raw == 'no' or raw == 'n':
            return
        else:
            print("\nI know, it's a lot. Just say no if it's too boring.")
            return display_data(df, start)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df, 0)

        restart = input("\nWould you like to restart?\n(Y)es or (N)o: ")
        while restart.lower() not in ['yes', 'no', 'y', 'n']:
            print("Invalid input. Please type 'yes' or 'no'.")
            restart = input("\nWould you like to restart?\n(Y)es or (N)o: ")
        if restart.lower() == 'yes' or restart.lower() == 'y':
            main()
        elif restart.lower() == 'no' or restart.lower() == 'n':
            break


if __name__ == "__main__":
	main()
