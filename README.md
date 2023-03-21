# BMICalculator
This is a Python program that creates a Body Mass Index (BMI) calculator using the graphical user interface (GUI) library Tkinter.
////Video Tutorial from DJ Oamen: https://www.google.com/search?q=bmi+calculator+dj+oamen&oq=bmi+calculator+dj+oamen&aqs=chrome..69i57j33i160l2.14292j1j7&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:930189d8,vid:23_93SXvCpc

###Edited by JC Villa:  Font, Colors, BottomFrame, test_log/ReadMe 

	This is a Python program that creates a Body Mass Index (BMI) calculator using the graphical user interface (GUI) library Tkinter. BMI is a measure of body fat based on a person's height and weight. The program consists of a main window divided into two sections: the left side with labels, input fields, and a calculate button, and the right side with a result display area.
	The program defines a class called BMI that initializes the GUI window and its components. It also creates different frames (subsections of the window) to organize the layout of the interface. The left frame contains the input fields for height and weight, a calculate button, and a reset button. The right frame displays the calculated BMI and a status message.
	The program uses various functions to perform tasks such as resetting the input fields, calculating the BMI, and exiting the application. It also uses different types of variables to store the user's input and the calculated result.
	The labels, buttons, and frames are customized with different colors, fonts, and dimensions. The program also displays a message at the bottom of the window explaining how healthcare providers and researchers can use a BMI app to track and collect data on their patients' health.

	The formula for BMI is:
	BMI = weight (kg) / [height (m)]^2
	Here are the steps to measure BMI:
		1.	Measure the person's weight in kilograms (kg). This can be done using a weighing scale. 
		2.	Measure the person's height in meters (m). This can be done using a stadiometer or a measuring tape. 
		3.	Square the person's height in meters. 
				-For example, if a person's height is 1.75 meters, you would calculate 1.75 x 1.75 = 3.06. 
		4.	Divide the person's weight in kilograms by the square of their height in meters. 
				-For example, if a person's weight is 70 kg and their height is 1.75 meters, you would calculate 70 / 3.06 = 22.9. 
		
	The resulting number is the person's BMI. BMI values can be interpreted as follows:
		◦	Below 18.5: Underweight
		◦	18.5-24.9: Normal weight
		◦	25.0-29.9: Overweight
		◦	30.0 and above: Obese

	It's important to note that BMI is not a perfect measurement of body fat, as it doesn't take into account factors like muscle mass or body shape. It should be used as a general guide.

