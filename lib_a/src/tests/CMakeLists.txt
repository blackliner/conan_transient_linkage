add_executable(lib_a_test lib_a_test.cpp)

target_link_libraries(lib_a_test PRIVATE lib_a Catch2::Catch2WithMain)

add_test(NAME lib_a_test COMMAND lib_a_test)
