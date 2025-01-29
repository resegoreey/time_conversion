#the user inputs the hour(s) they want to convert
hours = int(input("Enter hour(s): "))

#converting hours to minutes
minutes = hours * 60
#converting minutes to seconds
seconds = minutes * 60

#printing the results
print(f"""{hours} hour(s) has:
{minutes} minutes
{seconds} seconds""")