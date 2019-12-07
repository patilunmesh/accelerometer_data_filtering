'''
accelerometer filtering with median and low pass filter using scipy
@author: Unmesh Patil
'''
import os
import sys
import csv
import numpy as np 
import math
from scipy import signal

def median_filter(data, f_size):
	return signal.medfilt(data, f_size)
	
def freq_filter(data, f_size, cutoff):
	lpf = signal.firwin(f_size, cutoff, window='hamming')
	return signal.convolve(data, lpf, mode='same')

def readCsv(file):
	with open (('/home/unmesh/'+ file) , 'r') as l:
		data = csv.reader(l)
		acc_data = list(data)
	l.close()
	return acc_data

def writeCsv(axis, data, median_data, lpf_data, comb_data):
	with open (('/home/unmesh/filtered' + axis + '.csv'), 'a') as pw:
		writer_point = csv.writer(pw)
		all_data = np.zeros((len(data),4))
		i = 0
		for i in range(len(data)-1):
			all_data[i][0] = str(data[i])
			all_data[i][1] = str(median_data[i])
			all_data[i][2] = str(lpf_data[i])
			all_data[i][3] = str(comb_data[i])
		writer_point.writerows(all_data)
	pw.close()

def CompleteFilter(axis, data):
	median_data=median_filter(data, 155)
	#print(median_data)
	lpf_data=freq_filter(data, 155, cutoff/fs)
	#print(lpf_data)
	comb_data=freq_filter(median_data, 155, cutoff/fs)
	writeCsv(axis, data, median_data, lpf_data, comb_data)



data = readCsv('braking.csv')
#print(data)
acc_x =[]
acc_y =[]
acc_z =[]
for i in range(len(data)):
	acc_x.append(float(data[i][0]))
	acc_y.append(float(data[i][1]))
	acc_z.append(float(data[i][2]))
#print(acc_x)
fs=512
cutoff=10
CompleteFilter('x',acc_x)
CompleteFilter('y',acc_y)
CompleteFilter('z',acc_z)
print('done filtering!!!')


