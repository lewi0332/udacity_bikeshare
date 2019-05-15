# Programing for Data Science Course

### Explore US Bike Share Data

The project asks to investigate some bikeshare data from 3 .csv files.

There are 4 lines of import. 

pip install -r requirements.txt

(requires pandas 0.23.0)

The CITY_DATA dictionary is built in order to set the file locations of the three datasets. Before running this script, be certain these files are either in the same folder or the full path is listed as the value for each city.

```
import time
import pandas as pd
import numpy as np
from datetime import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': '~washington.csv' }
```

The first function "get_filters()" asks the user for input in the terminal session on how they might want to filter the data.

The end of this function returns 3 varibles to be used in later functions that will build statistics from these variables.

```
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
                month_1 = 'January'
            elif month == "February" or month == "Feb":
                month = "February"
                month_1 = 'February'
            elif month == 'March' or month == "Mar":
                month = 'March'
                month_1 = 'March'
            elif month == 'April' or month == "Apr":
                month = 'April'
                month_1 = 'April'
            elif month == 'May' or month == "May":
                month = 'May'
                month_1 = 'May'
            elif month == 'June' or month == "Jun":
                month = 'June'
                month_1 = 'June'
            elif month == 'All' or month == "A" or month == '':
                month = 'All'
                month_1 = 'All'
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
                day_1 = 'none'
            elif day == "Tuesday" or day == "Tue" or day == "T":
                day = "Tuesday"
                day_1 = 'none'
            elif day == 'Wednesday' or day == "Wed" or day == "W":
                day = 'Wednesday'
                day_1 = 'none'
            elif day == 'Thursday' or day == "Thu" or day == "Th":
                day = 'Thursday'
                day_1 = 'none'
            elif day == 'Friday' or day == "Fri" or day == "F":
                day = 'Friday'
                day_1 = 'none'
            elif day == 'Saturday' or day == "Sat" or day == "Sa":
                    day = 'Saturday'
                    day_1 = 'none'
            elif day == 'Sunday' or day == "Sun" or day == "Su":
                day = 'Sunday'
                day_1 = 'none'
            elif day == 'All' or day == "A" or day == '':
                day = 'All'
                day_1 = "All"
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
```


This next function takes the varibles that just created and uses them as arguments in the funtion. It loads the correct csv file and filters based on the arguments.

This code requires the latest version of pandas: 0.23.0 or higher. I've included a note in the script and a requirements.txt file for pip install.

```
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'All':
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df
```

This was asked in the template. Having converted the columns of hour and month into strings, printing a readable most frequent Month and Day could happen with just one line of code. This works with the version of Pandas from my terminal. For some reason on the udacity web terminal, the month_name function is not found.

However, here is where the code initially broke and took far to long to fix. In looking for the most frequent month, it wasn't correct to print a "frequent month" when it had been filtered to only one month of date. Thus, I had asked for the 'month' variable created in the first get_filters() function. I figured the return statment made the scope global. It did not. I tried to create a second variable that did save outside the function, but that didn't work. I have finally realized that I could add the variable as arguments in the function. This would bring the values into this function and allow me to create an 'if' statement to first check if the user had filtered the month before claiming it was the most frequent.

```
def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel.
    """
    print("\nCalculating The Most Frequent times of travel...\n")
    start_time = time.time()
    # display the most common month
    if month == 'All':
        mode_month = (df['month_name'].mode().iloc[0])
        print("--> The most common month to ride (or the month you selected to filter) was {}.\n\n".format(mode_month))
    else:
        print("--> You have selected to see only the rides that happened in {}.\n\n".format(month))
    # display the most common day of week
    if day == 'All':
        mode_day = (df['day_of_week'].mode().iloc[0])
        print("--> The most common day to ride (or the day you selected to filter) was {}.\n\n".format(mode_day))
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
```

The next function is a fairly straight forward pandas call to those incredibly efficient stats functions to show us the most used stations. However, the request to find the most frequent combination of stations was rather challenging.

There were more complicated ways to bring forward this answer. I started with combining the two columns into a new column and using .value_count(). But, I was worried that might break the dataframe later and it was a bit more complicated. Also, I tried another option of groupby and .size. It worked if I sorted it, and then returned the first index. That was more complicated. I chose the .describe() method and just pulled out the [top] from the resulting dataframe. It's a little slower than the other method, but not by much. It's way more simple to write and read.

```
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
```    

The next function started very easy. Just run some arithmetic. However, back to the desire for user read-ability, I struggled to find a more understandable look at the total time than just thousands of minutes. I found divmod built in function instead of the %. This shouldn't be any slower and looks cleaner in the code (and in the output).

I found inspiration for the divmod function here: https://stackoverflow.com/questions/4048651/python-function-to-convert-seconds-into-minutes-hours-and-days

```
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
```


One of the requirements is to show the breakdown of gender. The .csv for Washington doesn't have a column for gender. So, I need to write an 'if' statement to ask if the city variable is New York or Chicago first.

However, city, month, or day varible from the 'get_filters()' function wasn't passed through. Instead, I chose to ask if a Gender colomn existed in a column first with an 'if' statement. This is better in case another city is added later to the list of .csv files.

Addtionally, I found the to_string() to remove the additional information that .count() outputted. Sadly, the newest version of pandas removed one of the arguments from to_string() that would have fixed the alignment issue that shows up in the terminal (I think). However, removing the header was a win for me. I found the to_string() here: https://stackoverflow.com/questions/40278845/suppress-name-dtype-from-python-pandas-describe

```
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    customers = df.groupby('User Type')['User Type'].count().to_string(header = False)
    print("--> Here is a count of each type of user: \n\n", customers, "\n\n")
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
```    
    
Finally, the rubric requires the script to ask if the user would like to see raw data in groups of 5 rows. The .iloc[] built into Pandas allows for this.

```
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
```
     
Lastly the template included() this main function and asked to create a check whether the user would like to restart the script.

Adding the 'month' & 'day' arguments to the time_stats() function solved my scope issues from earlier.

```
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
```
