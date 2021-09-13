# conan_transient_linkage
https://github.com/conan-io/conan/issues/9600

reproduce an error when building shared libs

run build.sh to get this:
```
...
[ 75%] Building CXX object tests/CMakeFiles/lib_a_test.dir/lib_a_test.cpp.o
[100%] Linking CXX executable lib_a_test
/usr/bin/ld: warning: liblib_c.so, needed by //home/fberchtold/.conan/data/lib_b/1.0.0/_/_/package/436fa0a6d3ec3ce29639456d6db8d06cd9bf62c9/lib/liblib_b.so, not found (try using -rpath or -rpath-link)
//home/fberchtold/.conan/data/lib_b/1.0.0/_/_/package/436fa0a6d3ec3ce29639456d6db8d06cd9bf62c9/lib/liblib_b.so: undefined reference to `lum::lib_c::SayHello[abi:cxx11]()'
collect2: error: ld returned 1 exit status
tests/CMakeFiles/lib_a_test.dir/build.make:98: recipe for target 'tests/lib_a_test' failed
make[2]: *** [tests/lib_a_test] Error 1
CMakeFiles/Makefile2:881: recipe for target 'tests/CMakeFiles/lib_a_test.dir/all' failed
make[1]: *** [tests/CMakeFiles/lib_a_test.dir/all] Error 2
Makefile:145: recipe for target 'all' failed
make: *** [all] Error 2
lib_a/1.0.0: 
lib_a/1.0.0: ERROR: Package '4c3f20be28cf1be70e428d9fc0e689236ff00f59' build failed
lib_a/1.0.0: WARN: Build folder /home/fberchtold/.conan/data/lib_a/1.0.0/_/_/build/4c3f20be28cf1be70e428d9fc0e689236ff00f59
ERROR: lib_a/1.0.0: Error in build() method, line 52
        cmake.build()
        ConanException: Error 2 while executing cmake --build '/home/fberchtold/.conan/data/lib_a/1.0.0/_/_/build/4c3f20be28cf1be70e428d9fc0e689236ff00f59' '--' '-j24'
```
