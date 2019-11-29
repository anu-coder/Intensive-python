# Grading scores
# Take the following into consideration:
# Grade is 'Excellent' if score is greater than or equal to 75.
# Grade is 'Very good' if score is greater than or equal to 60.
# Grade is 'Good' if score is greater than or equal to 50.
# Grade is 'Not bad' if score is greater than or equal to 40.
# Grade is 'Bad' if score is greater than or equal to 30.
# Grade is 'Horrible' if score is greater than or equal to 20.
# Grade is 'Appalling' if score is below 20.

from collections import OrderedDict as OD


def get_report_card(name, score):
    """ Return a report card with name, score, and grade based on score.

    >>> get_report_card('Bob', 80)
    >>> OrderedDict([('Name', 'Bob'), ('Score', 80), ('Grade', 'Excellent')])
    """

    # TODO: Parse it from a file, or a string
    #       Also look into string as a file-like object.
    grade_dict = {75: 'Excellent',
                  60: 'Very good',
                  50: 'Good',
                  40: 'Not bad',
                  30: 'Bad',
                  20: 'Horrible'}

    break_executed = False
    for thresh, grade in grade_dict.items():
        if score >= thresh:
            break_executed = True
            break

    if not break_executed:
        grade = 'Appalling'

    res = OD(Name=name, Score=score, Grade=grade)

    return(res)





def main():
    res = get_report_card('Joe', 55)
    print(res)
    for k, v in res.items():
        print("{}: {}".format(k, v))

if __name__ == "__main__":
    main()
