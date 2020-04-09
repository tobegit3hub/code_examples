
%module school

%include "stdint.i"
%include "std_string.i"

%{
#include "student.h"
#include "classroom.h"
%}

%include student.h
%include classroom.h

