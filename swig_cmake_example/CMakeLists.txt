
cmake_minimum_required(VERSION 3.8.0)

project(swig_cmake_example)

add_compile_options(-std=c++14)

set(CMAKE_VERBOSE_MAKEFILE ON)

add_subdirectory(src)
