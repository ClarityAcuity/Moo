import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,\
DayLocator, MONDAY,date2num
from mplfinance.original_flavor import candlestick_ohlc
import numpy as np

def candlePlot(seriesData,title='a'):
    plt.rcParams['font.sans-serif'] = ['Heiti TC']
    plt.rcParams['axes.unicode_minus'] = False
	#設定日期格式
    Date=[date2num(date) for date in seriesData.index]
    seriesData.loc[:,'Date']=Date

	#將DataFrame數據轉換成List類型
    listData=[]
    for i in range(len(seriesData)):
        a=[seriesData.Date[i],\
        seriesData.Open[i],seriesData.High[i],\
        seriesData.Low[i],seriesData.Close[i]]
        listData.append(a)

	#設定繪圖相關參數
    ax = plt.subplot()
    mondays = WeekdayLocator(MONDAY)
    #日期格式為‘15-Mar-09’形式
    weekFormatter = DateFormatter('%y %b %d')
    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(DayLocator())
    ax.xaxis.set_major_formatter(weekFormatter)

	#調用candlestick_ohlc函數
    candlestick_ohlc(ax,listData, width=0.7,\
                     colorup='r',colordown='g')
    ax.set_title(title) #設定標題
    #設定x軸日期顯示角度
    plt.setp(plt.gca().get_xticklabels(), \
    rotation=50,horizontalalignment='center')
    return(plt.show())

#蠟燭圖與線圖,柱狀圖
def candleLinePlots(candleData, candleTitle='a', **kwargs):
    plt.rcParams['font.sans-serif'] = ['Heiti TC']
    plt.rcParams['axes.unicode_minus'] = False

    Date = [date2num(date) for date in candleData.index]
    candleData.loc[:,'Date'] = Date
    listData = []    
    for i in range(len(candleData)):
        a = [candleData.Date[i],\
            candleData.Open[i],candleData.High[i],\
            candleData.Low[i],candleData.Close[i]]
        listData.append(a)
    # 如 果 不 定 長 參 數 無 取 值 ， 只 畫 蠟 燭 圖
    ax = plt.subplot()    
    # 如 果 不 定 長 參 數 有 值 ， 則 分 成 兩 個 子 圖
    flag=0
    if kwargs:
        if kwargs['splitFigures']:
            ax = plt.subplot(211)
            ax2= plt.subplot(212)
            flag=1;
        # 如 果 無 參 數 splitFigures ， 則 只 畫 一 個 圖 形 框
        # 如 果 有 參 數 splitFigures ， 則 畫 出 兩 個 圖 形 框      
        for key in kwargs:
            if key=='title':
                ax2.set_title(kwargs[key])
            if key=='ylabel':
                ax2.set_ylabel(kwargs[key])
            if key=='grid':
                ax2.grid(kwargs[key])
            if key=='Data':
                plt.sca(ax)
                if flag:
                    plt.sca(ax2)                   
                #一維數據
                if kwargs[key].ndim==1:
                    plt.plot(kwargs[key],\
                        color='k',\
                        label=kwargs[key].name)
                    plt.legend(loc='best')
                #二維數據有兩個columns
                elif all([kwargs[key].ndim==2,\
                          len(kwargs[key].columns)==2]):
                    plt.plot(kwargs[key].iloc[:,0], color='k',\
                        label=kwargs[key].iloc[:,0].name)
                    plt.plot(kwargs[key].iloc[:,1],\
                        linestyle='dashed',\
                        label=kwargs[key].iloc[:,1].name)
                    plt.legend(loc='best')
                 #二維數據有3個columns
                elif all([kwargs[key].ndim==2,\
                          len(kwargs[key].columns)==3]):
                    plt.plot(kwargs[key].iloc[:,0], color='k',\
                        label=kwargs[key].iloc[:,0].name)
                    plt.plot(kwargs[key].iloc[:,1],\
                        linestyle='dashed',\
                        label=kwargs[key].iloc[:,1].name)
                    plt.bar(x = kwargs[key].iloc[:,2].index,\
                        height = kwargs[key].iloc[:,2],\
                        color = 'r',label = kwargs[key].iloc[:,2].name)
                    plt.legend(loc='best')                   
    mondays = WeekdayLocator(MONDAY)
    weekFormatter = DateFormatter('%y %b %d')
    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(DayLocator())
    ax.xaxis.set_major_formatter(weekFormatter)
    plt.sca(ax)
    
    candlestick_ohlc(ax,listData, width=0.7,\
                     colorup='r',colordown='g')
    ax.set_title(candleTitle)
    plt.setp(ax.get_xticklabels(),\
             rotation=20,\
             horizontalalignment='center')
    ax.autoscale_view()
    
    return(plt.show())

#蠟燭圖與成交量柱狀圖
def candleVolume(seriesData,candletitle='a',bartitle='b'):
    plt.rcParams['font.sans-serif'] = ['Heiti TC']
    plt.rcParams['axes.unicode_minus'] = False

    Date=[date2num(date) for date in seriesData.index]
    seriesData.loc[:,'Date']=Date
    seriesData.index=list(range(len(Date)))
    listData=zip(seriesData.Date,seriesData.Open,seriesData.High,seriesData.Low,
                 seriesData.Close)
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    for ax in ax1,ax2:
        mondays = WeekdayLocator(MONDAY)
        weekFormatter = DateFormatter('%m/%d/%Y')
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(DayLocator())
        ax.xaxis.set_major_formatter(weekFormatter)
        ax.grid(True)

    ax1.set_ylim(seriesData.Low.min()-2,seriesData.High.max()+2)
    ax1.set_ylabel('蠟燭圖及收盤價線')
    candlestick_ohlc(ax1,listData, width=0.7,colorup='r',colordown='g')
    plt.setp(plt.gca().get_xticklabels(),\
            rotation=45,horizontalalignment='center')
    ax1.autoscale_view()
    ax1.set_title(candletitle)
    ax1.plot(seriesData.Date,seriesData.Close,\
               color='black',label='收盤價')
    ax1.legend(loc='best')

    ax2.set_ylabel('成交量')
    ax2.set_ylim(0,seriesData.Volume.max()*3)
    ax2.bar(np.array(Date)[np.array(seriesData.Close>=seriesData.Open)]
    ,height=seriesData.iloc[:,5][np.array(seriesData.Close>=seriesData.Open)]
    ,color='r',align='center')
    ax2.bar(np.array(Date)[np.array(seriesData.Close<seriesData.Open)]
    ,height=seriesData.iloc[:,5][np.array(seriesData.Close<seriesData.Open)]
    ,color='g',align='center')
    ax2.set_title(bartitle)
    return(plt.show())

