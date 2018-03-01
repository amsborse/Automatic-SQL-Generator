import pymysql

class Connector:
	conn = None
	def __init__(self):
		print("Initializing in dbConnector")
	def connect(self):
		try:
			Connector.conn = pymysql.connect(user='root',passwd='akshay',host='127.0.0.1',port=3306,database='nlp')
			print("Connection successful")
		except:
			print("Oops...Connection fail!")
		return Connector.conn