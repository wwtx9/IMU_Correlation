import os
import numpy as np
import pandas as pd
import strym
from strym import strymread
from scipy import signal
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # load imus
    xx = 'ax'
    imu1 = pd.read_csv('data/imu1/imu1_data_ax.csv')[0:1000]
    imu2 = pd.read_csv('data/imu2/imu2_data_ax.csv')[0:1000]
    df1 = imu1.copy(deep=True)
    df2 = imu2.copy(deep=True)

    # visualize the data first
    fig, ax = strymread.create_fig(1)
    ax[0].scatter(x=df1['Time'], y=df1['Message'], s=4, label='imu1', c='#131342')
    ax[0].scatter(x=df2['Time'], y=df2['Message'], s=1, label='imu2', c='#f34283')
    ax[0].set(xlabel='timestamps(s)') #, ylabel='ax')
    ax[0].set_ylabel(xx, labelpad=-10)
    # ax[0].yaxis.set_label_coords(0, 0.5)
    ax[0].legend()
    fig.show()
    # save_path = "results/" + xx + ".png"
    # fig.savefig(save_path)

    # Now, we can use strymread's time_shift function from strym package to find out the optimal time_shift
    time_shift = strymread.time_shift(df1, df2)
    print(time_shift)
    time_shift = 3.62
    # Finally, we can visualize the data after timeshift:
    fig, ax = strymread.create_fig(1)
    ax[0].scatter(x=df1['Time'], y=df1['Message'], s=4, label='IMU1', c='#131342')
    ax[0].scatter(x=df2['Time'] + time_shift, y=df2['Message'], s=1, label='IMU2', c='#f34283')
    # ax[0].scatter(x=df2['timestamp[s]'] + time_shift, y=df2['wx'], s=1, label='IMU2', c='#f34283')
    ax[0].set(xlabel='timestamps(s)')
    ax[0].set_ylabel(xx, labelpad=-10)
    ax[0].legend(loc='lower right')
    fig.show()
    # save_path = "results/" + xx + "_synchronised.png"
    # fig.savefig(save_path)

