#include <iostream>
#include "student.h"

//Default Constructor
Student::Student()
{
	this->studentID = "";
	this->firstName = "";
	this->lastName = "";
	this->emailAddress = "";
	this->age = 0;
	this->daysInCourse[0] = 0;
	this->daysInCourse[1] = 0;
	this->daysInCourse[2] = 0;
	this->degreeProgram;
}
//Constructor
Student::Student(std::string studentID,
	std::string firstName,
	std::string lastName,
	std::string emailAddress,
	int age,
	int daysInCourse[],
	DegreeProgramEnum degreeProgram) 
{
	this->studentID = studentID;
	this->firstName = firstName;
	this->lastName = lastName;
	this->emailAddress = emailAddress;
	this->age = age;
	for (int i = 0; i < 3; i++) this->daysInCourse[i] = daysInCourse[i];
	this->degreeProgram = degreeProgram;
}

//Accessors
std::string Student::getStudentID() 
{
	return studentID;
}
std::string Student::getFirstName() 
{
	return firstName;
}
std::string Student::getLastName() 
{
	return lastName;
}
std::string Student::getEmailAddress() 
{
	return emailAddress;
}
int Student::getAge() 
{
	return age;
}
int* Student::getDaysInCourse() 
{
	return daysInCourse;
}
DegreeProgramEnum Student::getDegreeProgram() 
{
	return degreeProgram;
}
	

//Mutators
void Student::setStudentID(std::string studentID) 
{
	this->studentID = studentID;
}
void Student::setFirstName(std::string firstName) 
{
	this->firstName = firstName;
}
void Student::setLastName(std::string lastName) 
{
	this->lastName = lastName;
}
void Student::setEmailAddress(std::string emailAddress) 
{
	this->emailAddress = emailAddress;
}
void Student::setAge(int age) 
{
	this->age = age;
}
void Student::setDaysInCourse(int daysInCourse1, int daysInCourse2, int daysInCourse3) 
{
	this->daysInCourse[0] = daysInCourse1;
	this->daysInCourse[1] = daysInCourse2;
	this->daysInCourse[2] = daysInCourse3;
}
void Student::setDegreeProgram(DegreeProgramEnum degreeProgram) 
{
	this->degreeProgram = degreeProgram;
}

//Print
void Student::print() 
{
	std::cout << "Student ID: " << getStudentID() << std::endl;
	std::cout << "First Name: " << getFirstName() << std::endl;
	std::cout << "Last Name: " << getLastName() << std::endl;
	std::cout << "Email Address: " << getEmailAddress() << std::endl;
	std::cout << "Age: " << getAge() << std::endl;
	std::cout << "Days in Course: " << getDaysInCourse() << std::endl;
	std::cout << "Degree Program: " << getDegreeProgram() << std::endl;
}

void Student::printName()
{
	std::cout << getFirstName() << " " << getLastName() << std::endl;
}