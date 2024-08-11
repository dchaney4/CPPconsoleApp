#pragma once
#include <iostream>
#include <string>
#include <array>
#include <iomanip>
#include "roster.h"



//Constructor
Roster::Roster(int maxStudents) {
	for (int i = 0; i < maxStudents; i++)
	{
		this->classRosterArray[i] = new Student;
	}
	return;
}

void Roster::parse(std::string studentData)
	{
		//set temp variables
		std::string ID; std::string fName; std::string lName; std::string eAddress; int studentAge; int daysInCourse1; int daysInCourse2; int daysInCourse3; std::string dProgram;
		if (index < maxStudents) {
			classRosterArray[index] = new Student();

			//find data between each "," and parse into temp variables
			int x = studentData.find(",");
			ID = studentData.substr(0, x);
			classRosterArray[index]->setStudentID(ID);

			int y = x + 1;
			x = studentData.find(",", y);
			fName = studentData.substr(y, x - y);
			classRosterArray[index]->setFirstName(fName);

			y = x + 1;
			x = studentData.find(",", y);
			lName = studentData.substr(y, x - y);
			classRosterArray[index]->setLastName(lName);

			y = x + 1;
			x = studentData.find(",", y);
			eAddress = studentData.substr(y, x - y);
			classRosterArray[index]->setEmailAddress(eAddress);

			y = x + 1;
			x = studentData.find(",", y);
			studentAge = std::stoi(studentData.substr(y, x - y));
			classRosterArray[index]->setAge(studentAge);

			y = x + 1;
			x = studentData.find(",", y);
			daysInCourse1 = std::stoi(studentData.substr(y, x - y));

			y = x + 1;
			x = studentData.find(",", y);
			daysInCourse2 = std::stoi(studentData.substr(y, x - y));

			y = x + 1;
			x = studentData.find(",", y);
			daysInCourse3 = std::stoi(studentData.substr(y, x - y));
			classRosterArray[index]->setDaysInCourse(daysInCourse1, daysInCourse2, daysInCourse3);

			//Convert string to DegreeProgramEnum
			y = x + 1;
			x = studentData.find(",", y);
			dProgram = studentData.substr(y, x - y);
			if (dProgram == "SECURITY") {
				classRosterArray[index]->setDegreeProgram(SECURITY);
			}
			else if (dProgram == "NETWORK") {
				classRosterArray[index]->setDegreeProgram(NETWORK);
			}
			else if (dProgram == "SOFTWARE") {
				classRosterArray[index]->setDegreeProgram(SOFTWARE);
			}
			else {
				std::cout << "NO DEGREE FOUND" << std::endl;
			}
			index++;

		}
	};

void Roster::add(std::string studentID, std::string firstName, std::string lastName, std::string emailAddress, int age, int daysInCourse1, int daysInCourse2, int daysInCourse3, DegreeProgramEnum degreeProgram) 
{
	
	int daysInCourse[3] = { daysInCourse1, daysInCourse2, daysInCourse3 };
	
	classRosterArray[maxStudents] = new Student(studentID, firstName, lastName, emailAddress, age, daysInCourse, degreeProgram);
};

//Find student by ID and remove from roster
void Roster::remove(std::string studentID) 
{
	bool found = false;
	for (int i = 0; i < maxStudents; i++)
	{
		if (classRosterArray[i] != nullptr && classRosterArray[i]->getStudentID() == studentID)
		{
			delete classRosterArray[i];
			classRosterArray[i] = nullptr;
			std::cout << "Student # " << studentID << " has successfully been removed" << std::endl;
			found = true;
			break;
		}
		
	}
	//Print error if studentID not found
	if (!found)
	{
		std::cout << "ERROR: STUDENT # " << studentID << " NOT FOUND" << std::endl;
	}
}

//Loop through roster, printing student data
void Roster::printAll()
{
	std::cout << "Student List: " << std::endl;
	for (int i = 0; i < maxStudents; i++)
	{
		if (classRosterArray[i] != nullptr)
		{
			classRosterArray[i]->print();
		}
	}
}

void Roster::printAverageDaysInCourse(std::string studentID)
{
	for (int i = 0; i < maxStudents; i++)
	{
		if (studentID == classRosterArray[i]->getStudentID())
		{
			int averageDaysInCourse = ((classRosterArray[i]->getDaysInCourse()[0] + classRosterArray[i]->getDaysInCourse()[1] + classRosterArray[i]->getDaysInCourse()[2]) / 3);
			std::cout << "Student #" << studentID << "'s average days to class completion: " << averageDaysInCourse << std::endl;
			break;
		}
	}
	return;
}

void Roster::printInvalidEmails()
{
	for (int i = 0; i < maxStudents; i++)
	{
		std::string tempEmail = classRosterArray[i]->getEmailAddress();
		//look for an incorrect space or a missing '@' or a missing '.'
		if ((tempEmail.find(" ") != std::string::npos) || (tempEmail.find("@") == std::string::npos) || (tempEmail.find(".") == std::string::npos))
		{
			std::cout << tempEmail << std::endl;
		}
	}
	return;
}

void Roster::printByDegreeProgram(DegreeProgramEnum degreeProgram)
{
	//convert DegreeProgramEnum to string
	std::string degreeString;
	if (degreeProgram == SECURITY)
	{
		degreeString = "SECURITY";
	}
	else if (degreeProgram == NETWORK)
	{
		degreeString = "NETWORK";
	}
	else if (degreeProgram == SOFTWARE)
	{
		degreeString = "SOFTWARE";
	}
	else
	{
		degreeString = "ERROR: DEGREE NOT FOUND";
	}

	std::cout << "Students in " << degreeString << " degree program:" << std::endl;

	int numberStudents = 0;
	//compare each student's degree program against input
	for (int i = 0; i < maxStudents; i++)
	{
		if (classRosterArray[i] != nullptr && classRosterArray[i]->getDegreeProgram() == degreeProgram)
		{
			//print student name if degree program matches
			classRosterArray[i]->printName();
			++numberStudents;
		}
	}
	//Print message if no student degree program match is found
	if (numberStudents == 0)
	{
		std::cout << "ERROR: None Found" << std::endl;
	}
	return;
	
}

//Destructor
Roster::~Roster()
{
	for (int i = 0; i < maxStudents; i++)
	{
		delete classRosterArray[i];
		classRosterArray[i] = nullptr;
	}
}