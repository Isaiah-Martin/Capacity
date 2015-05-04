def year(grade):
	seg=1.00
	if grade=="freshman":
		seg+=0.00
	elif grade=="half-freshman":
		seg+=0.50
	elif grade=="sophomore":
		seg+=1.00
	elif grade=="half-sophomore":
		seg+=1.50
	elif grade=="junior":
		seg+=2.00
	elif grade=="half-junior":
		seg+=2.50
	elif grade=="senior":
		seg+=3.00
	elif grade=="half-senior":
		seg+=3.50
	else:
		seg+=0.00
	return seg

#MaxGPA(grade, current_gpa, semester):
#add a feature that calculates the maximum gpa the student have by a given amount 
#of time for the given gpa ( ex input = 3.0 by 2 semesters; max gpa=x )

# class = sophomore
# current_gpa =  2.56
# semester = 5.00
#  logic:
#	((current_gpa*sophomore)+(4.00*semester))/(semester+sophomore) 
#print  ((2.56*2)+(4.00*5.00))/(5.00+2.00) 

def MaxGPA(grade, current_gpa, semester):
	seg=year(grade)
	return ((current_gpa*seg)+(4.00*semester))/(semester+seg)

#print MaxGPA("sophomore", 3.23, 2)

def Avg(start,time, end):
	x = start
	while ((start+(x*time))/(time+1)) <= end:
		x+=0.01
	return x
#print Avg(3.00,4,3.20)
#calculates the average gpa they need to maintain for a certain amount 
#of time given the current gpa, desired gpa, and time interval.
#def WantGPA(grade, current_gpa, semester, desired_gpa):
# grade = sophomore
# current_gpa = 3.00
# semester = 2
# desired_gpa = 3.20
# output: answer
def WantGPA(grade,current_gpa, semester, desired_gpa):
	seg=year(grade)
	x = Avg(current_gpa, semester,desired_gpa)
	while ((current_gpa*seg)+(x*semester))/(semester+seg) != desired_gpa:
		x+=0.01
		return x
print WantGPA("sophomore", 3.00, 2, 3.20)
print WantGPA("junior", 2.30, 1, 3.0)

