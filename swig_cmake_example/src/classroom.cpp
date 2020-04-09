
#include "classroom.h"

Classroom::Classroom() {
    
}

Classroom::~Classroom() {
    // this->students.clear();
}

void Classroom::addStudent(string name, int age) {

    // this->students.push_back(make_unique<Student>(name, age));

}

/*
unique_ptr<Student> Classroom::getStudent(int i) {

    //auto p = this->students[0];
    return nullptr;
}
*/

void Classroom::show() {
    // cout << "Classroom students size is " << this->students.size() << endl;
    cout << "mock classroo show" << endl;
}


