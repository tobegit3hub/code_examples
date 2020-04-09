#ifndef CLASSROOM_H_
#define CLASSROOM_H_

#include "student.h"
#include <vector>
#include <string>

using namespace std;

class Classroom {

private:
    // vector<unique_ptr<Student>> students;

public:

    Classroom();
    ~Classroom();

    void addStudent(string name, int age);
    //unique_ptr<Student> getStudent(int i);
    void show();
    
};

#endif // End of CLASSROOM_H_