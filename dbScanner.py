import pymysql

class Scanner:
	def __init__(self):
		print("Initializing in dbScanner")
	def scan(self,conn):
		cur = conn.cursor()
		cur.execute("show tables;")
		return cur