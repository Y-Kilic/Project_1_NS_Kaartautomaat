class InfoManager(object):
    def getDelay(plannedDateTime, actualDateTime):
        if plannedDateTime == actualDateTime:
            return "-"

        delay = plannedDateTime - actualDateTime


