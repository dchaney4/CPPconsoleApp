#pragma once
#include <iostream>
#include <string>
#include <array>
#include "roster.h"
#include "student.h"


int main()
{
	//Print my info
	std::cout << "Scripting and Programming - Applications - C867" << std::endl;
	std::cout << "Programming Language: C++" << std::endl;
	std::cout << "Student ID #: 011277045" << std::endl;
	std::cout << "Name: Dirk Chaney-Zimmerman" << std::endl << std::endl << std::endl;

	const std::string studentData[] =
	{
		//student data info to be parsed
		"A1,John,Smith,John1989@gm ail.com,20,30,35,40,SECURITY",
		"A2,Suzan,Erickson,Erickson_1990@gmailcom,19,50,30,40,NETWORK",
		"A3,Jack,Napoli,The_lawyer99yahoo.com,19,20,40,33,SOFTWARE",
		"A4,Erin,Black,Erin.black@comcast.net,22,50,58,40,SECURITY",
		"A5,Dirk,Chaney-Zimmerman,dcha336@wgu.edu,29,23,2,23,SOFTWARE"
	};
	
	const int maxStudents = 5;

	Roster classRoster = Roster(maxStudents);

	//parse and add
	for (int i = 0; i < maxStudents; i++)
	{
		classRoster.parse(studentData[i]);
	}
	//print all roster data
	classRoster.printAll();
	std::cout << std::endl << std::endl;

	//print invalid emails
	std::cout << "Invalid Emails: " << std::endl;
	classRoster.printInvalidEmails();
	std::cout << std::endl << std::endl;

	//print average days in course for each student
	for (int i = 0; i < maxStudents; i++)
	{
		classRoster.printAverageDaysInCourse(classRoster.classRosterArray[i]->getStudentID());
	}
	std::cout << std::endl << std::endl;

	//print students names in degree program (software)
	classRoster.printByDegreeProgram(SOFTWARE);
	std::cout << std::endl << std::endl;

	//remove student A3 from roster
	classRoster.remove("A3");
	std::cout << std::endl << std::endl;

	//print all roster data again to show removed student
	classRoster.printAll();
	std::cout << std::endl << std::endl;

	//attempt to remove student A3 again, printing error
	classRoster.remove("A3");
	std::cout << std::endl << std::endl;

	//destructor
	classRoster.~Roster();

	return 0;
}
