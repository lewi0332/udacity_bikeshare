Hi Reviewer!

Thank you for the thought feedback and catching my errors.

Of the two issues that needed to be revised:

The first revision asked me to use the 'int' method of sorting the month column
in the DataFrame. I realized that The method I used in the script .month_name()
works only on pandas versions 0.23.0 and above. I tested the web terminal on the
udacity site to find it running pandas 0.18.0. I was able to upgrade the pandas
in that user environment and the original script is working. Thus, I have left a
version of the script in my submission with this code in it and a requirements.txt
file to be installed by the user. I like this code as it is cleaner and allows
for greater flexibility in the future.

I have also created a second version of the script that uses the 'int' method
you suggested. I've added this in a separate folder marked ".downgraded". Just
in case it is required in the rubric to use an older version of pandas.

Regarding the second revision you asked of the get_filters() function,
both scripts have been revised. That change is far better for the user. Thanks
for the suggestion!

-Derrick
