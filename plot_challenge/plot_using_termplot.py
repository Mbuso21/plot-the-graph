from urllib import response
import matplotlib.pyplot as mpl
from datetime import datetime
import requests as req
from datetime import date
import json


def getDataFromAPI(api_url):
    """
    takes a string http url
    returns the data as a dict text
    """
    return json.loads(req.get(api_url).text)



def convertDataIntoLists(data):
    """
    Takes data(dict) as a param and returns a tuple of x and y co-ordinates which are lists
    """
    x = []
    y = []
    for k in data:
        y.append(datetime.strptime(k, '%d-%m-%Y'))
        x.append(data[k])

    return x, y
    
def plotGraph(x_axis, y_axis):
    """
    Takes xaxis(list) a list of x co-ordinates
    """

    mpl.plot_date(y_axis, x_axis, xdate=True, ydate=False)
    mpl.show()


def run():
    data = getDataFromAPI("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")
    x_axis, y_axis = convertDataIntoLists(data)
    plotGraph(x_axis, y_axis)


if __name__ == "__main__":
    run()
