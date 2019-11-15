import webbrowser as web
import random as rand
import PySimpleGUI as sg

layout = [
	[sg.Text('SCP Series:', size=(15,1))],
	[sg.Radio('Any', '1', default=True), sg.Radio('1', '1'), sg.Radio('2', '1'), sg.Radio('3', '1'), sg.Radio('4', '1'), sg.Radio('5', '1')],
	[sg.Submit(), sg.Exit()]
]

window = sg.Window('Random SCP Page', no_titlebar=True, grab_anywhere=True, keep_on_top=True).Layout(layout)

def scpURL(scpNum):
	web.open('www.scp-wiki.com/scp-' + scpNum)

while True:
	button, series = window.Read()
  
	if button in 'Exit':
		break
  
	if series[0] == True:
		anyRandNum = str(rand.randrange(1, 5000))
		if len(anyRandNum) == 2:
			anyRandNum = '0' + anyRandNum
		elif len(anyRandNum) == 1:
			anyRandNum = '00' + anyRandNum
		scpURL(anyRandNum)
	else:
		seriesRandNum = str(rand.randrange(1, 1000))
		trueSeries = 0
		for i in range(5):
			if series[i+1] == True:
				trueSeries = str(i)
				
		while len(seriesRandNum) < 3:
			seriesRandNum = '0' + seriesRandNum
		if series[1] == False:
			seriesRandNum = trueSeries + seriesRandNum
		scpURL(seriesRandNum)

window.Close()