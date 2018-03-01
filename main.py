import dbConnector
import dbScanner
import dbSchema

connector = dbConnector.Connector()
connection = connector.connect()

scanner = dbScanner.Scanner()
cursor = scanner.scan(connection)

schema = dbSchema.Schema()
dictionary = schema.populate(cursor)

for i in dictionary:
	print(i,dictionary[i])


