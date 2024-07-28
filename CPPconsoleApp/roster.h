#pragma once
#include "student.h"
#include <iostream>
#include <string>


class Roster {

public:

	Student* classRosterArray[5];

	int maxStudents = 5;

	int index = 0;

	//Constructor
	Roster(int maxStudents);

	//Parse and add each set of data to roster array
	void parse(std::string studentData);

	//add student
	void add(std::string studentID, std::string firstName, std::string lastName, std::string emailAddress, int age, int daysInCourse1, int daysInCourse2, int daysInCourse3, DegreeProgramEnum degreeProgram);
	
	//remove student by student ID
	void remove(std::string studentID);
	
	//print all student data
	void printAll();
	
	//print a student's average number of days in each course, identify by student ID
	void printAverageDaysInCourse(std::string studentID);
	
	//print all invalid email address
	void printInvalidEmails();
	
	//print students by degree type
	void printByDegreeProgram(DegreeProgramEnum degreeProgram);

	//Destructor
	~Roster();

};