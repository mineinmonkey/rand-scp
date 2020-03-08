from webbrowser import open
from random import randrange
import PySimpleGUI as sg

layout = [
    [sg.Text('SCP Series:', size=(15, 1))],
    [sg.Radio('Any', '1', default=True), sg.Radio('1', '1'), sg.Radio('2', '1'), sg.Radio('3', '1'), sg.Radio('4', '1'),
     sg.Radio('5', '1'), sg.Radio('6', '1')],
    [sg.Submit(), sg.Exit()]
]

window = sg.Window('Random SCP Page', no_titlebar=True, grab_anywhere=True, keep_on_top=True).Layout(layout)


def scp_url(scp_num):
    open('www.scp-wiki.com/scp-' + scp_num)


while True:
    button, series = window.Read()

    if button in 'Exit':
        break

    if series[0]:
        anyRandNum = str(randrange(1, 6000))
        if len(anyRandNum) == 2:
            anyRandNum = '0' + anyRandNum
        elif len(anyRandNum) == 1:
            anyRandNum = '00' + anyRandNum
        scp_url(anyRandNum)
    else:
        seriesRandNum = str(randrange(1, 1000))
        trueSeries = 0
        for i in range(5):
            if series[i + 1]:
                trueSeries = str(i)
        # If the random number has less than 3 digits, add 0s to the front
        while len(seriesRandNum) < 3:
            seriesRandNum = '0' + seriesRandNum
        if not series[1]:
            seriesRandNum = trueSeries + seriesRandNum
        scp_url(seriesRandNum)

window.Close()
