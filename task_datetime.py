# -*- coding: utf-8 -*-
from datetime import datetime

# Determine the current date and time, add 1 day to it
data_time_now = datetime.now()

# add to it 1 day
the_next_day = data_time_now.day + 1

# Convert it to a string in the format (DD-MM-YYYY HH:SS)
convert_datetime = data_time_now.strftime("%d-%m-%Y, %H:%S")

# Create a string variable with the date ‘2020-02-03 09:18:36.000’ and convert it to datetime format
my_date = "2020-02-03 09:18:36.000"
convert_date_from_string = datetime.strptime(my_date, '%Y-%m-%d %H:%M:%S.%f')

# day
my_day = convert_date_from_string.strftime("%d")

# month
my_month = convert_date_from_string.strftime("%m")

# year
my_year = convert_date_from_string.strftime("%Y")

# time
my_time = convert_date_from_string.strftime("%H")

# seconds
my_seconds = convert_date_from_string.strftime("%S")


if __name__ == "__main__":
    print(f"Текущая дата и время {data_time_now}")
    print(f"Завтра будет {the_next_day} число")
    print(f"Дата, время, секунды: {convert_datetime}")
    print("------------------")
    print(f"День: {my_day}")
    print(f"Месяц: {my_month}")
    print(f"Год: {my_year}")
    print(f"Часы: {my_time}")
    print(f"Cекунды: {my_seconds}")
    print("------------------")


