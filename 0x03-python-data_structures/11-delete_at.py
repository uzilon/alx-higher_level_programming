#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
	return my_list
    else:
	front = my_list[:idx]
	back = my_list[idx + 1:]
	my_list[0:] = front + back
	return my_list
