from dataclasses import dataclass
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
    for key in data:
        y.append(datetime.strptime(key, '%d-%m-%Y'))
        x.append(data[key])

    return x, y

def covertStringDateIntoDateTime(str_date):
    """
    Converts a date string into a datetime object
    str_date formate must be DD-MM-YYYY
    returns a datetime object
    """

    return datetime.strptime(str_date, '%d-%m-%Y')


def isDataDateBeforeStartDate(data_start_date, date_entered):
    """
    Both params take string date in format DD-MM-YYYY
    returns True if data_start_date < date_entered else False
    """


    return covertStringDateIntoDateTime(data_start_date) > covertStringDateIntoDateTime(date_entered)

    
def plotGraph(x_axis, y_axis, start_date=0, end_date=0):
    """
    Takes xaxis(list) a list of x co-ordinates
    """
    if start_date == 0 or end_date == 0:

        mpl.plot_date(y_axis, x_axis, xdate=True, ydate=False)
        mpl.show()

    


def run():
    data = getDataFromAPI("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")
    x_axis, y_axis = convertDataIntoLists(data)
    print(x_axis)
    print(y_axis)
    plotGraph(x_axis, y_axis)


if __name__ == "__main__":
    run()
    # data_start_date = datetime.strptime("26-01-2022", "%d-%m-%Y")
    # date_entered = datetime.strptime("26-01-2021", "%d-%m-%Y")
    # check_bool = checkIfDateIsBeforeStartDate(data_start_date, date_entered)
    # print(check_bool)
