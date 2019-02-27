def app(samples):
	'''
	samples - a buffer stream from the gathered channels.
	This function will be executed on each recieved buffer of data.
	The analysis of the signal should, be handled through here.
	'''
	print(samples)
