from datetime import datetime, timedelta

class DateHelper:
    
    def date_today(self):
        with open("files/current_date.txt", "r") as file:
            current_date_string = file.read().strip()
        return datetime.strptime(current_date_string, "%Y/%m/%d").date()

    def yesterday(self):
        today = self.date_today()
        return today - timedelta(days=1)

    def exp_date(self, exp_date: str):
        x =(datetime.strptime(exp_date, '%Y-%m-%d'))
        return x.strftime('%Y-%m-%d')
        
    def date_string(self,date:str):
        x=datetime.strptime(date, '%Y-%m')
        return x.strftime('%B %Y')
     
my_date = DateHelper()
today = my_date.date_today()
yesterday = my_date.yesterday()



