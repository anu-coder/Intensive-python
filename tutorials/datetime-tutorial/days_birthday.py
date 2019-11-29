'''
Calculates the days passed before the previous birthday and until next
birthday.
'''
import datetime
import helpers



def main(bday_s):
    tday = datetime.date.today()

    try:
        bday = (datetime.datetime
        .strptime(f'{bday_s} {tday.year}', '%d %B %Y')
        .date()
        )
    except ValueError:
        # Only one case will result in ValueError
        # B'day is 29 Feb
        pass
    else:
        tdelta = tday - bday
        if tdelta.days >= 0:
            prev_bday = bday
            next_bday = helpers.add_relative(prev_bday, years=1)
        else:
            next_bday = bday
            prev_bday = helpers.add_relative(next_bday, years=-1)


        days_after = (tday - prev_bday).days
        days_until = (next_bday - tday).days

    print('Days passed after previous birthday on',
          prev_bday.strftime("%d %B %Y"), ':', days_after)

    print('Days remaining until next birthday on',
           next_bday.strftime("%d %B %Y"), ':', days_until)






if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description=__doc__
    )

    # TODO: Find a way to directly assign an argument to rv of a function
    #       For e.g. list joined to give a str.
    parser.add_argument('-bday',
    help='Birthday in "DD MonthName" format',
    nargs='+')
    bday_s = ' '.join(parser.parse_args().bday)

    main(bday_s)