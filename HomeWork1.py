from datetime import date, datetime, timedelta


def get_days_from_today(date):
    try:
        time_now = datetime.today()
        time_now1 = time_now.date()
        #print(time_now1)
        date_object = datetime.strptime(date, "%Y-%m-%d").date()
        #print(date_object)
        diff_time = time_now1 - date_object
        #print(diff_time.days)
        return diff_time.days
    except ValueError:
        print("Not right value! Try 'YYYY-MM-DD'")
get_days_from_today("2010-11-1")



