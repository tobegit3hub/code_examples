package com.tobe.demo;

import com.tobe.school.*;

public class JavaSchoolDemo {
    public static void main(String[] argv) {
        System.out.println("Start main");

        //String path = JavaSchoolDemo.class.getResource("./libfesql_jsdk.jnilib").getPath();
        //String path = "/Users/tobe/code/code_examples/swig_example/build/libschool_swig.dylib";
        String path = "/Users/tobe/code/code_examples/swig_cmake_example/build/src/libjava_school.so";
        System.load(path);

        


        Student student1 = new Student();

        student1.show();




        System.out.println("End of main");
    }

}