import json

from flask import Flask, request, redirect, render_template
app = Flask(__name__)

path = []
def notify():
	return '<title>Capacity</title>\
    <meta name="viewport" content="width=device-width, initial-scale=1.0">\
    <!-- Bootstrap -->\
    <link href="css/bootstrap.css" rel="stylesheet" media="screen">\
    <script src="js/holder.js"></script>\
    <div class="alert alert-dangerous alert-dismissible" role="alert">\
  <button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>\
  <strong>Sorry, but this email has already been taken.\
</div>'

@app.route('/submit', methods=['POST'])
def Join_Now():
	scripture = open("accounts.txt", "a+")
	I1 = request.form['EmailInput1'] 
	I2 = request.form['Nickname'] 
	data = [{'email':(I1)}, {'nickname':(I2)}, {'next'}]
	if str(I1) in open('info.txt').read():
		return redirect("http://localhost:8888/Capacity/Notified_New_Beginnings.html#notify", code=302)
	else:
		info = json.dumps(data)
		scripture.write(info);
		scripture.close()
		return redirect("http://localhost:8888/Capacity/Basic_Information.html", code=302)

@app.route('/submit2', methods=['POST'])
def Basic_Info():
	scripture = open("user_info.txt", "a+")
	I1 = request.form['focus'] 
	I3 = request.form['Birth'] 
	I4 = request.form['Class'] 
	I5 = request.form['UPA']  
	I6 = request.form['GPA'] 
	I7 = request.form['CSH'] 
	data = [{'focus':(I1)}, {'dob':(I3)}, {'class':(I4)}, {'gpa':(I5)}, {'gpa_goal':(I6)}, {'community_service_goal':(I7)}]
	info = json.dumps(data)
	scripture.write(info);
	scripture.close()
	return redirect("http://localhost:8888/Capacity/Student_Page.html", code=302)

@app.route('/submit3',methods=['POST'])
def Personal_Goals():
	scripture = open("goals.txt", "a+")
	I4 = request.form['WG1'] 
	I5 = request.form['WG2'] 
	I6 = request.form['WG3'] 
	I7 = request.form['MG1'] 
	I8 = request.form['MG2'] 
	I9 = request.form['MG3'] 
	I10 = request.form['YG1'] 
	I11 = request.form['YG2'] 
	I12 = request.form['YG3'] 

	data = [{'week_goal_1':(I4)}, {'week_goal_2':(I5)}, {'week_goal_3':(I6)},{'month_goal_1':(I7)}, {'month_goal_2':(I8)}, {'month_goal_3':(I9)},{'year_goal_1':(I10)}, {'year_goal_2':(I11)}, {'Year_goal_3':(I12)}]
	info = json.dumps(data)
	scripture.write(info);
	scripture.close()
	return redirect("http://localhost:8888/Capacity/Community_Service.html", code=302)

@app.route('/submit3.5',methods=['POST'])
def ECs():
	scripture = open("extra_curriculars.txt", "a+")
	I1 = request.form['act1'] 
	I2 = request.form['act2'] 
	I3 = request.form['act3'] 

	data = [{'extra_curricular_1':(I1)}, {'extra_curricular_2':(I2)}, {'extra_curricular_3':(I3)}]
	info = json.dumps(data)
	scripture.write(info);
	scripture.close()
	return redirect("http://localhost:8888/Capacity/Community_Service.html", code=302)

@app.route('/submit4',methods=['POST'])
def CS_Goals():
	scripture = open("goals.txt", "a+")
	I6 = request.form['Wk1'] 
	I7 = request.form['Wk2'] 
	I8 = request.form['Wk3'] 
	I9 = request.form['M1'] 
	I10 = request.form['M2'] 
	I11 = request.form['M3'] 
	I12 = request.form['Y1'] 
	I13 = request.form['Y2'] 
	I14 = request.form['Y3'] 

	data = [{'wk1':(I6)}, {'wk2':(I7)}, {'wk3':(I8)}, {'m1':(I9)}, {'m2':(I10)}, {'m3':(I11)}, {'y1':(I12)}, {'y2':(I13)}, {'y3':(I14)}]
	info = json.dumps(data)
	scripture.write(info);
	scripture.close()
	return redirect("http://localhost:8888/Capacity/Sign_In.html", code=302)

@app.route('/submit4.5',methods=['POST'])
def Comm_Serv():
	scripture = open("community_service.txt", "a+")
	I1 = request.form['Date'] 
	I2 = request.form['Duties'] 
	I3 = request.form['Time'] 
	I4 = request.form['Organization'] 
	I5 = request.form['OrgLead'] 

	data = [{'date':(I1)}, {'duties':(I2)}, {'time':(I3)}, {'organization':(I4)}, {'org_lead':(I5)}]
	info = json.dumps(data)
	scripture.write(info);
	scripture.close()
	return redirect("http://localhost:8888/Capacity/Sign_In.html", code=302)

@app.route('/submit5',methods=['POST'])
def Sign_In():
	scripture = open("accounts.txt", "a+")
	I1 = request.form['EmailInput2'] 
	I2 = request.form['name'] 
	data = [{'email':(I1)}, {'nickname':(I2)}]
	info = json.dumps(data)
	scripture.write(info);
	scripture.close()
	return redirect("http://localhost:8888/Capacity/Student_Page.html", code=302)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



if __name__ == "__main__":
	app.debug = True
	app.run('0.0.0.0')







