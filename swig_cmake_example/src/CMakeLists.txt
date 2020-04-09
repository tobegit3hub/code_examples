
# SWIG: use SWIG_MODULE_NAME property.
if(POLICY CMP0086)
  cmake_policy(SET CMP0086 NEW)
endif()

# SWIG: use standard target name.
if(POLICY CMP0078)
  cmake_policy(SET CMP0078 NEW)
endif()

find_package(SWIG REQUIRED)
include(UseSWIG)

include_directories(${INCLUDE_DIRECTORIES}
        ${PROJECT_SOURCE_DIR}/src
        ${PROJECT_BINARY_DIR}/src)

add_library(student STATIC student.cpp)
add_library(classroom STATIC classroom.cpp)
add_library(school STATIC student.cpp classroom.cpp)

add_executable(school_demo school_demo.cpp)
target_link_libraries(school_demo student school)

# g++ -std=c++14 -fpic -c school_wrap.cxx ./student.cpp ./classroom.cpp ./student.h ./classroom.h -I/Library/Java/JavaVirtualMachines/jdk1.8.0_201.jdk/Contents/Home/include/darwin -I/Library/Java/JavaVirtualMachines/jdk1.8.0_201.jdk/Contents/Home/include/

include(UseSWIG)

set_property(SOURCE school.i PROPERTY CPLUSPLUS ON)
set_property(SOURCE school.i PROPERTY SWIG_MODULE_NAME python_school)

swig_add_library(python_school
  TYPE SHARED
  LANGUAGE python
  OUTPUT_DIR ${PROJECT_SOURCE_DIR}/python/school/
  SOURCES	school.i)
  target_include_directories(python_school PRIVATE /usr/local/Cellar/python@3.8/3.8.2/Frameworks/Python.framework/Versions/3.8/include/python3.8/)
target_include_directories(python_school PRIVATE ${PYTHON_INCLUDE_DIRS})
target_link_directories(python_school PRIVATE /usr/local/Cellar/python@3.8/3.8.2/Frameworks/Python.framework/Versions/3.8/lib/)
target_link_libraries(python_school PRIVATE school)  
target_link_libraries(python_school PRIVATE python3.8)

#set_property(SOURCE school.i PROPERTY SWIG_MODULE_NAME java_school)
set_property(SOURCE school.i PROPERTY COMPILE_OPTIONS
  -package com.tobe.school
)
swig_add_library(java_school
  TYPE SHARED
  LANGUAGE java
  OUTPUT_DIR ${PROJECT_SOURCE_DIR}/swig_java_demo/src/main/java/com/tobe/school/
  SOURCES	school.i)
#target_include_directories(java_school PRIVATE ${JNI_INCLUDE_DIRS})
target_include_directories(java_school PRIVATE /Library/Java/JavaVirtualMachines/jdk1.8.0_201.jdk/Contents/Home/include/)
target_include_directories(java_school PRIVATE /Library/Java/JavaVirtualMachines/jdk1.8.0_201.jdk/Contents/Home/include/darwin/)
target_link_libraries(java_school PRIVATE school)
if(APPLE)
  set_target_properties(java_school PROPERTIES
           SUFFIX ".so")
  set_property(TARGET java_school APPEND PROPERTY
    LINK_FLAGS "-flat_namespace -undefined suppress")
endif()
