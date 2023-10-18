from conans import ConanFile
from os.path import join

class TestPackageConan(ConanFile):
    python_requires = "myconantools/1.0@myUser/myChannel"
    python_requires_extend = "myconantools.DefaultPackageConan"

    # CMakeDeps generator create the *Config.cmake files for the requirements, so we can use find_package in cmakelists
    generators = ["CMakeDeps", "CMakeToolchain"]

    name = "TestPackage"
    version = "1.0"

    def requirements(self):
        self.requires("MyPackage/1.0@myUser/myChannel")

    def test(self):
        self.run(join(self.build_folder, "testpackage"))
