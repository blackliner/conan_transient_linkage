cmake_minimum_required(VERSION 3.15)
project(lib_a)

include(CTest)

find_package(lib_b REQUIRED)

add_library(lib_a src/lib_a.cpp)

target_include_directories(lib_a PUBLIC include)

target_link_libraries(lib_a PRIVATE lib_b::lib_b)

install(TARGETS lib_a)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
        FILES_MATCHING
        PATTERN "*.h*"
)

if(BUILD_TESTING)
  find_package(Catch2 2.13.4 REQUIRED)

  add_subdirectory(tests)
endif()
