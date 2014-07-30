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

	gather = I1+I2+I3+I4+I5+I6+i7
	return gather
if __name__ == "__main__":
	app.debug = True
	app.run('0.0.0.0')
