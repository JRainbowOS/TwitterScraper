import matplotlib.pyplot as plt
from matplotlib.dates import (date2num,
                            num2date,
                            DAILY,
                            DateFormatter,
                            rrulewrapper,
                            RRuleLocator)
import numpy as np 


class Visualiser():

    def __init__(self, account_name):
        self.account_name = account_name
        self.dates = None
        self.values = None
        self.plt_dates = None

    def set_dates(self, dates):
        self.dates = dates
        self.plt_dates = [date2num(date) for date in self.dates]

    def set_values(self, values):
        self.values = values

    def plot(self, average=None):
        if average:
            average_dates = [np.mean(self.plt_dates[i: i + average]) for i in range(0, len(self.plt_dates), average)]
            average_values = [np.mean(self.values[i: i + average]) for i in range(0, len(self.values), average)]
            plt.plot_date(x=average_dates, y=average_values, xdate=True, ydate=False)
        else:
            plt.plot_date(x=self.plt_dates, y=self.values, xdate=True, ydate=False)
        plt.title(f'Sentiment Analysis of {self.account_name}\'s Twitter Feed')
        plt.xlabel('Date')
        plt.xticks(rotation=30)
        plt.ylabel('Sentiment (-1 to 1)')
        plt.show()


        # rule = rrulewrapper(DAILY, byeaster=1, interval=5)
        # loc = RRuleLocator(rule)
        # formatter = DateFormatter('%m/%d/%y')
        # fig, ax = plt.subplots()
        # plt.plot_date(x=self.plt_dates, y=self.values, xdate=True, ydate=False)
        # ax.xaxis.set_major_locator(loc)
        # ax.xaxis.set_major_formatter(formatter)
        # ax.axis.set_tick_params(rotation=30, labelsize=10)
        # plt.show()
