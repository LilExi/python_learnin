import re


def date_parser(text):
    # |\d{2}.\d{2}.\d{2}
    Date = re.findall('\d{4}-\d{2}-\d{2}|\d{2}.\d{2}.\d{4}', text)
    return Date


def date_time_parser(text):
    Date_time = re.findall('\d{4}-\d{2}-\d{2}|\d{2}.\d{2}.\d{4}|\d{2}:\d{2}:\d{2}', text)
    return Date_time


def email_parser(text):
    email = re.findall('[\w\.-]+@[\w\.-]+', text)
    return email


def output(text):
    print('Date: {:>10} {}'.format(' ', date_parser(text)))
    print('Date and time: {:>1} {}'.format(' ', date_time_parser(value)))
    print('Email: {:>9} {}'.format(' ', email_parser(text)))


def output_in_file(text):
    f = open('output.txt', 'w')
    f.write('{} {:>8} [\'{}\']\n'.format('Input: ', ' ', text))
    f.write('Date: {:>10} {}\n'.format(' ', date_parser(text)))
    f.write('Date and time: {:>1} {}\n'.format(' ', date_time_parser(value)))
    f.write('Email: {:>9} {}\n'.format(' ', email_parser(text)))


if __name__ == "__main__":
    value = "some text 1999-12-01 31.01.2009 with time 13:30:00 and email test@gmail.com"
    date_parser(value)
    output(value)
    output_in_file(value)
