#pragma once
#include <iostream>
#include "degree.h"
#include <string>


class Student {

private:
	//Student Class Variables
	std::string studentID;
	std::string firstName;
	std::string lastName;
	std::string emailAddress;
	int age;
	int daysInCourse[3];
	DegreeProgramEnum degreeProgram;

public:
	// Constructors
	Student();
	Student(std::string studentID, std::string firstName, std::string lastName, std::string emailAddress, int age, int daysInCourse[], DegreeProgramEnum degreeProgram);

	// Accessors
	std::string getStudentID();
	std::string getFirstName();
	std::string getLastName();
	std::string getEmailAddress();
	int getAge();
	int* getDaysInCourse();
	DegreeProgramEnum getDegreeProgram();

	// Mutators
	void setStudentID(std::string studentID);
	void setFirstName(std::string firstName);
	void setLastName(std::string lastName);
	void setEmailAddress(std::string emailAddress);
	void setAge(int age);
	void setDaysInCourse(int daysInCourse1, int daysInCourse2, int daysInCourse3);
	void setDegreeProgram(DegreeProgramEnum degreeProgram);

	// Print
	void print();
	void printName();



};
