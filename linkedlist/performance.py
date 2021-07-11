# test 


from memory_profiler import profile



@profile
def run(type_list):
	from time import time
	start = time()
	for i in range(0,1000):
		type_list.append(i)
	print(time()-start)
