from .models import Dreamreal, Error
import datetime


def Dateformat(date):
    try:
        return datetime.datetime.strptime(date, '%m-%d-%Y').strftime('%Y-%m-%d')
    except:
        return datetime.datetime.strptime(date, '%m-%d-%y').strftime('%Y-%m-%d')


def handle_uploaded_file(f):
    i = 0
    for chunk in f:
        chunk = chunk.decode("utf-8")
        chunk = chunk.split(',')
        data = Dreamreal()
        if i != 0:
            chunk[0] = Dateformat(chunk[0])
            if Dreamreal.objects.filter(host=chunk[1], date=chunk[0]).count() < 1:
                data.date = chunk[0]
                data.host = chunk[1]
                data.din = chunk[2]
                data.dout = chunk[3]
                data.dtot = chunk[4]
                data.save()
        i += 1


def DataValidate(hostname, date):
    try:
        datetime.datetime.strptime(date, '%m-%d-%Y').strftime('%Y-%m-%d')
        return True
    except:
        if hostname != None:
            pass
            return False


def handle_file(f):
    # print f.readlines()
    i = 0
    for chunk in f:
        print chunk
        chunk = chunk.decode("utf-8")
        print chunk
        chunk = chunk.split(',')

        data = Dreamreal()
        if i != 0:
            chunk[0] = Dateformat(chunk[0])
            if Dreamreal.objects.filter(host=chunk[1], date=chunk[0]).count() < 1:
                data.date = chunk[0]
                data.host = chunk[1]
                data.din = chunk[2]
                data.dout = chunk[3]
                data.dtot = chunk[4]
                data.save()
        i += 1


# ===============



def Log_process(hostname, log):
    print hostname, log
    date = datetime.datetime.now().date()
    print date
    a_data = Error.objects.filter(hostname=hostname, date=date, log=log)
    data = Error()
    if not a_data:
        print 'New data'
        data.hostname = hostname
        data.date = date
        data.log = log
        data.c = 1
        data.save()
        return 200
    else:
        print 'Old data found'
        b_data = Error.objects.get(hostname=hostname, date=date, log=log)
        b_data.c = b_data.c + 1
        print b_data
        b_data.save()
        return 200


# chartview
from chartit import DataPool, Chart
def chart_view(log, d):
    if not d:
        d = datetime.datetime.now().date()
        d = d.strftime('%Y-%m-%d')
        #d = '2017-08-12'
        #print 'Date:',d
    logdata = \
        DataPool(
            series=
            [{'options': {
                'source': Error.objects.filter(log=log, date=d)},
                'terms': [
                    'hostname',
                    'date',
                    'log',
                    'c']}
            ])

    # Step 2: Create the Chart object
    chart = Chart(
        datasource=logdata,
        series_options=
        [{'options': {
            'type': 'line',
            'stacking': False},
            'terms': {
                'hostname': [
                    'c']
            }}],
        chart_options=
        {'title': {
            'text': log},
            'xAxis': {
                'title': {
                    'text': 'Host Name'}},
            'yAxis': {
                'title': {
                    'text': 'Count per day'}}})
    return chart


