# multi_lib_single_conanfile tutorial

This program has been developped and tested with conan 1.59

The multi_lib_single_conanfile is a package that contains 2 public shared libraries, libfoo.so and libbar.so, and a private static library, libcommon.a, that is used by the 2 others.

The package uses a cmake_layout, and demonstrate how to package a multi-component package, and how to configure its layout so the package is also usable in editable mode.

## 🛠️ Create a cpnan cache version of myconantools
Start by creating in the conan cache the package containing the class that all other packages will inherit from, containing default settings, generator, options, and methods
```bash
cd my_conan_tools
conan export . myconantools/1.0@myUser/myChannel
```

## 🛠️ Build the package with conan
```bash
cd multi_lib_single_conanfile
conan install . -if build
conan build . -if build
```
The -if build tells conan to generate the config files inside the build directory, so it doesn't pollute the package directory.

Because this package uses the cmake_layout, conan does not need to be given the build directory. It uses the cmake_layout build folder (build/Release by default).

## 🛠️ Create a conan cache version of the package
```bash
cd multi_lib_single_conanfile
conan create . myUser/myChannel
```

## 🛠️ Set the package as editable
```bash
cd multi_lib_single_conanfile
conan editable add . MyPackage/1.0@myUser/myChannel
```
So when a consumer requires ``MyPackage/1.0@myUser/myChannel``, the path to the includes, libs, etc will point to the package in your workspace, and not in cache.

## 🛠️ Test the package
The test_package is a basic binary that requires the ``MyPackage/1.0@myUser/myChannel``, and uses its exported libraries libfoo.so and libbar.so.

First create a cache local version of the MyPackage (cf. Create a conan cache version of the package), then, either by using conan:
```bash
# In release mode
cd test_package
conan install . -if build
conan build . -if build

# In debug mode
cd test_package
conan install . -if build -sbuild_type=Debug -b missing
conan build . -if build
```

or building with pure cmake:
```bash
# In release mode
cd test_package
cmake . -DRUN_CONAN_INSTALL=ON -Bbuild/Release
cmake --build build/Release

# In Debug mode
cd test_package
cmake . -DRUN_CONAN_INSTALL=ON -Bbuild/Debug -DCMAKE_BUILD_TYPE=Debug
cmake --build build/Debug
```
Then, set the MyPackage as editable (cf. Set the package as editable), and repeat. Notice the difference in the ``test_app/build/Release/generators/conan_toolchain.cmake`` and ``test_app/build/Release/generators/MyPackage-release-x86_64-data.cmake``, the path to the MyPackage dependency is now pointing to your workspace
