add_executable(lib_b_test lib_b_test.cpp)

target_link_libraries(lib_b_test PRIVATE lib_b Catch2::Catch2WithMain)

add_test(NAME lib_b_test COMMAND lib_b_test)
