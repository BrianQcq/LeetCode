
def Q1(arg, *argv):
	dis = 0
	ini_time = arg[0][0]
	ini_read = arg[0][1]
	for item in arg[1:]:
		dis += (item[0] - ini_time)/3600 * ini_read
		ini_time = item[0]
		ini_read = item[1]
	dis += (argv[0] - ini_time)/3600 * ini_read
	return round(dis,2)

print(Q1([[0,90],[300,80]], 600))


def Q2(coordinates):
	n = len(coordinates)
	x_list = sorted([x[0] for x in coordinates])
	y_list = sorted([x[1] for x in coordinates])
	med_x, med_y = x_list[n//2], y_list[n//2]
	dis = 0
	for coord in coordinates:
		dis += abs(med_x - coord[0]) + abs(med_y - coord[1])
	return dis

print(Q2([[-4,3],[-2,1],[1,0],[3,2]]))