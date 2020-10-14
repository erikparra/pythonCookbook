import math

def drop_first_last(grades):
	first, *middle, last = grades
	print( 'middle: ', middle )
	return sum(middle) / len(middle)



if __name__ == '__main__':
	list = [10, 20, 30, 40]
	print( 'Average:', drop_first_last(list) )

	record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
	name, email, *phone_numbers = record
	print( 'name', name)
	print( 'email', email)
	print( 'phone_numbers', phone_numbers)