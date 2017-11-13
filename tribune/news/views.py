from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

# display news
def news_of_day(request):
    date = dt.date.today()

    # Function to convert date object to find exact day
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
        '''
    return render(request,'all-news/today_news.html',{"date": date,})

# getting day of the week
def convert_dates(dates):
    '''
    Function that gets the weekday number for the dates
    '''
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    # Returning the actual day of the week
    day = days[day_number]
    return day

# getting values from a URL
# view function to prevent news from the past days
def past_days_news(request,past_date):
    try:
    # converts data from the string url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:

        # raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    return render(request,'all-news/past_news.html',{"date": date})
