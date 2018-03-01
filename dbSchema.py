
class Schema():
	tables = []
	dictionary = {}
	def __init__(self):
		Schema.tables=[]
		print("Initialization in Schema")
	def populate(self,cur):
		cur.execute("show tables;")
		for row in cur:
			Schema.tables.append(row[0])
		for table in Schema.tables:
			s = "desc "+table+" ;"
			cur.execute(s);
			lst = []
			for row in cur:
				lst.append(row[0])
			Schema.dictionary.update({table:lst})	

		return Schema.dictionary