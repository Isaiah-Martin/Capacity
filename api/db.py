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
		text2.write(',' + '{"email":"%s","nickname":"%s","focus":"c","dob":"d","class":"e","gpa":"f","goal_gpa":"g","plan_hrs":"h","extra_curricular":[],"week_goal_1":"j", "week_goal_2":"k", "week_goal_3":"l","month_goal_1":"m", "month_goal_2":"n","month_goal_3":"o","year_goal_1":"p", "year_goal_2":"q", "year_goal_3":"r", "date":"t", "duties":"s", "time":"w", "organization":"x", "org_lead":"z"}'% (email,nickname) + ']');
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
	json_data = json.loads(text2.read())
	json_data[len(json_data)-1]["focus"] = I1
	json_data[len(json_data)-1]["dob"] = I3
	json_data[len(json_data)-1]["class"] = I4
	json_data[len(json_data)-1]["gpa"] = I5
	json_data[len(json_data)-1]["goal_gpa"] = I6
	json_data[len(json_data)-1]["plan_hrs"] = I7
	a = json_data[len(json_data)-1]["email"] 
	b = json_data[len(json_data)-1]["nickname"]
	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.close()
	return render_template('/Student_Page.html', name=b, email=a, Focus=I1, G_GPA=I6, total='0',hrs=I7)

@app.route('/submit3',methods=['POST'])
def Personal_Goals():
	text2 = open("database.json","r+")
	I4 = str(request.form['WG1']) 
	I5 = str(request.form['WG2'])
	I6 = str(request.form['WG3'])
	I7 = str(request.form['MG1'])
	I8 = str(request.form['MG2'])  
	I9 = str(request.form['MG3'])
	I10 = str(request.form['YG1']) 
	I11 = str(request.form['YG2'])
	I12 = str(request.form['YG3'])
	json_data = json.loads(text2)
	json_data[len(json_data)-1]["week_goal_1"] = I4
	json_data[len(json_data)-1]["week_goal_2"] = I5
	json_data[len(json_data)-1]["week_goal_3"] = I6
	json_data[len(json_data)-1]["month_goal_1"] = I7
	json_data[len(json_data)-1]["month_goal_2"] = I8
	json_data[len(json_data)-1]["month_goal_3"] = I9
	json_data[len(json_data)-1]["year_goal_1"] = I10
	json_data[len(json_data)-1]["year_goal_2"] = I11
	json_data[len(json_data)-1]["year_goal_3"] = I12
	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.close()
	return redirect("http://localhost:8888/Capacity/Student_Page.html", code=302)

@app.route('/submit3.5',methods=['POST'])
def ECs():
	text2 = open("database.json","r+")
	IA = request.form['act1']
	json_data = json.loads(text2.read())
	IA = IA + json_data[len(json_data)-1]["extra_curricular"]
	json_data[len(json_data)-1]["extra_curricular"] = IA
	I1 = json_data[len(json_data)-1]["focus"] 
	I3 = json_data[len(json_data)-1]["dob"] 
	I4 = json_data[len(json_data)-1]["class"] 
	I5 = json_data[len(json_data)-1]["gpa"] 
	I6 = json_data[len(json_data)-1]["goal_gpa"] 
	I7 = json_data[len(json_data)-1]["plan_hrs"] 
	a = json_data[len(json_data)-1]["email"] 
	b = json_data[len(json_data)-1]["nickname"]
	text2.seek(0)
	data = json.dumps(json_data)
	text2.write(data);
	return render_template("/Student_Page.html",vlist=json_data[len(json_data)-1]["extra_curricular"], name=b, email=a, Focus=I1, G_GPA=I6, total='0',hrs=I7, act=IA)
	text2.close()

@app.route('/submit4',methods=['POST'])
def CS_Goal():
	text2 = open("database.json","r+")
	I6 = request.form['CSH'] 
	json_data = json.loads(text2)
	json_data[len(json_data)-1]["plan_hrs"] = I1 
	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.close()
	return redirect("http://localhost:8888/Capacity/Community_Service.html", code=302)

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
	text2.seek(0)
	json_data = json.dumps(json_data)
	text2.write(json_data);
	text2.close()
	return redirect("http://localhost:8888/Capacity/Community_Service.html", code=302)

@app.route('/submit5',methods=['POST'])
def Sign_In():
	copy = open("accounts.txt","r+")
	text2 = open("database.json","r+")
	json_data = json.loads(text2)
	text2.seek(-1,2);
	email = str(request.form['email'])
	nickname = str(request.form['nickname'])
	if taken(email,open("accounts.txt").read()) == True:
		return redirect("http://localhost:8888/Capacity/Sign_In.html")
	else:
		for x in len(text2.read()):
			if text2.read(x) == json_data[x]["email"][0]:
				text2.seek(x)
				return redirect("http://localhost:8888/Capacity/Basic_Information.html")
	copy.close()
	text2.close()   


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




