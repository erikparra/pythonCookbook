def drop_first_last(grades):
	first, *middle, last = grades
	return avg(middle)

if __name__ == '__main__':
	list = [10, 20, 30, 40]
	print( drop_first_last(list) )