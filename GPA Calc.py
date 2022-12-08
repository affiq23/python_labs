number_of_total_credits = 0

def get_grades():
	global number_of_total_credits
	className = ''
	classGrade = 0.0
	classScale = 0
	
	gradesList = []
	
	numberofclasses = int (input('Number of classes: '))

	for _ in range(numberofclasses):
		className = input('Enter Class {} Name: '.format(_+1))
		if(className == 'NONE'):
			continue
		
		classGrade = float (input('Enter Class {} Grade: '.format(_ + 1)))
		classScale = float (input('Enter Class {} Scale: '.format(_ + 1)))
		classCredits = float (input('Enter Number of Credits: '.format(_ + 1)))
		
		number_of_total_credits += classCredits

		print('')
 
		gradesList.append((className, classGrade, classScale, classCredits))
		
	return gradesList


def compute_gpa(gradeslist):
	global number_of_total_credits
	
	weighted_gpa_list = []
	unweighted_gpa_list = []

	weightedGpa = 0.0
	unweightedGpa = 0.0


	for name,grade,weight,credits in gradeslist:
		weightedGpa = ((weight - ((100 - grade)/10)) * credits)

		weighted_gpa_list.append(weightedGpa)

	weightedGpa = (sum(weighted_gpa_list) / number_of_total_credits)

	for name,grade,weight,credits in gradeslist:
		unweightedGpa = ((4.0 - ((90 - grade)/10)) * credits)

		if (unweightedGpa > 4.0):
			unweightedGpa = 4.0

		unweighted_gpa_list.append((unweightedGpa))

	unweightedGpa = (sum(unweighted_gpa_list) / number_of_total_credits)

	gpas = (weightedGpa, unweightedGpa)

	return gpas


def printGPA(gpas):
	weighed, unweighted = gpas
	
	print('Weighted GPA: {}'.format(weighed))
	print('Unweighed GPA: {}'.format((unweighted)))


def printTranscript(gpas, gradeslist):
	with open('myTranscript.txt', mode = 'w') as my_new_transcript:
		my_new_transcript.write(('Class Name: \t Class Grade:'))

		for name,grade,weight,credits in gradeslist:
			my_new_transcript.write(f'\n{name}')
			my_new_transcript.write(f'\t \t{grade}')


		weighed, unweighted = gpas

		my_new_transcript.write(f'\n\nWeighted GPA: {weighed}')
		my_new_transcript.write(f'\n\nUnweighed GPA: {unweighted}')


if __name__ == '__main__':

	gradeslist = get_grades()
	gpas = compute_gpa(gradeslist)
	printTranscript(gpas, gradeslist)
	
	printGPA(gpas)
