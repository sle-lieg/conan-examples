from conans import ConanFile
from conan.tools.cmake import CMake, cmake_layout
#   This Cmake require the CMakeToolChain generator to work.
#   The CMakeToolChain generator generate the CMakePresets.json and conan_toolchain.cmake files, each consumed by the
#   conan.tools.cmake.CMake helper.

class MyPackageConan(ConanFile):
    python_requires = "myconantools/1.0@myUser/myChannel"
    python_requires_extend = "myconantools.DefaultPackageConan"

    name = "MyPackage"
    version = "1.0"

    # Must export all the file needed to build the different libs. Project tree kept as it is when copied in cache
    # .
    # ├── CMakeLists.txt
    # ├── libbar/
    # ├── libcommon/
    # └── libfoo/
    exports_sources = "CMakeLists.txt", "libcommon/*", "libfoo/*", "libbar/*"

    def layout(self):
        super().layout()

        # Source informations (relative to Source path, which is where the conanfile.py is located by default,
        # so ./conan-examples/multi_lib_single_conanfile here) :
        #   - So the consumer of the package if in EDITABLE mode knows where the includes are
        self.cpp.source.components["foo"].includedirs = ["libfoo/include"]
        self.cpp.source.components["bar"].includedirs = ["libbar/include"]
        # self.cpp.source.components["bar"].resdirs = ["libbar/resources"] # If your component has resources

        # Build informations (relative to the Build path, so by default with 'cmake_layout' build/Release or build Debug):
        #   - So the consumer of the package if in EDITABLE mode knows where the libs are located
        self.cpp.build.components["foo"].libs = ["foo"]
        self.cpp.build.components["foo"].libdirs = ["libfoo"]  # so consumer knows the lib foo is in build/Release/libfoo folder
        self.cpp.build.components["bar"].libs = ["bar"]
        self.cpp.build.components["bar"].libdirs = ["libbar"] # so consumer knows the lib bar is in build/Release/libbar folder
        # self.cpp.source.components["bar"].bindir = ["path_to_bin/"] # If your component was a binary

        # package informations: can replace the package_info, and describe the final content of the package
        # (see package_info below for more informations)
        self.cpp.package.components["foo"].includedirs = ["include/foo"]
        self.cpp.package.components["foo"].libdirs = ["lib/foo"]
        self.cpp.package.components["foo"].libs = ["foo"]

        self.cpp.package.components["bar"].includedirs = ["include/bar"]
        self.cpp.package.components["bar"].libdirs = ["lib/bar"]
        self.cpp.package.components["bar"].libs = ["bar"]

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
        # You can either define package_info for the package and its components in here, or in the layout method.
        # Package_info is used to tell the consumers of the package where are the different libs, include, resources,
        # etc inside it, and to set some package properties. But it does not affect the project tree, it does not create
        # any folders !!

        # This define how the MyPackage cmake file will be named
        # (file searched by find_package(<cmake_file_name>Config.cmake) in CMakeLists.txt).
        self.cpp_info.set_property("cmake_file_name", "MyPackage") # By default it already take the package name

        # Set the package and components target names (to use when doing a target_link_libraries for example)
        self.cpp_info.set_property("cmake_target_name", "MyPackage::MyPackage") # Default to <package_name>::<package_name>
        self.cpp_info.components["foo"].set_property("cmake_target_name", "MyPackage::foo")
        self.cpp_info.components["bar"].set_property("cmake_target_name", "MyPackage::bar")

        ## Set this if you want the consumers to include 'foo/foo.h', and not only foo.h
        # self.cpp_info.includedirs = ["include"]

        ## Otherwise, this allow consumers to require only foo.h and bar.h
        # self.cpp_info.components["foo"].includedirs = ["include/foo"]
        # self.cpp_info.components["bar"].includedirs = ["include/bar"]

        ## This
        # self.cpp_info.components["foo"].libs = ["foo"]
        # self.cpp_info.components["foo"].libdirs = ["lib/foo"]

        # self.cpp_info.components["bar"].libs = ["bar"]
        # self.cpp_info.components["bar"].libdirs = ["lib/bar"]
