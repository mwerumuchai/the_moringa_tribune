from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Article


# display news
# def news_of_day(request):
#     date = dt.date.today()
#
#     # Function to convert date object to find exact day
#
#     return render(request,'all-news/today_news.html',{"date": date,})


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

    return render(request,'all-news/past_news.html',{"date": date, "news":news})

# updating our views
def news_today(request):
    date = dt.date.today()
    news = Article.todays_news

    return render(request, 'all-news/today_news.html', {"date": date, "news":news})
