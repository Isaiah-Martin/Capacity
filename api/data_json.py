def fetch():
	text = open("database.json","r")
	text = json.loads(text)
	return text