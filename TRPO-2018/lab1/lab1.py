import datetime

from dateutil.relativedelta import *


def valid_date(iso_date):
    try:
        dto = datetime.datetime.strptime(iso_date, '%Y-%m-%dT%H:%M:%S%z')
        return True
    except:
        print('{} {}\n {:>6} {}'.format('[ERROR]', 'Incorrect date format', ' ',
                                        'Correct date format is YYYY-MM-DDTHH:MM:SS+ZZZZ'))
        return False


def get_dt_object(iso_date):
    datetime_object = datetime.datetime.strptime(iso_date, '%Y-%m-%dT%H:%M:%S%z')
    return datetime_object


def next_day(iso_date):
    nd = get_dt_object(iso_date) + datetime.timedelta(days=1)
    return nd


def next_month(iso_date):
    nm = get_dt_object(iso_date) + relativedelta(months=1)
    return nm


def start_end_weekday(iso_date):
    start = get_dt_object(iso_date) - datetime.timedelta(days=get_dt_object(iso_date).weekday())
    end = start + datetime.timedelta(days=6)
    return start, end


def output(iso_date):
    print('{} {:>16} {}'.format('Today:', ' ', get_dt_object(iso_date)))
    print('{} {:>13} {}'.format('Next day:', ' ', next_day(iso_date)))
    print('{} {:>11} {}'.format('Next month:', ' ', next_month(iso_date)))
    print('{0}{1} {2} \n{3} {4:>5} {5}'.format('Beginning of the week:', ' ', start_end_weekday(iso_date)[0],
                                               'End of the week: ', ' ', start_end_weekday(iso_date)[1]))


def output_in_file(iso_date):
    f = open('output.txt', 'w')
    f.write('{} {:>16} {}\n'.format('Today:', ' ', get_dt_object(iso_date)))
    f.write('{} {:>13} {}\n'.format('Next day:', ' ', next_day(iso_date)))
    f.write('{} {:>11} {}\n'.format('Next month:', ' ', next_month(iso_date)))
    f.write('{0}{1} {2} \n{3} {4:>5} {5}\n'.format('Beginning of the week:', ' ', start_end_weekday(iso_date)[0],
                                                   'End of the week: ', ' ', start_end_weekday(iso_date)[1]))


if __name__ == "__main__":
    value = '2017-12-31T16:59:27+0000'
    if valid_date(value) == True:
        try:
            output(value)
            output_in_file(value)
        except ValueError:
            print('👎')
