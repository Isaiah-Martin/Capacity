import json

from flask import Flask, request, redirect, render_template
app = Flask(__name__)

scripture = open("info.txt", "a+")
info = {}
data = []
@app.route('/submit', methods=['POST'])
def info():
	global info
	global data
	global scripture
	I1 = request.form['EmailInput1'] 
	I2 = request.form['Nickname'] 
	data = [{'Email':'%s'%(I1)}, {'Nickname':'%s'%(I2)}]
	info = json.dumps(data)
	return render_template("http://localhost:8888/Capacity/Basic_Information.html",EmailInput1=I1,Nickname=I2)

data = data
@app.route('/submit2', methods=['POST'])
def info2():
	global info
	global data
	I1 = request.form['focus'] 
	I3 = request.form['Birth'] 
	I4 = request.form['Class'] 
	I5 = request.form['UPA']  
	I6 = request.form['GPA'] 
	I7 = request.form['CSH'] 
	data = data + [{'Focus':'%s'%(I1)}, {'DOB':'%s'%(I3)}, {'Class':'%s'%(I4)}, {'GPA':'%s'%(I5)}, {'GPA_Goal':'%s'%(I6)}, {'Community_Service_Goal':'%s'%(I7)}]
	info = json.dumps(data, sort_keys=True)
	return redirect("http://localhost:8888/Capacity/Student_Page.html", code=302)

data = data
@app.route('/submit3',methods=['POST'])
def info3():
	global info
	global data
	I1 = request.form['act1'] 
	I2 = request.form['act2'] 
	I3 = request.form['act3'] 
	I3 = request.form['WG1'] 
	I4 = request.form['WG2'] 
	I5 = request.form['WG3'] 
	I6 = request.form['MG1'] 
	I7 = request.form['MG2'] 
	I8 = request.form['MG3'] 
	I9 = request.form['YG1'] 
	I10 = request.form['YG2'] 
	I11 = request.form['YG3'] 

	data = data + [{'Extra_Curricular_1':'%s'%(I1)}, {'Extra_Curricular_2':'%s'%(I2)}, {'Week_Goal_1':'%s'%(I3)}, {'Week_Goal_2':'%s'%(I4)}, {'Week_Goal_3':'%s'%(I5)},{'Month_Goal_1':'%s'%(I6)}, {'Month_Goal_2':'%s'%(I7)}, {'Month_Goal_3':'%s'%(I8)},{'Year_Goal_1':'%s'%(I9)}, {'Year_Goal_2':'%s'%(I10)}, {'Year_Goal_3':'%s'%(I11)}]
	info = json.dumps(data, sort_keys=True)
	return redirect("http://localhost:8888/Capacity/Community_Service.html", code=302)

data = data
@app.route('/submit4',methods=['POST'])
def info4():
	global info
	global data
	I1 = request.form['Date'] 
	I2 = request.form['Duties'] 
	I3 = request.form['Time'] 
	I4 = request.form['Organization'] 
	I5 = request.form['OrgLead'] 
	I6 = request.form['Wk1'] 
	I7 = request.form['Wk2'] 
	I8 = request.form['Wk3'] 
	I9 = request.form['M1'] 
	I10 = request.form['M2'] 
	I11 = request.form['M3'] 
	I12 = request.form['Y1'] 
	I13 = request.form['Y2'] 
	I14 = request.form['Y3'] 

	data = data + [{'Date':'%s'%(I1)}, {'Duties':'%s'%(I2)}, {'Time':'%s'%(I3)}, {'Organization':'%s'%(I4)}, {'OrgLead':'%s'%(I5)}, {'Wk1':'%s'%(I6)}, {'Wk2':'%s'%(I7)}, {'Wk3':'%s'%(I8)}, {'M1':'%s'%(I9)}, {'M2':'%s'%(I10)}, {'M3':'%s'%(I11)}, {'Y1':'%s'%(I12)}, {'Y2':'%s'%(I13)}, {'Y3':'%s'%(I14)}]
	info = json.dumps(data, sort_keys=True)
	return redirect("http://localhost:8888/Capacity/Sign_In.html", code=302)

data = data
@app.route('/submit5',methods=['POST'])
def info5():
	global info
	global data
	I1 = request.form['EmailInput2'] 
	I2 = request.form['name'] 
	data = data + [{'Email':'%s'%(I1)}, {'Nickname':'%s'%(I2)}]
	info = json.dumps(data, sort_keys=True)
	scripture.write(info);
	scripture.close()
	return info

if __name__ == "__main__":
	app.debug = True
	app.run('0.0.0.0')







