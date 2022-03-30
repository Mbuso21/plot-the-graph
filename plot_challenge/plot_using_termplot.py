from urllib import response
import matplotlib.pyplot as mpl
from datetime import datetime
import requests as req
from datetime import date
import json

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

    response = req.get("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")

    response_text = response.text
    json_data = json.loads(response_text)
    print(json_data)
    print(type(json_data))
    print(type(response_text))


    print(datetime.strptime('01-01-2022', '%d-%m-%Y'))

    for k in json_data:
        y.append(datetime.strptime(k, '%d-%m-%Y'))
        x.append(api_data[k])

    print(y)
    print(x)

    mpl.plot_date(y, x, xdate=True, ydate=False)
    mpl.show()
    


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
        x.append(api_data[k])

    return x, y
    
def plotGraph(x_axis, y_axis):
    """
    Takes xaxis(list) a list of x co-ordinates
    """

    mpl.plot_date(y, x, xdate=True, ydate=False)
    mpl.show()


def run():
    print(hello)


if __name__ == "__main__":
    work()
