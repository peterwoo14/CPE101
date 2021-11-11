"""
CPE 101
Section 6
Project 4
Pete Woo
pswoo@calpoly.edu
"""


import sys
import copy


class Crime:
    """ This Class represents Crime object
    Attributes:
        crime_id(int): ID number corresponding to logged crime
        category(str): category of crime committed
        day_of_week(str/None): day of week crime occurred
        month(str/None): month of year crime occurred
        hour(str):  hour of day crime occurred
    """
    def __init__(self, crime_id:int, category:str, day_of_week:str = None, month:str = None, hour:str = None):
        self.crime_id = crime_id
        self.category = category
        self.day_of_week = day_of_week
        self.month = month
        self.hour = hour

    def __eq__(self, other):
        return isinstance(other, Crime) and self.crime_id == other.crime_id

    def __repr__(self):
        return '{}\t{}\t{}\t{}\t{}\n'.format(self.crime_id, self.category, self.day_of_week, self.month, self.hour)


def create_crimes(lines:list)->list:
    """ This function finds each unique ROBBERY found in crimes.tsv and return a list of these Crime objects
    Args:
        lines(list): list of strings, each a line read from crimes.tsv
    Returns:
        list: list of Crime objects, one for each unique ROBBERY found
    """
    size = len(lines)
    crimes, crime_ids = [], []
    row, start = 0, 0
    for i in range(size):
        string = lines[row]
        stop = string.find('\t')
        crime_id = string[start:stop]
        start += (len(crime_id) + 1)
        stop = string.find('\t', start)
        category = string[start:stop]
        if category == 'ROBBERY':
            copy = False
            for i in range(len(crime_ids)):
                if crime_id == crime_ids[i]:
                    copy = True
                i += 1
            if copy:
                continue
            crime = Crime(int(crime_id), category)
            crime_ids.append(crime_id)
            crimes.append(crime)
        row += 1
        start = 0
    return crimes

def sort_crimes(crimes:list)->None:
    """ This function sorts a list of crimes by ID numbers using selection sort (muatates existing input Crime list)
    Args:
        crimes(list): list of Crime objects to be sorted
    """
    size = len(crimes)
    for i in reversed(range(1, size)):
        max_id = 0
        for j in range(1, i + 1):
            test_crime, control_crime = crimes[j], crimes[max_id]
            test_id, control_id = test_crime.crime_id, control_crime.crime_id
            if test_id > control_id:
                max_id = j
        crimes[max_id], crimes[i] = crimes[i], crimes[max_id]


def set_crimetime(crime:Crime, day_of_week:str, month:int, hour:int)->Crime:
    """ This function updates the day of week, month, and hour attributes of a Crime object
    Args:
        crime(Crime): Crime object without updated attributes
        day_of_week(str): day of week crime occurred
        month(int): integer between 1 and 12 corresponding to month crime occurred
        hour(int): integer between 0 and 23 corresponding to hour crim occurred
    Returns:
        Crime: Crime object with updated attributes
    """
    new_crime = copy.copy(crime)
    new_crime.day_of_week = day_of_week
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    new_crime.month = months[month - 1]
    hours = ['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM']
    new_crime.hour = hours[hour]
    return new_crime


def find_crime(crimes:list, crime_id:int)->int:
    """ This function returns a Crime object from a list of crimes using the crime ID and binary search
    Args:
        crimes(list): list of Crime objects to be searched
        crime_id(int): ID number corresponding to the ID of the Crime object to be returned
    Returns:
        int: the index of the Crime object in crimes with the particular crime_id (-1 if Crime object not found)
    """
    low, high = 0, len(crimes) - 1
    while low <= high:
        mid = (low + high) // 2
        test_crime = crimes[mid]
        test_id = test_crime.crime_id
        if test_id == crime_id:
            return mid
        if crime_id < test_id:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def update_crimes(crimes:list, lines:list)->None:
    """ This function updates attributes of all Crime objects in a list (mutates exisiting input Crime list)
    Args:
        crimes(list): list of Crime objects to be updated
        lines(list): list containing time information for each Crime to be used for updating
    """
    size = len(lines)
    row = 0
    for i in range(size):
        start = 0
        string = lines[row]
        end = string.find('\t')
        crime_id = int(string[start:end])
        crime_index = find_crime(crimes, crime_id)
        crime = crimes[crime_index]
        if crime_index != -1:
            start += (len(str(crime_id)) + 1)
            end = string.find('\t', start)
            day_of_week = string[start:end]
            start += (len(day_of_week) + 1)
            end = string.find('/', start)
            month = int(string[start:end])
            start += 11
            end = string.find(':', start)
            hour = int(string[start:end])
            new_crime = set_crimetime(crime, day_of_week, month, hour)
            crimes[crime_index] = new_crime
        row += 1

def most_robbed_day(crimes:list)->str:
    """ This function finds the day with the most robberies
    Args:
        crimes(list): list of Crime objects to be searched
    Returns:
        str: day with most robberies
    """
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_count = [0, 0, 0, 0, 0, 0, 0]
    size = len(crimes)
    i = 0
    for i in range(size):
        crime = crimes[i]
        day = crime.day_of_week
        day_index = days.index(day)
        day_count[day_index] += 1
        i += 1
    day_with_most = days[day_count.index(max(day_count))]
    return day_with_most

def most_robbed_hour(crimes:list)->str:
    """ This function finds the hour with the most robberies
    Args:
        crimes(list): list of Crime objects to be searched
    Returns:
        str: hour with the most robberies
    """
    hours = ['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM']
    hour_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    size = len(crimes)
    i = 0
    for i in range(size):
        crime = crimes[i]
        hour = crime.hour
        hour_index = hours.index(hour)
        hour_count[hour_index] += 1
        i += 1
    hour_with_most = hours[hour_count.index(max(hour_count))]
    return hour_with_most

def most_robbed_month(crimes:list)->str:
    """ This function finds the month with the most robberies
    Args:
        crimes(list): list of Crime objects to be searched
    Returns:
        str: month with most robberies
    """
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    size = len(crimes)
    i = 0
    for i in range(size):
        crime = crimes[i]
        month = crime.month
        month_index = months.index(month)
        month_count[month_index] += 1
        i += 1
    month_with_most = months[month_count.index(max(month_count))]
    return month_with_most

def main():
    """ This function executes the main program.

    """
    crime_file, time_file = sys.argv[1], sys.argv[2]
    with open(crime_file, 'r') as crimef:
        crime_lines = crimef.readlines()
        crime_lines = crime_lines[1:]
    with open(time_file, 'r') as timef:
        time_lines = timef.readlines()
        time_lines = time_lines[1:]
    crimes = create_crimes(crime_lines)
    sort_crimes(crimes)
    update_crimes(crimes, time_lines)
    with open('robberies.tsv', 'w') as outf:
        size = len(crimes)
        outf.write('ID\tCategory\tDayOfWeek\tMonth\tHour\n')
        i = 0
        for i in range(size):
            string = str(crimes[i])
            outf.write(string)
            i += 1
    num_robberies, day_with_most, month_with_most, hour_with_most = len(crimes), most_robbed_day(crimes), most_robbed_month(crimes), most_robbed_hour(crimes)
    stats = 'NUMBER OF PROCESSED ROBBERIES: {}\nDAY WITH MOST ROBBERIES: {}\nMONTH WITH MOST ROBBERIES: {}\nHOUR WITH MOST ROBBERIES: {}'
    print(stats.format(num_robberies, day_with_most, month_with_most, hour_with_most))


if __name__ == '__main__':
    main()

