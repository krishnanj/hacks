import datetime as dt

bday = [1995, 6, 8, 17, 30, 0]

# Define the birth date
birth_date = dt.datetime(bday[0], bday[1], bday[2], bday[3], bday[4], bday[5])

# List of labels corresponding to the powers of 10
labels = [
    "1 second", "10 seconds", "100 seconds", "1,000 seconds", "10,000 seconds",
    "100,000 seconds", "1 million seconds", "10 million seconds", "100 million seconds", "1 billion seconds"
]

for i in range(0, 10):
    # Calculate the time delta in seconds
    time_delta = 10 ** i
    
    # Add the time delta to the birth date
    new_date = birth_date + dt.timedelta(seconds=time_delta)
    
    # Print the result
    print(f"You will reach {labels[i]} at exactly:")
    print(new_date)
