import math
import numpy as np
import datetime

def TravelDis(city1, city2, tripID):
	earth_radius = 3958.8
	coord1 = (float(city1.split(':')[-2])*math.pi/180, float(city1.split(':')[-1])*math.pi/180)
	coord2 = (float(city2.split(':')[-2])*math.pi/180, float(city2.split(':')[-1])*math.pi/180)
	long_diff = abs(coord1[1] - coord2[1])
	angle = np.arccos(math.sin(coord1[0])*math.sin(coord2[0]) + math.cos(coord1[0])*math.cos(coord2[0])*math.cos(long_diff))
	dis = earth_radius * angle
	temp = tripID.split(':')[1:]
	temp.append(str(int(round(dis))))
	#print(temp)
	return ':'.join(temp)

print(TravelDis('LOC:CHI:41.836944:-87.684722', 'LOC:NYC:40.7127:-74.0059', 'TRIP:C0FFEE1C:CHI:NYC'))



def AccountNumberValid(s):
	temp_sum = str(int(s[2:], 16))
	res = 0
	for i in temp_sum:
		res += int(i)
	return 'VALID' if res == int(s[:2],16) else 'INVALID'

print(AccountNumberValid('BADF00D5'))
print(AccountNumberValid('1CC0FfEE'))


class Hashtable:
	_table = {}
	_high_watermark = 0

	def __init__(self, rawEvetns):
		for item in rawEvetns:
			epoch, tp, ky, vl = item.split('|')
			

	@property
	def table(self):
		return self._table
	
	@property
	def high_watermark(self):
		return self._high_watermark
	