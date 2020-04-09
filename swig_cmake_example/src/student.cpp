#include "student.h"

Student::Student() {
    this->name = "No name";
    this->age = 0;
}

Student::Student(string name, int age) {
    this->name = name;
    this->age = age;
}

Student::~Student() {

}

void Student::show() {
    cout << "The name is " << this->name << ", age is " << this->age << endl;
}

