from __future__ import division
__author__ = 'Isaiah'

from flask import Flask, request, redirect, render_template
app = Flask(__name__, static_url_path='')

from data_json import fetch

import json

def taken(v_obj,v_area):
	if v_obj in v_area:
		return True
	return False

@app.route('/test', methods=['POST'])
def info():
	user_email_address = str(request.form['email'])

	print "user_email_address = %s" % (user_email_address)

	json_ = {"email_address" : user_email_address}
	#Code Oakland
	return json.dumps(json_)
	#return render_template('/Method2.html', info=email)
@app.route('/UHome')
def home_page():
	text2 = open("database.json", "r+")
	json_data  = json.loads(text2.read())
	name = json_data[len(json_data)-1]["username"]
	email = json_data[len(json_data)-1]["email"]
	return render_template("/UHome.html", name=name, email=email)

@app.route('/UBasic_Information')
def Basic_Information_route():
	text2 = open("database.json", "r+")
	json_data  = json.loads(text2.read())
	name = json_data[len(json_data)-1]["username"]
	email = json_data[len(json_data)-1]["email"]
	return render_template("/UBasic_Information.html", name=name, email=email)

@app.route('/Community_Service')
def community_service_route():
    text2 = open("database.json", "r+")
    # open file database.json and store contents in variable
    json_data  = json.loads(text2.read())
    current = json_data[len(json_data)-1]["hrs"]
    hrs = json_data[len(json_data)-1]["plan_hrs"]
    percentage = float(float(current)/float(hrs) * 100)
    difference = 100 - percentage
    last = float(hrs) - float(current)
    name = json_data[len(json_data)-1]["username"]
    email = json_data[len(json_data)-1]["email"]
    date = json_data[len(json_data)-1]["date"]
    duties = json_data[len(json_data)-1]["duties"]
    time = json_data[len(json_data)-1]["time"]
    organization = json_data[len(json_data)-1]["organization"]
    organization_leader = json_data[len(json_data)-1]["org_lead"]

    # search contents for entry that is associated with community service info
   

    template_data = fetch()
    intlist = []
    for x in range(len(template_data["date"])):
    	#print template_data["date"][x]
    	intlist.append(x)
    print intlist

    # build data_object for all items that will be using in template

    data_object = { "name":name, "email":email, "current_hrs":current, "last":last, "goal":hrs, "percentage":percentage, "difference":difference, "date":date, "duties":duties, "time":time, "organization":organization, "org_lead":organization_leader}

    # build the list of dictionaries for community service goals

    return render_template("/Community_Service.html", mode="/Community_Service", intlist=intlist, data=data_object, template_data=template_data)


@app.route('/Student_Page')
def student_page_route():
	text2 = open("database.json","r+")
	json_data = json.loads(text2.read())
	A4 = json_data[len(json_data)-1]["week_goal_1"] 
	A5 = json_data[len(json_data)-1]["week_goal_2"]
	A6 = json_data[len(json_data)-1]["week_goal_3"] 
	A7 = json_data[len(json_data)-1]["month_goal_1"] 
	A8 = json_data[len(json_data)-1]["month_goal_2"] 
	A9 = json_data[len(json_data)-1]["month_goal_3"]
	A10 = json_data[len(json_data)-1]["year_goal_1"] 
	A11 = json_data[len(json_data)-1]["year_goal_2"]
	A12 = json_data[len(json_data)-1]["year_goal_3"] 
	IA = json_data[len(json_data)-1]["ec1"]
	IB = json_data[len(json_data)-1]["ec2"] 
	IC = json_data[len(json_data)-1]["ec3"] 
	I1 = json_data[len(json_data)-1]["focus"] 
	I3 = json_data[len(json_data)-1]["dob"] 
	I4 = json_data[len(json_data)-1]["class"] 
	I5 = json_data[len(json_data)-1]["gpa"] 
	I6 = json_data[len(json_data)-1]["goal_gpa"] 
	I7 = json_data[len(json_data)-1]["plan_hrs"] 
	I8 = json_data[len(json_data)-1]["hrs"] 
	a = json_data[len(json_data)-1]["email"] 
	b = json_data[len(json_data)-1]["username"]
	mod = float(float(I8)/float(I7) * 100)
	print mod
	width2 = 100-mod
	hrs = float(I7)-float(I8)
	text2.seek(0)
	json_data = json.dumps(json_data)	
	text2.close()
	return render_template('/Student_Page.html',mode="Student_Page",width=mod,a1=A4,a2=A5,a3=A6,b1=A7,b2=A8,b3=A9,c1=A10,c2=A11,c3=A12,a=IA,b=IB,c=IC,name=b, email=a, Focus=I1, G_GPA=I6, hrs=I8, left=hrs,width2=width2)


@app.route('/submit', methods=['POST'])
def Join_Now():
	copy = open("accounts.txt","r+")
	text2 = open("database.json","r+")
	email = str(request.form['email'])
	username = str(request.form['username'])
	if taken(email,text2) == True:
		copy.close()
		text2.close()
		return redirect("/Notify_NB.html")
	else:
		text2.seek(-1,2);
		copy.write("," + email+'-'+username+ "]");
		text2.write(',' + '{"email":"%s","username":"%s","focus":"","dob":"","class":"","gpa":"","goal_gpa":"","plan_hrs":"","hrs":"","ec1":"","ec2":"","ec3":"","week_goal_1":"", "week_goal_2":"", "week_goal_3":"","month_goal_1":"", "month_goal_2":"","month_goal_3":"","year_goal_1":"", "year_goal_2":"", "year_goal_3":"", "date":[], "duties":[], "time":[], "organization":[], "org_lead":[]}'% (email,username) + "]");
		copy.close()
		text2.close()
		return render_template('/Basic_Information.html', email=email, name=username)


@app.route('/submit2', methods=['POST'])
def Basic_Info():
	text2 = open("database.json","r+")
	I1 = str(request.form['focus'])
	I3 = str(request.form['Birth'])
	I4 = str(request.form['Class'])
	I5 = str(request.form['UPA'])  
	I6 = str(request.form['GPA'])
	I7 = str(request.form['CSH']) 
	I8 = str(request.form['hrs'])
	json_data  = json.loads(text2.read())
	json_data[len(json_data)-1]["focus"] = I1
	json_data[len(json_data)-1]["dob"] = I3
	json_data[len(json_data)-1]["class"] = I4
	json_data[len(json_data)-1]["gpa"] = I5
	json_data[len(json_data)-1]["goal_gpa"] = I6
	json_data[len(json_data)-1]["plan_hrs"] = I7
	json_data[len(json_data)-1]["hrs"] = I8
	a = json_data[len(json_data)-1]["email"] 
	b = json_data[len(json_data)-1]["username"]
	mod = float(float(I8)/float(I7) * 100)
	print mod
	width2 = 100-mod
	hrs = float(I7)-float(I8)
	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.truncate()
	text2.close()
	return render_template('/Student_Page.html',mode="submit2",width=mod, name=b, email=a, Focus=I1, G_GPA=I6, hrs=I8,left=hrs,width2=width2)

@app.route('/submit3',methods=['POST'])
def allGoals():
	text2 = open("database.json","r+")
	A4 = request.form['WG1']
	A5 = request.form['WG2']
	A6 = request.form['WG3']
	A7 = request.form['MG1']
	A8 = request.form['MG2']  
	A9 = request.form['MG3']
	A10 = request.form['YG1'] 
	A11 = request.form['YG2']
	A12 = request.form['YG3']
	json_data = json.loads(text2.read())
	json_data[len(json_data)-1]["week_goal_1"] = A4
	json_data[len(json_data)-1]["week_goal_2"] = A5
	json_data[len(json_data)-1]["week_goal_3"] = A6
	json_data[len(json_data)-1]["month_goal_1"] = A7
	json_data[len(json_data)-1]["month_goal_2"] = A8
	json_data[len(json_data)-1]["month_goal_3"] = A9
	json_data[len(json_data)-1]["year_goal_1"] = A10
	json_data[len(json_data)-1]["year_goal_2"] = A11
	json_data[len(json_data)-1]["year_goal_3"] = A12
	IA = json_data[len(json_data)-1]["ec1"]
	IB = json_data[len(json_data)-1]["ec2"] 
	IC = json_data[len(json_data)-1]["ec3"] 
	I1 = json_data[len(json_data)-1]["focus"] 
	I3 = json_data[len(json_data)-1]["dob"] 
	I4 = json_data[len(json_data)-1]["class"] 
	I5 = json_data[len(json_data)-1]["gpa"] 
	I6 = json_data[len(json_data)-1]["goal_gpa"] 
	I7 = json_data[len(json_data)-1]["plan_hrs"] 
	I8 = json_data[len(json_data)-1]["hrs"] 
	a = json_data[len(json_data)-1]["email"] 
	b = json_data[len(json_data)-1]["username"]
	mod = float(float(I8)/float(I7) * 100)
	print mod
	width2 = 100-mod
	hrs = float(I7)-float(I8)
	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.truncate()
	text2.close()
	return render_template('/Student_Page.html',mode="submit3.2",width=mod,a1=A4,a2=A5,a3=A6,b1=A7,b2=A8,b3=A9,c1=A10,c2=A11,c3=A12,a=IA,b=IB,c=IC,name=b, email=a, Focus=I1, G_GPA=I6, hrs=I8,left=hrs,width2=width2)
'''
@app.route('/submit3.1',methods=['POST'])
def Weekly_Goals():
	text2 = open("database.json","r+")
	A4 = request.form['WG1']
	A5 = request.form['WG2']
	A6 = request.form['WG3']
	json_data = json.loads(text2.read())
	A7 = json_data[len(json_data)-1]["month_goal_1"]
	A8 = json_data[len(json_data)-1]["month_goal_2"]
	A9 = json_data[len(json_data)-1]["month_goal_3"]
	A10 = json_data[len(json_data)-1]["year_goal_1"]
	A11 = json_data[len(json_data)-1]["year_goal_2"]
	A12 = json_data[len(json_data)-1]["year_goal_3"]
	json_data[len(json_data)-1]["week_goal_1"] = A4
	json_data[len(json_data)-1]["week_goal_2"] = A5
	json_data[len(json_data)-1]["week_goal_3"] = A6
	IA = json_data[len(json_data)-1]["ec1"]
	IB = json_data[len(json_data)-1]["ec2"] 
	IC = json_data[len(json_data)-1]["ec3"] 
	I1 = json_data[len(json_data)-1]["focus"] 
	I3 = json_data[len(json_data)-1]["dob"] 
	I4 = json_data[len(json_data)-1]["class"] 
	I5 = json_data[len(json_data)-1]["gpa"] 
	I6 = json_data[len(json_data)-1]["goal_gpa"] 
	I7 = json_data[len(json_data)-1]["plan_hrs"] 
	I8 = json_data[len(json_data)-1]["hrs"] 
	a = json_data[len(json_data)-1]["email"] 
	b = json_data[len(json_data)-1]["username"]
	mod = float(float(I8)/float(I7) * 100)
	print mod
	width2 = 100-mod
	hrs = float(I7)-float(I8)
	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.truncate()
	text2.close()
	return render_template('/Student_Page.html',mode="submit3.1",width=mod,a1=A4,a2=A5,a3=A6,b1=A7,b2=A8,b3=A9,c1=A10,c2=A11,c3=A12,a=IA,b=IB,c=IC,name=b, email=a, Focus=I1, G_GPA=I6, hrs=I8,left=hrs,width2=width2)

@app.route('/submit3.2',methods=['POST'])
def Monthly_Goals():
	text2 = open("database.json","r+")
	A7 = request.form['MG1']
	A8 = request.form['MG2']  
	A9 = request.form['MG3']
	json_data = json.loads(text2.read())
	A4 = json_data[len(json_data)-1]["week_goal_1"]
	A5 = json_data[len(json_data)-1]["week_goal_2"]
	A6 = json_data[len(json_data)-1]["week_goal_3"]
	json_data[len(json_data)-1]["month_goal_1"] = A7
	json_data[len(json_data)-1]["month_goal_2"] = A8
	json_data[len(json_data)-1]["month_goal_3"] = A9
	A10 = json_data[len(json_data)-1]["year_goal_1"]
	A11 = json_data[len(json_data)-1]["year_goal_2"]
	A12 = json_data[len(json_data)-1]["year_goal_3"]
	IA = json_data[len(json_data)-1]["ec1"]
	IB = json_data[len(json_data)-1]["ec2"] 
	IC = json_data[len(json_data)-1]["ec3"] 
	I1 = json_data[len(json_data)-1]["focus"] 
	I3 = json_data[len(json_data)-1]["dob"] 
	I4 = json_data[len(json_data)-1]["class"] 
	I5 = json_data[len(json_data)-1]["gpa"] 
	I6 = json_data[len(json_data)-1]["goal_gpa"] 
	I7 = json_data[len(json_data)-1]["plan_hrs"] 
	I8 = json_data[len(json_data)-1]["hrs"] 
	a = json_data[len(json_data)-1]["email"] 
	b = json_data[len(json_data)-1]["username"]
	mod = float(float(I8)/float(I7) * 100)
	print mod
	width2 = 100-mod
	hrs = float(I7)-float(I8)
	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.truncate()
	text2.close()
	return render_template('/Student_Page.html',mode="submit3.2",width=mod,a1=A4,a2=A5,a3=A6,b1=A7,b2=A8,b3=A9,c1=A10,c2=A11,c3=A12,a=IA,b=IB,c=IC,name=b, email=a, Focus=I1, G_GPA=I6, hrs=I8,left=hrs,width2=width2)

@app.route('/submit3.3',methods=['POST'])
def Yearly_Goals():
	text2 = open("database.json","r+")
	A10 = request.form['YG1'] 
	A11 = request.form['YG2']
	A12 = request.form['YG3']
	json_data = json.loads(text2.read())
	A4 = json_data[len(json_data)-1]["week_goal_1"]
	A5 = json_data[len(json_data)-1]["week_goal_2"]
	A6 = json_data[len(json_data)-1]["week_goal_3"]
	A7 = json_data[len(json_data)-1]["month_goal_1"]
	A8 = json_data[len(json_data)-1]["month_goal_2"]
	A9 = json_data[len(json_data)-1]["month_goal_3"]
	json_data[len(json_data)-1]["year_goal_1"] = A10
	json_data[len(json_data)-1]["year_goal_2"] = A11
	json_data[len(json_data)-1]["year_goal_3"] = A12
	IA = json_data[len(json_data)-1]["ec1"]
	IB = json_data[len(json_data)-1]["ec2"] 
	IC = json_data[len(json_data)-1]["ec3"] 
	I1 = json_data[len(json_data)-1]["focus"] 
	I3 = json_data[len(json_data)-1]["dob"] 
	I4 = json_data[len(json_data)-1]["class"] 
	I5 = json_data[len(json_data)-1]["gpa"] 
	I6 = json_data[len(json_data)-1]["goal_gpa"] 
	I7 = json_data[len(json_data)-1]["plan_hrs"] 
	I8 = json_data[len(json_data)-1]["hrs"] 
	a = json_data[len(json_data)-1]["email"] 
	b = json_data[len(json_data)-1]["username"]
	mod = float(float(I8)/float(I7) * 100)
	print mod
	width2 = 100-mod
	hrs = float(I7)-float(I8)
	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.truncate()
	text2.close()
	return render_template('/Student_Page.html',mode="submit3.3",width=mod,a1=A4,a2=A5,a3=A6,b1=A7,b2=A8,b3=A9,c1=A10,c2=A11,c3=A12,a=IA,b=IB,c=IC,name=b, email=a, Focus=I1, G_GPA=I6, hrs=I8,left=hrs,width2=width2)
	
'''
@app.route('/submit3.5',methods=['POST'])
def ECs():
	text2 = open("database.json","r+")
	IA = request.form['act1']
	IB = request.form['act2']
	IC = request.form['act3']
	json_data = json.loads(text2.read())
	json_data[len(json_data)-1]["ec1"] = IA
	json_data[len(json_data)-1]["ec2"] = IB
	json_data[len(json_data)-1]["ec3"] = IC
	I1 = json_data[len(json_data)-1]["focus"] 
	I3 = json_data[len(json_data)-1]["dob"] 
	I4 = json_data[len(json_data)-1]["class"] 
	I5 = json_data[len(json_data)-1]["gpa"] 
	I6 = json_data[len(json_data)-1]["goal_gpa"] 
	I7 = json_data[len(json_data)-1]["plan_hrs"] 
	I8 = json_data[len(json_data)-1]["hrs"] 
	a = json_data[len(json_data)-1]["email"] 
	b = json_data[len(json_data)-1]["username"]
	mod = float(float(I8)/float(I7) * 100)
	print mod
	width2 = 100-mod
	hrs = float(I7)-float(I8)
	text2.seek(0)
	data = json.dumps(json_data)
	text2.write(data);
	text2.truncate()
	text2.close()
	return render_template("/Student_Page.html",width=mod,mode="submit3.5",a=IA,b=IB,c=IC, name=b, email=a, Focus=I1, G_GPA=I6, left=hrs,width2=width2, hrs=I8)
	

@app.route('/submit4',methods=['POST'])
def CS_Goal():
	text2 = open("database.json","r+")
	I6 = request.form['CSH'] 
	json_data = json.loads(text2.read())
	json_data[len(json_data)-1]["plan_hrs"] = I6 	
	current = json_data[len(json_data)-1]["hrs"]
	hrs = json_data[len(json_data)-1]["plan_hrs"] 
	name = json_data[len(json_data)-1]["username"]
	email = json_data[len(json_data)-1]["email"]
	date = json_data[len(json_data)-1]["date"] 
	duties = json_data[len(json_data)-1]["duties"]
	time = json_data[len(json_data)-1]["time"] 
	organization = json_data[len(json_data)-1]["organization"] 
	organization_leader = json_data[len(json_data)-1]["org_lead"] 
	percentage = float(float(current)/float(hrs)*100)
	difference = 100 - percentage
	last = float(hrs) - float(current)

	# search contents for entry that is associated with community service info
   	template_data = fetch()

   	# build data_object for all items that will be using in template
   	data_object = { "name":name, "email":email, "current_hrs":current, "last":last, "goal":hrs, "percentage":percentage, "difference":difference, "date":date, "duties":duties, "time":time, "organization":organization, "org_lead":organization_leader}

   	intlist = []
   	for x in range(len(template_data["date"])):
		#print template_data["date"][x]
		intlist.append(x)
	print intlist

	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.truncate()
	text2.close()
	return render_template("/Community_Service.html",mode="/submit4", intlist=intlist, data=data_object, template_data=template_data)

@app.route('/submit4.5',methods=['POST'])
def Comm_Serv():
	text2 = open("database.json","r+")
	I1 = request.form['Date'] 
	I2 = request.form['Duties'] 
	I3 = request.form['Time'] 
	I4 = request.form['Organization'] 
	I5 = request.form['OrgLead'] 

	json_data = json.loads(text2.read())

	json_data[len(json_data)-1]["date"].append(I1)
	json_data[len(json_data)-1]["duties"].append(I2)
	json_data[len(json_data)-1]["time"].append(I3)
	json_data[len(json_data)-1]["organization"].append(I4)
	json_data[len(json_data)-1]["org_lead"].append(I5)
	print len(json_data),(len(json_data)-1)
	print "\n%s\n"%(json_data[len(json_data)-1])

	date = json_data[len(json_data)-1]["date"] 
	duties = json_data[len(json_data)-1]["duties"]
	time = json_data[len(json_data)-1]["time"]
	increment = str(float(json_data[len(json_data)-1]["hrs"]) + float(I3))
	json_data[len(json_data)-1]["hrs"] = increment
	current = json_data[len(json_data)-1]["hrs"] 
	hrs = json_data[len(json_data)-1]["plan_hrs"] 
	name = json_data[len(json_data)-1]["username"]
	email = json_data[len(json_data)-1]["email"]
	organization = json_data[len(json_data)-1]["organization"] 
	organization_leader = json_data[len(json_data)-1]["org_lead"] 
	percentage = float(float(current)/float(hrs)*100)
	difference = 100 - percentage
	last = float(hrs) - float(current)


	# search contents for entry that is associated with community service info
   	template_data = fetch()

   	# build data_object for all items that will be using in template
   	data_object = { "name":name, "email":email, "current_hrs":current, "last":last, "goal":hrs, "percentage":percentage, "difference":difference, "date":date, "duties":duties, "time":time, "organization":organization, "org_lead":organization_leader}

   	intlist = []
   	x=0
   	for x in range(len(template_data["date"])-1):
		print template_data["date"][x]
		intlist.append(x)
	print intlist

	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.truncate()
	text2.close()
	return render_template("/Community_Service.html", mode="/submit4.5", intlist=intlist, data=data_object, template_data=template_data)

@app.route('/submit5',methods=['POST'])
def SignIn():
	text2 = open("database.json","r+")
	email = str(request.form['email'])
	name = str(request.form['username'])
	json_data = json.loads(text2.read())
	for y in range(1,len(json_data)):
		if email != str(json_data[y]["email"]) and name != str(json_data[y]["username"]):
			text2.close()
			return redirect("/Notify_SignIn.html")
		else:
			if email == str(json_data[y]["email"]) and name == str(json_data[y]["username"]):
				text2.write(',' + '{"email":"%s","username":"","focus":"","dob":"","class":"","gpa":"","goal_gpa":"","plan_hrs":"","hrs":"","ec1":"","ec2":"","ec3":"","week_goal_1":"", "week_goal_2":"", "week_goal_3":"","month_goal_1":"", "month_goal_2":"","month_goal_3":"","year_goal_1":"", "year_goal_2":"", "year_goal_3":"", "date":[], "duties":[], "time":[], "organization":[], "org_lead":[]}'% (email) + "]");

	    		json_data[len(json_data)-1]["username"] = json_data[y]["username"] 
	    		json_data[len(json_data)-1]["focus"] = json_data[y]["focus"] 
	    		json_data[len(json_data)-1]["dob"] = json_data[y]["dob"] 
	    		json_data[len(json_data)-1]["class"] = json_data[y]["class"] 
	    		json_data[len(json_data)-1]["gpa"] = json_data[y]["gpa"] 
	    		json_data[len(json_data)-1]["goal_gpa"] = json_data[y]["goal_gpa"] 
	    		json_data[len(json_data)-1]["plan_hrs"] = json_data[y]["plan_hrs"] 
	    		json_data[len(json_data)-1]["hrs"] = json_data[y]["hrs"] 
	    		json_data[len(json_data)-1]["week_goal_1"] = json_data[y]["week_goal_1"] 
	    		json_data[len(json_data)-1]["week_goal_2"] = json_data[y]["week_goal_2"] 
	    		json_data[len(json_data)-1]["week_goal_3"] = json_data[y]["week_goal_3"] 
	    		json_data[len(json_data)-1]["month_goal_1"] = json_data[y]["month_goal_1"] 
	    		json_data[len(json_data)-1]["month_goal_2"] = json_data[y]["month_goal_2"] 
	    		json_data[len(json_data)-1]["month_goal_3"] = json_data[y]["month_goal_3"] 
	    		json_data[len(json_data)-1]["year_goal_1"] = json_data[y]["year_goal_1"] 
	    		json_data[len(json_data)-1]["year_goal_2"] = json_data[y]["year_goal_2"] 
	    		json_data[len(json_data)-1]["year_goal_3"] = json_data[y]["year_goal_3"] 
	    		json_data[len(json_data)-1]["ec1"] = json_data[y]["ec1"] 
	    		json_data[len(json_data)-1]["ec2"] = json_data[y]["ec2"] 
	    		json_data[len(json_data)-1]["ec3"] = json_data[y]["ec3"] 
	    		json_data[len(json_data)-1]["email"] = json_data[y]["email"] 
	    		json_data[len(json_data)-1]["date"] = json_data[y]["date"] 
	    		json_data[len(json_data)-1]["duties"] = json_data[y]["duties"] 
	    		json_data[len(json_data)-1]["time"] = json_data[y]["time"] 
	    		json_data[len(json_data)-1]["organization"] = json_data[y]["organization"] 
	    		json_data[len(json_data)-1]["org_lead"] = json_data[y]["org_lead"]

	    		A4 = json_data[y]["week_goal_1"]
	    		A5 = json_data[y]["week_goal_2"]
	    		A6 = json_data[y]["week_goal_3"]
	    		A7 = json_data[y]["month_goal_1"]
	    		A8 = json_data[y]["month_goal_2"]
	    		A9 = json_data[y]["month_goal_3"]
	    		A10 = json_data[y]["year_goal_1"]
	    		A11 = json_data[y]["year_goal_2"]
	    		A12 = json_data[y]["year_goal_3"]
	    		IA = json_data[y]["ec1"]
	    		IB = json_data[y]["ec2"]
	    		IC = json_data[y]["ec3"]
	    		I1 = json_data[y]["focus"]
	    		I3 = json_data[y]["dob"]
	    		I4 = json_data[y]["class"]
	    		I5 = json_data[y]["gpa"]
	    		I6 = json_data[y]["goal_gpa"]
	    		I7 = json_data[y]["plan_hrs"]
	    		I8 = json_data[y]["hrs"]
	    		a = json_data[y]["email"]
	    		b = json_data[y]["username"]
	    		email = json_data[y]["email"]
	    		date = json_data[y]["date"]
	    		duties = json_data[y]["duties"]
	    		time = json_data[y]["time"]
	    		organization = json_data[y]["organization"]
	    		organization_leader = json_data[y]["org_lead"]

	    		mod = float(float(I8)/float(I7) * 100)
	    		print mod
	    		width2 = 100-mod
	    		hrs = float(I7)-float(I8)
	    		text2.seek(0)
	    		json_data = json.dumps(json_data)
	    		text2.write(json_data);
	    		text2.truncate()
	    		text2.close()
	    		return render_template('/Student_Page.html',mode="Student_Page",width=mod,a1=A4,a2=A5,a3=A6,b1=A7,b2=A8,b3=A9,c1=A10,c2=A11,c3=A12,a=IA,b=IB,c=IC,name=b, email=a, Focus=I1, G_GPA=I6, hrs=I8, left=hrs,width2=width2)

	  


@app.route('/submit6', methods=['POST'])
def handle():
    f_name = request.form['C_name']
    f_email = request.form['email_add']
    f_concern = request.form['Worry']

    print "\t\t\t **** f_name= %s" % f_name
    print "\t\t\t **** f_email= %s" % f_email
    print "\t\t\t **** f_concern= %s" % f_concern

    json_return = ''

    json_return = {'success': True, 'message':'Thank you ' + f_name + ' , we will contact you shortly'}


    return json.dumps(json_return)

@app.route('/hello/<email>',  methods=['POST'])
def hello(name=None):
	email = request.form['email']
	return render_template('hello.html', email=email)



if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')




