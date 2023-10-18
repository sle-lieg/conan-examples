from conans import ConanFile
from conan.tools.cmake import CMake, cmake_layout

class DefaultPackageConan(object):
    # Common settings, generator, options and method for all packages
    settings = "os", "compiler", "build_type", "arch"
    generators = ["CMakeToolchain"]
    options = {"tested": [True, False], "shared": [True, False], "fPIC": [True, False]}
    default_options = {"tested": True, "shared": True, "fPIC": True}

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

class GlobalConan(ConanFile):
    name = "myconantools"
    version = "1.0"
    url = ""
    license = "MIT License"
    description = "Common functions to create conan packages"
