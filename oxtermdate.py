#!/usr/bin/python

import datetime, math, os, re, sys

df = '%Y-%m-%d'
weekdays = ['Su', 'M', 'Tu', 'W', 'Th', 'F', 'Sa']

def parse_date(s):
    return datetime.datetime.strptime(s, df)

def format_date(d):
    return d.strftime(df)

def actual_date(start, weekday, week):
    day_offset = weekdays.index(weekday)
    return start + datetime.timedelta(days=day_offset, weeks=week-1)

def term_date(start, date):
    diff = (date - start).days
    week = (diff // 7) + 1
    weekday = date.strftime('%A')
    return (week, weekday)

def ordinal(n):
    # From http://stackoverflow.com/a/20007730
    a = abs(n)
    return "%d%s" % (n,"tsnrhtdd"[(math.floor(a/10)%10!=1)*(a%10<4)*a%10::4])

start_date = parse_date(os.environ['OXFORD_TERM_START'])

if len(sys.argv) > 1:
    arg = sys.argv[1]
    date_match = re.match("([0-9]{4})-([0-9]{2})-([0-9]{2})", arg)
    ox_match = re.match("(Su|M|Tu|W|Th|F|Sa)([0-9].*)", arg)
    if date_match:
        week, weekday = term_date(start_date, parse_date(arg))
        print(weekday + " of " + ordinal(week) + " week")
    elif ox_match:
        weekday = ox_match.group(1)
        week = int(ox_match.group(2))
        print(format_date(actual_date(start_date, weekday, week)))
    else:
        sys.exit(1)
else:
    sys.exit(1)
