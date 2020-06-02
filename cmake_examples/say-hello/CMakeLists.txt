
add_library(
    hello 
    src/hello.h 
    src/hello.cpp
)

target_include_directories(hello PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/src")
