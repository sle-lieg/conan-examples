from conans import ConanFile
from conan.tools.cmake import cmake_layout

class DefaultParams(object):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"
    options = {"tested": [True, False], "shared": [True, False], "fPIC": [True, False]}
    default_options = {"tested": True, "shared": True, "fPIC": True}

    def layout(self):
        cmake_layout(self)


class GlobalConan(ConanFile):
    name = "globalconanhelper"
    version = "1.0"
    url = ""
    license = ""
    description = "Common functions to create conan packages"
