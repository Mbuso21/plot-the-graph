from tkinter.tix import MAIN
from unittest.main import main
from urllib import response

from flask import request
import plotext as plt
import matplotlib.pyplot as mpl
from datetime import datetime
import requests as req

def work():
    y = []
    x = []

    api_data = {
        "01-01-2022":300,
        "02-01-2022":500,
        "03-01-2022":700,
        "04-01-2022":1300,
        "05-01-2022":2000,
        "06-01-2022":3000,
        "07-01-2022":3500,
        "08-01-2022":4000,
        "09-01-2022":4500,
        "10-01-2022":5000,
        "11-01-2022":20000,
        "12-01-2022":35000,
        "13-01-2022":46000,
        "14-01-2022":70000,
        "15-01-2022":90000
    }

    # response = request.get("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")

    # print(response)

    print(datetime.strptime('01-01-2022', '%d-%m-%Y'))

    for k in api_data:
        y.append(datetime.strptime(k, '%d-%m-%Y'))
        x.append(api_data[k])

    print(y)
    print(x)

    mpl.plot_date(y, x, xdate=True, ydate=False)
    mpl.show()
    


def getDataFromAPI(api_url):
    """
    
    """

    return data_dict


def convertDateIntoLists(data):
    """
    Takes data(dict) as a param and returns a tuple of x and y co-ordinates which are lists
    """
    x = []
    y = []
    for k in api_data:
        y.append(datetime.strptime(k, '%d-%m-%Y'))
        x.append(api_data[k])

    return x, y
    
def plotGraph(xaxis, yaxis, start, end):
    """

    """

    mpl.plot_date(y, x, xdate=True, ydate=False)
    mpl.show()

def run():
    print(hello)


if __name__ == "__main__":
    work()
