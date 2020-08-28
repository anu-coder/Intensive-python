'''
Add relative months and years to a datetime.date object
'''
import datetime
import calendar

def last_day_of_month(year: int, month: int)-> int:
    # TODO: Implement this function
    return(calendar.monthrange(year, month)[1])



is_leap = lambda year: year % 4 == 0
is_feb = lambda dtobj: dtobj.month == 2


def add_relative(dtobj: datetime.date, years=None, months=None):

    # TODO: Consideration for days in a month
    # TODO: Consideration for leap years
    # TODO: Make it DRY.
    if years is not None:
        final_year = dtobj.year +  years
        if ((not is_leap(final_year)) and
            (is_feb(dtobj)) and
            (dtobj.day == 29)):

            dtobj = dtobj.replace(day=28).replace(year=final_year)
        else:
            dtobj = dtobj.replace(year=final_year)

    if months is not None:
        final_month = dtobj.month + months
        if final_month <= 12:
            try:
                dtobj = dtobj.replace(month=final_month)
            except ValueError:
                last_day = last_day_of_month(dtobj.year, final_month)
                dtobj = dtobj.replace(day=last_day).replace(month=final_month)
        else:
            years_to_add, final_month = divmod(final_month, 12)
            try:
                dtobj = dtobj.replace(month=final_month)
            except ValueError:
                dtobj = dtobj.replace(day=last_day).replace(month=final_month)

            dtobj = add_relative(dtobj, years=years_to_add)

    return(dtobj)



def main():
    d = datetime.date(2011, 1, 31)
    print(add_relative(d, years=1, months=1))


if __name__ == "__main__":
    main()