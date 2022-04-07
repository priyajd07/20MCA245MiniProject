from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
from django.http import HttpResponse
import requests
import json
import tweepy
from tweepy.auth import OAuthHandler
from textblob import TextBlob
from .fusioncharts import FusionCharts
from collections import OrderedDict
from .news import Analysis

# Create your views here.


def home(request):
    return render(request, 'blog/index.html', {})


def getSentiments(request):
    auth = OAuthHandler('XRCnQ49KVWgy0IsN5QYBTn5Zm', 'P6UwYNbfboKQfrr51P3HLjp88Mq32SxNcQt7zsFKDdAZdXrAoW')
    auth.set_access_token('912853951984238592-BODZqgKvgD0QdKD5Rz1grMGPCDFiZm4', 'proz3qXFAR7Ie8YOylG86z0uERL8orw0HcClAA2X4CN6t')

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    

    public_tweets = []
    if request.method=='GET':
        query = request.GET.get('search',"congress")
        a = Analysis(query)
        full_analysis = a.run()
    else:
        return redirect('home')

    chartData = OrderedDict()
    total_pos = 0
    total_neg = 0
    total_neu = 0

    for tweet in tweepy.Cursor(api.search, q=query, result_type="recent", tweet_mode="extended", lang="en").items(20):
        blob = TextBlob(tweet.full_text)
        senti = blob.sentiment.polarity
        sub = float("{0:.2f}".format(blob.sentiment.subjectivity))
        if senti>0.1:
            senti_analysis = 'Positive'
            total_pos += 1
        elif senti<-0.1:
            senti_analysis = 'Negative'
            total_neg += 1
        else:
            senti_analysis = 'Neutral'
            total_neu += 1
        public_tweets.append({'tweet':tweet, 'subjectivity':sub, 'senti': senti, 'senti_analysis':senti_analysis})
        chartData[tweet.user.screen_name] = senti
    score=total_pos+(total_neu/2)-total_neg
    percent=(score/20)*100
    if(percent>95):
        percent=percent-10
    print(percent)
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Sentiments of Tweets"
    chartConfig["subCaption"] = "sentiments in range 0 to 1. Red: negative, Blue: Positive, Black: Neutral"
    chartConfig["xAxisName"] = "Twitter Handles"
    chartConfig["yAxisName"] = "Sentiments"
    chartConfig["numberSuffix"] = ""
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs data
    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        if value>0.1:
            data["color"] = "#0000ff"
        elif value<-0.1:
            data["color"] = "#ff0000"
        else:
            data["color"] = "#000000"
        if value>0:
            data["value"] = value
        else:
            data["value"] = -value
        dataSource["data"].append(data)

    datapie = [{
            "label": "Positive",
            "value": total_pos
        }, {
            "label": "Negative",
            "value": total_neg
        }, {
            "label": "Neutral",
            "value": total_neu
        }]
    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("column2d", "ex1" , "100%", "200", "chart-1", "json", dataSource)
        # Create an object for the pie3d chart using the FusionCharts class constructor
    pie3d = FusionCharts("pie3d", "ex2" , "100%", "200", "chart-2", "json",
        # The data is passed as a string in the `dataSource` as parameter.
    {
        "chart": {
            "caption": "Sentiment Distribution",
            "subCaption" : "Pie Chart",
            "showValues":"1",
            "showPercentInTooltip" : "1",
            "numberPrefix" : "$",
            "enableMultiSlicing":"1",
            "theme": "fusion"
        },
        "data": datapie,
    })

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
#   return  render(request, 'index.html', {'output' : pie3d.render(), 'chartTitle': 'Pie 3D Chart'})






    return render(request, 'search_result.html', {'public_tweets': public_tweets, 'full_analysis': full_analysis, 'percent':percent,'output1': column2D.render(), 'output2' : pie3d.render()})