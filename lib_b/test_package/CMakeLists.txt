cmake_minimum_required(VERSION 3.15)
project(test_package)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(lib_b REQUIRED)

add_executable(test_package test_package.cpp)
target_link_libraries(test_package lib_b::lib_b)
