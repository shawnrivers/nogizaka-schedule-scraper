import urllib.request as r
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
import sys

# Weekday
weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Handle system paramaters.

# If there are no paramaters, ouput the schedule of today.
if len(sys.argv) > 1:
    input_datetime = str(sys.argv[1])
    if input_datetime == 'tomorrow' or input_datetime == 'tom':
        # Get tomorrow.
        tomorrow_datetime = date.today() + timedelta(days=1)
        year = tomorrow_datetime.year
        month = '%02d' % tomorrow_datetime.month
        day = '%02d' % tomorrow_datetime.day
        weekday_num = tomorrow_datetime.weekday()
    elif input_datetime == 'today' or input_datetime == 'tod':
        # Get today.
        current_datetime = date.today()
        year = current_datetime.year
        month = '%02d' % current_datetime.month
        day = '%02d' % current_datetime.day
        weekday_num = current_datetime.weekday()
    elif input_datetime != '':
        input_datetime_splitted = input_datetime.split('-')
        year = input_datetime_splitted[0]
        month = input_datetime_splitted[1]
        day = input_datetime_splitted[2]
        weekday_num = datetime.strptime(input_datetime, '%Y-%m-%d').weekday()
    else:
        # Get today.
        current_datetime = date.today()
        year = current_datetime.year
        month = '%02d' % current_datetime.month
        day = '%02d' % current_datetime.day
        weekday_num = current_datetime.weekday()
else:
    # Get today.
    current_datetime = date.today()
    year = current_datetime.year
    month = '%02d' % current_datetime.month
    day = '%02d' % current_datetime.day
    weekday_num = current_datetime.weekday()


# Set up HTTP request.
url = 'http://www.nogizaka46.com/schedule/?to={}{}'.format(year, month)
req = r.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
raw_html = r.urlopen(req).read()

schedule_id = 'd' + str(day)

# Fetch schedules.
soup = BeautifulSoup(raw_html, 'html.parser')

day_schedules = soup.find(id=schedule_id)

live_schedules = day_schedules.find_all('a', class_='live')
handshake_schedules = day_schedules.find_all('a', class_='handshake')
tv_schedules = day_schedules.find_all('a', class_='tv')
radio_schedules = day_schedules.find_all('a', class_='radio')
magazine_schedules = day_schedules.find_all('a', class_='magazine')
web_schedules = day_schedules.find_all('a', class_='web')
movie_schedules = day_schedules.find_all('a', class_='movie')
theatre_schedules = day_schedules.find_all('a', class_='theatre')
release_schedules = day_schedules.find_all('a', class_='release')
bd_schedules = day_schedules.find_all('a', class_='bd')

# Print results to the command line.
print('\nSchedules of {}-{}-{} ({}):'.format(year,
                                             month, day, weekday[weekday_num]))

if (len(bd_schedules) > 0):
    print('\nBirthday:')
    for bd_schedule in bd_schedules:
        print(' ', bd_schedule.string)

if (len(live_schedules) > 0):
    print('\nLive:')
    for live_schedule in live_schedules:
        print(' ', live_schedule.string)

if (len(handshake_schedules) > 0):
    print('\nHandshake:')
    for handshake_schedule in handshake_schedules:
        print(' ', handshake_schedule.string)

if (len(tv_schedules) > 0):
    print('\nTV:')
    for tv_schedule in tv_schedules:
        print(' ', tv_schedule.string)

if (len(radio_schedules) > 0):
    print('\nRadio:')
    for radio_schedule in radio_schedules:
        print(' ', radio_schedule.string)

if (len(magazine_schedules) > 0):
    print('\nMagazine:')
    for magazine_schedule in magazine_schedules:
        print(' ', magazine_schedule.string)

if (len(web_schedules) > 0):
    print('\nWeb:')
    for web_schedule in web_schedules:
        print(' ', web_schedule.string)

if (len(movie_schedules) > 0):
    print('\nMovie:')
    for movie_schedule in movie_schedules:
        print(' ', movie_schedule.string)

if (len(theatre_schedules) > 0):
    print('\nTheater:')
    for theatre_schedule in theatre_schedules:
        print(' ', theatre_schedule.string)

if (len(release_schedules) > 0):
    print('\nRelease:')
    for release_schedule in release_schedules:
        print(' ', release_schedule.string)

print('\n')
