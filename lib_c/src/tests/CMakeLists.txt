add_executable(lib_c_test lib_c_test.cpp)

target_link_libraries(lib_c_test PRIVATE lib_c Catch2::Catch2WithMain)

add_test(NAME lib_c_test COMMAND lib_c_test)
