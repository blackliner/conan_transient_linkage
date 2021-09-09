cmake_minimum_required(VERSION 3.15)
project(lib_c)

include(CTest)

add_library(lib_c src/lib_c.cpp)

target_include_directories(lib_c PUBLIC include)

install(TARGETS lib_c)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
        FILES_MATCHING
        PATTERN "*.h*"
)

if(BUILD_TESTING)
  find_package(Catch2 2.13.4 REQUIRED)

  add_subdirectory(tests)
endif()
