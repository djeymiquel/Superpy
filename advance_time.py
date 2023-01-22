from my_lib2 import *

# Advance Time
def advanced_time(num: int):
    with open("files/current_date.txt", "r") as time_file:
        current_time = datetime.strptime(time_file.read(), "%Y/%m/%d")
    # Advance the time by the specified number of days
        new_time = current_time + timedelta(days=num)
    with open("files/current_date.txt", "w") as time_file:
        time_file.write(new_time.strftime("%Y/%m/%d"))
    console.print("OK", style='green')
    
    

    

