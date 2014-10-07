import json

def fetch():
	text2 = open("database.json","r+")

	json_data = json.loads(text2.read())

	date = json_data[len(json_data)-1]["date"]
	duties = json_data[len(json_data)-1]["duties"]
	time = json_data[len(json_data)-1]["time"]
	organization = json_data[len(json_data)-1]["organization"]
	org_lead = json_data[len(json_data)-1]["org_lead"]


	returner = {"date":date, "duties":duties, "time":time, "organization":organization, "org_lead":org_lead}

	for x in range(len(returner["date"])):
		print returner["date"][x],
		print returner["duties"][x],
	#	print returner["time"][x]
	#	print returner["organization"][x]
	#	print returner["org_lead"][x]
	#print returner
	return returner


fetch()