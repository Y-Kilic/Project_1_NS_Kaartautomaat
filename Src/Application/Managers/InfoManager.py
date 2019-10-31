import datetime

class InfoManager(object):
    def getDelay(plannedDateTime, actualDateTime):
        if plannedDateTime == actualDateTime:
            delay = "-"
            return delay
        planned = plannedDateTime.replace('T', ':')
        actual = actualDateTime.replace('T', ':')
        planned = datetime.datetime.strptime(planned[11:16], '%H:%M')
        actual = datetime.datetime.strptime(actual[11:16], '%H:%M')
        delay = actual - planned
        return str(delay)


