def add_time(start, duration, day_name = None) :


    total_minutes = ["%02d" % i for i in range(60)] # For minutes to be displayed
                                                    #in standard format

    # Splitting the start time for required operations
    start_pieces_1 = start.split()
    start_part = start_pieces_1[1]
    start_pieces_2 = start_pieces_1[0].split(':')
    start_hour = start_pieces_2[0]
    start_minute = start_pieces_2[1]
    # print(start_hour, start_minute, start_part)

    # Splitting duration for required operations
    duration_pieces = duration.split(':')
    duration_hour = duration_pieces[0]
    duration_minute = duration_pieces[1]
    total_duration_minutes = (int(duration_hour) * 60) + int(duration_minute)
    # print(duration_hour, duration_minute)

    #Calculating total minutes
    minute = int(start_minute) + int(duration_minute)
    minute_overflow = int(minute / 60) # overflow of minutes above 60 will add
                                       # hours
    new_minute = minute % 60
    # print(minute, minute_overflow, new_minute)

    # Calculating to hours
    hour = int(start_hour) + int(duration_hour) + minute_overflow
    hour_overflow = int(hour / 12) # overflow of hours used for detemining "AM"
                                   # or "PM" setting

    # Keeping hours in 12 hrs format
    if hour % 12 == 0:
        new_hour = 12
    else:
        new_hour = hour % 12
    # print(hour, hour_overflow, new_hour)

    # Calculating settings for "AM" or "PM" based on 'hour_overflow' and
    # calculating number of days passed
    if start_part == 'PM' and hour_overflow % 2 == 1 :
        new_part = 'AM'
        num_of_days = int(total_duration_minutes/(60*24)) + 1 # "+ 1" required
                                        # for accounting of PM to AM transition
    elif start_part == 'PM' and hour_overflow % 2 == 0 :
        new_part = 'PM'
        num_of_days = int(total_duration_minutes/(60*24))

    if start_part == 'AM' and hour_overflow % 2 == 1 :
        new_part = 'PM'
        num_of_days = int(total_duration_minutes/(60*24))
    elif start_part == 'AM' and hour_overflow % 2 ==0 :
        new_part = 'AM'
        num_of_days = int(total_duration_minutes/(60*24))

    # Calling the function for calculating the current day day_name
    new_day_name = calc_day_name(num_of_days, day_name)


    # PRINTING RESULTS
    if day_name is None:
        if num_of_days == 0:
            new_time = str(new_hour) + ':' + total_minutes[new_minute] + ' ' + new_part
            return new_time
        elif num_of_days == 1:
            new_time = str(new_hour) + ':' + total_minutes[new_minute] + ' ' + new_part + ' (next day)'
            return new_time
        elif num_of_days > 1:
            new_time = str(new_hour) + ':' + total_minutes[new_minute] + ' ' + new_part + ' (' + str(num_of_days) + ' days later)'
            return new_time
    else:
        if num_of_days == 0:
            new_time = str(new_hour) + ':' + total_minutes[new_minute] + ' ' + new_part + ', ' + new_day_name[0].capitalize()
            return new_time
        elif num_of_days == 1:
            new_time = str(new_hour) + ':' + total_minutes[new_minute] + ' ' + new_part + ', ' + new_day_name[0].capitalize() + ' (next day)'
            return new_time
        elif num_of_days > 1:
            new_time = str(new_hour) + ':' + total_minutes[new_minute] + ' ' + new_part + ', ' + new_day_name[0].capitalize() + ' (' + str(num_of_days) + ' days later)'
            return new_time




# Function for identifying current day name based on number of days and last
# day
def calc_day_name(num_of_days, day_name ):
    if day_name is not None and len(day_name) > 0 :
        week_days = {'sunday' : 0, 'monday' : 1, 'tuesday' : 2,
        'wednesday' : 3, 'thursday' : 4, 'friday' : 5, 'saturday' : 6}
        x = (week_days[day_name.lower()] + num_of_days) % 7 # getting value of
        # current day to find the key from dictionary
        new_day_name = [i for i in week_days if week_days[i] == x]
        return new_day_name
