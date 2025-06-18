import datetime

# str to date
datetime.datetime.strptime('2024/12/15','%Y/%m/%d')

# add 7 days
date_old=datetime.datetime(2024, 12, 15, 0, 0)
date_new=date_old+datetime.timedelta(days=7)
date_new

# date to str
datetime.datetime.strftime(date_new,'%B %d,%Y')
