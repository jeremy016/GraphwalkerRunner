import json,os


class Set_Resource(object):

	data = None
	resource_path=None

	"""This function is used to get config data & current work folder path

		Args:
			current_path (str):	work folder path 

		

	"""

	def __init__(self,current_path=''):

		if current_path:
		
			self.resource_path = current_path+'/config.json'
		try:
			read_file = open(self.resource_path).read()

			self.data = json.loads(read_file)
		
		except IOError as e :
			print 111
			with open(self.resource_path,'w') as f: f.write('{}')
			self.__init__(current_path)

	"""This function is used to set android Device Serial to config.json

		Args:
			Serial(int): 

		Returns:
			True(bool): Successful
			data(json): config data

		Raises:
			False(bool): Fail
			e.message(str): error message

	"""
	def set_androidDeviceSerial(self,Serial):

		try:

			self.data['Device']['androidDeviceSerial'] = Serial

			json_str = json.dumps(self.data).decode('unicode-escape').encode('utf8')

			with open(self.resource_path, 'w') as f : f.write(json_str)		

			return True,self.data

		except KeyError as e:

			self.data[e.message]={}

			self.set_androidDeviceSerial(Serial)

		except Exception as e:
			
			print e
			return False,e
		
