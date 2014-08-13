__author__ = 'Isaiah'

from flask import Flask, request, redirect, render_template
app = Flask(__name__, static_url_path='')

import json

def taken(v_obj,v_area):
	if v_obj in v_area:
		return True
	return False

@app.route('/submit', methods=['POST'])
def Join_Now():
	copy = open("accounts.txt","r+")
	text2 = open("database.json","r+")
	text2.seek(-1,2);
	email = str(request.form['email'])
	nickname = str(request.form['nickname'])
	if taken(email,open("accounts.txt").read()) == True:
		return redirect("/New_Beginnings.html")
	else:
		text2.write(',' + '{"email":"%s","nickname":"%s","focus":"c","dob":"d","class":"e","gpa":"f","goal_gpa":"g","plan_hrs":"h","hrs":"zx","ec1":"i","ec2":"i2","ec3":"i3","week_goal_1":"j", "week_goal_2":"k", "week_goal_3":"l","month_goal_1":"m", "month_goal_2":"n","month_goal_3":"o","year_goal_1":"p", "year_goal_2":"q", "year_goal_3":"r", "date":"t", "duties":"s", "time":"w", "organization":"x", "org_lead":"z"}'% (email,nickname) + ']');
		return render_template('/Basic_Information.html', email=email, name=nickname)
	copy.close()
	text2.close()


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
	json_data = json.loads(text2.read())
	json_data[len(json_data)-1]["focus"] = I1
	json_data[len(json_data)-1]["dob"] = I3
	json_data[len(json_data)-1]["class"] = I4
	json_data[len(json_data)-1]["gpa"] = I5
	json_data[len(json_data)-1]["goal_gpa"] = I6
	json_data[len(json_data)-1]["plan_hrs"] = I7
	json_data[len(json_data)-1]["hrs"] = I8
	a = json_data[len(json_data)-1]["email"] 
	b = json_data[len(json_data)-1]["nickname"]
	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.close()
	return render_template('/Student_Page.html', name=b, email=a, Focus=I1, G_GPA=I6, total=I8,hrs=I7)

@app.route('/submit3',methods=['POST'])
def Personal_Goals():
	text2 = open("database.json","r+")
	A4 = str(request.form['WG1']) 
	A5 = str(request.form['WG2'])
	A6 = str(request.form['WG3'])
	A7 = str(request.form['MG1'])
	A8 = str(request.form['MG2'])  
	A9 = str(request.form['MG3'])
	A10 = str(request.form['YG1']) 
	A11 = str(request.form['YG2'])
	A12 = str(request.form['YG3'])
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
	a = json_data[len(json_data)-1]["email"] 
	b = json_data[len(json_data)-1]["nickname"]
	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.close()
	return render_template('/Student_Page.html',a1=A4,a2=A5,a3=A6,b1=A7,b2=A8,b3=A9,c1=A10,c2=A11,c3=A12, name=b, email=a, Focus=I1, G_GPA=I6, total=I8,hrs=I7)

	

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
	b = json_data[len(json_data)-1]["nickname"]
	text2.seek(0)
	data = json.dumps(json_data)
	text2.write(data);
	text2.close()
	return render_template("/Student_Page.html",a=IA,b=IB,c=IC, name=b, email=a, Focus=I1, G_GPA=I6, total=I8,hrs=I7)
	

@app.route('/submit4',methods=['POST'])
def CS_Goal():
	text2 = open("database.json","r+")
	I6 = request.form['CSH'] 
	json_data = json.loads(text2)
	json_data[len(json_data)-1]["plan_hrs"] = I6 
	a = json_data[len(json_data)-1]["hrs"]
	b = json_data[len(json_data)-1]["nickname"]
	json_data = json.loads(text2)
	A1 = json_data[len(json_data)-1]["date"] 
	A2 = json_data[len(json_data)-1]["duties"]
	A3 = json_data[len(json_data)-1]["time"] 
	A4 = json_data[len(json_data)-1]["organization"] 
	A5 = json_data[len(json_data)-1]["org_lead"] 
	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.close()
	return render_template("/Community_Service.html", name=b, tot=a, max=I6, ol=A5, date=A1, duties=A2, time=A3, org= A4, goal=I6)


@app.route('/submit4.5',methods=['POST'])
def Comm_Serv():
	text2 = open("database.json","r+")
	I1 = request.form['Date'] 
	I2 = request.form['Duties'] 
	I3 = request.form['Time'] 
	I4 = request.form['Organization'] 
	I5 = request.form['OrgLead'] 
	json_data = json.loads(text2)
	json_data[len(json_data)-1]["date"] = I1 
	json_data[len(json_data)-1]["duties"] = I2
	json_data[len(json_data)-1]["time"] = I3
	json_data[len(json_data)-1]["organization"] = I4
	json_data[len(json_data)-1]["org_lead"] = I5
	a = json_data[len(json_data)-1]["hrs"]
	b = json_data[len(json_data)-1]["nickname"]
	c = json_data[len(json_data)-1]["plan_hrs"]
	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.close()
	return render_template("/Community_Service.html",name=b, tot=a, max=c, ol=I5, date=I1, duties=I2, time=I3, org= I4, goal=c)

@app.route('/submit5',methods=['POST'])
def Sign_In():
	copy = open("accounts.txt","r+")
	text2 = open("database.json","r+")
	json_data = json.loads(text2)
	text2.seek(-1,2);
	email = str(request.form['email'])
	nickname = str(request.form['nickname'])
	json_data = json.loads(text2.read())
	if taken(email,open("accounts.txt").read()) == True:
		for x in len(text2.read()):
			for y in len(json_data):
				if email == json_data[y]["email"]:
					A4 = json_data[len(json_data)-1]["week_goal_1"] 
					A5 = json_data[len(json_data)-1]["week_goal_2"]
					A6 = json_data[len(json_data)-1]["week_goal_3"]
					A7 = json_data[len(json_data)-1]["month_goal_1"]
					A8 = json_data[len(json_data)-1]["month_goal_2"]
					A9 = json_data[len(json_data)-1]["month_goal_3"]
					A10 = json_data[len(json_data)-1]["year_goal_1"]
					A11 = json_data[len(json_data)-1]["year_goal_2"]
					A12 = json_data[len(json_data)-1]["year_goal_3"]
					IA = json_data[y]["ec1"] 
					IB = json_data[y]["ec2"] 
					IC = json_data[y]["ec3"]
					I1 = json_data[y]["focus"] 
					I2 = json_data[y]["dob"] 
					I3 = json_data[y]["class"] 
					I4 = json_data[y]["gpa"]
					I5 = json_data[y]["goal_gpa"]
					I6 = json_data[y]["plan_hrs"] 
					I7 = json_data[y]["hrs"] 
					a = json_data[y]["email"] 
					b = json_data[y]["nickname"]
					text2.close() 
					return render_template("/Student_Page.html",a=IA,b=IB,c=IC, name=b, email=a, Focus=I1, G_GPA=I5, total=I7,hrs=I6,a1=A4,a2=A5,a3=A6,b1=A7,b2=A8,b3=A9,c1=A10,c2=A11)
	else:
		text2.close() 
		return redirect("/Sign_In.html")
	
	  


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


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



if __name__ == "__main__":
	app.debug = True
	app.run('0.0.0.0')




