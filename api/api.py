from flask import Flask, request
app = Flask(__name__)



@app.route('/submit', methods=['POST'])
def info():
	I1 = request.form['EmailInput1'] + "<br><br>"

	gather = I1
	return gather + "<a href='http://localhost:8888/Capacity/Basic_Information.html'>Next</a>"

@app.route('/submit2', methods=['POST'])
def info2():
	I1 = request.form['focus'] + "<br><br>"
	I2 = request.form['Username'] + "<br><br>"
	I3 = request.form['Birth'] + "<br><br>"
	I4 = request.form['Class'] + "<br><br>"
	I5 = request.form['UPA'] + "<br><br>"
	I6 = request.form['GPA'] + "<br><br>"
	I7 = request.form['CSH'] + "<br><br>"

	gather = I1+I2+I3+I4+I5+I6+I7 + "<a href='http://localhost:8888/Capacity/Student_Page.html'>Next</a>"
	return gather

@app.route('/submit3',methods=['POST'])
def info3():
	I1 = request.form['act1'] + "<br><br>"
	I2 = request.form['act2'] + "<br><br>"
	I3 = request.form['WG1'] + "<br><br>"
	I4 = request.form['WG2'] + "<br><br>"
	I5 = request.form['MG1'] + "<br><br>"
	I6 = request.form['MG2'] + "<br><br>"
	I7 = request.form['YG1'] + "<br><br>"
	I8 = request.form['YG2'] + "<br><br>"

	gather = I1+I2+I3+I4+I5+I6+I7+I8 + "<a href='http://localhost:8888/Capacity/Community_Service.html'>Next</a>"
	return gather

@app.route('/submit4',methods=['POST'])
def info4():
	I1 = request.form['Date'] + "<br><br>"
	I2 = request.form['Duties'] + "<br><br>"
	I3 = request.form['Time'] + "<br><br>"
	I4 = request.form['Organization'] + "<br><br>"
	I5 = request.form['OrgLead'] + "<br><br>"
	I6 = request.form['Wk1'] + "<br><br>"
	I7 = request.form['Wk2'] + "<br><br>"
	I8 = request.form['Wk3'] + "<br><br>"
	I9 = request.form['M1'] + "<br><br>"
	I10 = request.form['M2'] + "<br><br>"
	I11 = request.form['M3'] + "<br><br>"
	I12 = request.form['Y1'] + "<br><br>"
	I13 = request.form['Y2'] + "<br><br>"
	I14 = request.form['Y3'] + "<br><br>"

	gather = I1+I2+I3+I4+I5+I6+I7+I8+I9+I10+I11+I12+I13+I14 + "<a href='http://localhost:8888/Capacity/Sign_In.html'>Next</a>"
	return gather

@app.route('/submit5',methods=['POST'])
def info5():
	I1 = request.form['EmailInput2'] + "<br><br>"
	I2 = request.form['name'] + "<br><br>"
	gather = I1+I2 + "<a href='http://localhost:8888/Capacity/Us.html'>Next</a>"
	return gather

@app.route('/submit6',methods=['POST'])
def info6():

	gather = "<a href='http://localhost:8888/Capacity/New_Beginnings.html.html'>Home</a>"
	return gather

if __name__ == "__main__":
	app.debug = True
	app.run('0.0.0.0')
