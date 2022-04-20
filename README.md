# Piazza-Plus-Plus

Team Members: Andrew, Neil, Brandon, Labib, Austin

admin account - 
email:admin@iit.edu
pass:admin

prof account - 
email:prof@iit.edu
pass:prof

student account - 
email:student@iit.edu
pass:student 
classes: "cs100,cs200,math200"

1) to start the program, in the terminal make sure your in the programs folder.
2) then in the terminal activate the venv with "source venv/scripts/activate"
3) once you are in the virtual enviroment, you and run it with "flask run"
4) this will allow they flask server to run on 127.0.0.1:5000 or localhost:5000
5) you can go into that address and view the program on your browser.

each of the example accounts above do work and allow diffrent functions to work baces on their roles

some things that still need to be added
 - home page show current users classes, then be able to click into those classes to see profesors posts
 - for posts we need to add due date so we can show it and use it for the calender side
 - we need to make another page for the calendar and link it to the users classes
 
simple layout for how home page will be and how the student will go though

(below looks better when read on text file)

only show their classes
		(diagram example)
			home
				class1
					(inside a class is posts and student can reply)
                		class2
					(inside a class is posts and student can reply)
                		class3
					(inside a class is posts and student can reply)
