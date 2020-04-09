#include <iostream>
#include "student.h"
#include "classroom.h"

using namespace std;

int main() {
    cout << "Start main" << endl;


//    unique_ptr<Student> student1 = make_unique<Student>("tobe", 20);
//    student1->show();

    auto classroom = make_unique<Classroom>();

    classroom->addStudent("tobe", 20);
    classroom->addStudent("tobe2", 22);

    classroom->show();

    cout << "End of main" << endl;

    return 0;
}