cmake_minimum_required(VERSION 3.15)
project(lib_b)

include(CTest)

find_package(lib_c REQUIRED)

add_library(lib_b src/lib_b.cpp)

target_include_directories(lib_b PUBLIC include)

target_link_libraries(lib_b PRIVATE lib_c::lib_c)

install(TARGETS lib_b)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
        FILES_MATCHING
        PATTERN "*.h*"
)

if(BUILD_TESTING)
  find_package(Catch2 2.13.4 REQUIRED)

  add_subdirectory(tests)
endif()
