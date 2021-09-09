from conans import ConanFile, CMake, tools


class LibBConan(ConanFile):
    name = "lib_b"
    version = "1.0.0"

    exports_sources = ["CMakeLists.txt", "src/**"]
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "with_tests": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "with_tests": True,
        "catch2:with_main": True,
    }
    generators = "cmake_find_package", "cmake"

    _cmake = None

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            del self.options.fPIC

    def build_requirements(self):
        if self.options.with_tests:
            self.build_requires("catch2/2.13.4", force_host_context=True)

    def requirements(self):
        self.requires("lib_c/1.0.0")

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake
        self._cmake = CMake(self)

        self._cmake.definitions["BUILD_TESTING"] = self.options.with_tests

        self._cmake.configure(source_folder=self.source_folder)
        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
