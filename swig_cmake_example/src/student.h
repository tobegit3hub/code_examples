#ifndef STUDENT_H_
#define STUDENT_H_

#include <string>
#include <iostream>

using namespace std;

class Student {

private:
    string name;
    int age;

public: 
    Student();
    Student(string name, int age);
    ~Student();

    void show();

};

#endif // end of STUDENT_H_