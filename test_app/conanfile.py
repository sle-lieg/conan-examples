from conans import ConanFile
from conan.tools.cmake import CMake
from os.path import join

class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    # CMakeDeps generator create the *Config.cmake files for the requirements, so we can use find_package in cmakelists
    generators = ["CMakeDeps", "CMakeToolchain"]
    options = {"tested": [True, False], "shared": [True, False], "fPIC": [True, False]}
    default_options = {"tested": True, "shared": True, "fPIC": True}

    name = "TestPackage"
    version = "1.0"

    def requirements(self):
        self.requires("MyPackage/1.0@myChannel/test")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run(join(self.build_folder, "testpackage"))
