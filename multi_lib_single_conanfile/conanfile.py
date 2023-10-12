from conans import ConanFile
from conan.tools.cmake import CMake
#   This Cmake require the CMakeToolChain generator to work.
#   The CMakeToolChain generator generate the CMakePresets.json and conan_toolchain.cmake files, each consumed by the
#   conan.tools.cmake.CMake helper.

class MyPackageConan(ConanFile):
    name = "MyPackage"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = ["CMakeToolchain"]
    options = {"fPIC": [True, False]}
    default_options = {"fPIC": True}

    # Must export all the file needed to build the different libs. Project tree kept as it is when copied in cache
    # .
    # ├── CMakeLists.txt
    # ├── libbar/
    # ├── libcommon/
    # └── libfoo/
    exports_sources = "CmakeLists.txt", "libcommon/*", "libfoo/*", "libbar/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    # def layout(self):
    #     # self.folders.package = "MyPackage"
    #     self.folders.source = "."
    #     build_type = str(self.settings.build_type).lower()
    #     self.folders.build = "cmake-build-{}".format(build_type)
    #     self.folders.generators = self.folders.build

        # self.cpp.build.includedirs = ["foo/include", "bar/include"]
        # self.cpp.build.libdirs = ["foo/lib", "bar/lib"]
        # self.cpp.build.bindirs = ["foo/bin", "bar/bin"]
        # self.cpp.build.resdirs = ["foo/resources", "bar/resources"]

        # self.cpp.package.includedirs = ["foo/include", "bar/include"]
        # self.cpp.package.libdirs = ["foo/lib", "bar/lib"]
        # self.cpp.package.bindirs = ["foo/bin", "bar/bin"]
        # self.cpp.package.resdirs = ["foo/resources", "bar/resources"]

        # self.cpp.package.components = {
        #     "foo": {
        #         "package_folder": "libfsoo",
        #         "build_folder": "build",
        #         "source_folder": "src",
        #         "install_folder": "lib",
        #     },
        #     "bar": {
        #         "toto": "libbar",
        #         "build_folder": "build",
        #         "source_folder": "src",
        #         "install_folder": "lib",
        #     },
        # }

        # self.cpp.package.components["foo"].includedirs = "include"
        # self.cpp.package.components["foo"].libdirs = "lib"

        # self.cpp.package.libs = ["foo", "bar"]
        # self.cpp.package.libdirs = []
        # self.cpp.package.includedirs = ["foo/include", "bar/include"] # includedirs is already set to this value by
        #                                            # default, but declared for completion

        # # this information is relative to the source folder
        # self.cpp.source.includedirs = ["include"]  # maps to ./src/include

        # # this information is relative to the build folder
        # self.cpp.build.libdirs = ["."]             # maps to ./cmake-build-<build_type>
        # self.cpp.build.bindirs = ["bin"]           # maps to ./cmake-build-<build_type>/bin


    def package(self):
        # libcommon.a and libcommon headers are not packaged since they are only required to build libfoo and libbar,
        # and common.h is only 'included' in foo.c and bar.c files, not in their header

        # Either manually Package libfoo.so, libbar.so and their headers
        # self.copy("*.h", dst="include/foo", src="libfoo/include")
        # self.copy("*.h", dst="include/bar", src="libbar/include")
        # self.copy("*.so", dst="lib/foo", src=os.path.join(self.build_folder, "libfoo"))
        # self.copy("*.so", dst="lib/bar", src=os.path.join(self.build_folder, "libbar"))

        # Or use the prefer method that use the install methods from the components cmakelists.
        # The conan CMake helper will automatically replace the default installation path by the package path in cache
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        # So the consumers must include 'foo/foo.h', and not only foo.h
        self.cpp_info.includedirs = ["include"]

        # This allow consumers to require only foo.h
        # self.cpp_info.components["foo"].includedirs = ["include/foo"]
        # self.cpp_info.components["bar"].includedirs = ["include/bar"]

        self.cpp_info.components["foo"].libs = ["foo"]
        self.cpp_info.components["foo"].libdirs = ["lib/foo"]

        self.cpp_info.components["bar"].libs = ["bar"]
        self.cpp_info.components["bar"].libdirs = ["lib/bar"]
