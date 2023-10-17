cmake_minimum_required(VERSION 3.5.0)
project(testpackage)

option(RUN_CONAN_INSTALL "Run conan install to get the dependencies when using pure cmake" OFF)

if(${RUN_CONAN_INSTALL})
    # Set the build type to Release by default
    if(NOT CMAKE_BUILD_TYPE)
        set(CMAKE_BUILD_TYPE Release)
    endif()

    execute_process(COMMAND conan install ${CMAKE_CURRENT_SOURCE_DIR} -if=${CMAKE_CURRENT_BINARY_DIR} -sbuild_type=${CMAKE_BUILD_TYPE}) #-b missing

    # The cmake_layout generate the CMakeToolchain files inside a generators folder, inside build/Release
    # (or build/Debug) directory by default.
    # So for cmake to find MyPackageConfig.cmake in the generators folder, include the conan_toolchain.cmake file, which
    # set CMAKE_PREFIX_PATH and CMAKE_MODULE_PATH to the proper paths, among other usefull variables
    include("${CMAKE_CURRENT_BINARY_DIR}/generators/conan_toolchain.cmake")
endif()

# This syntax is purely informative, cmake does not generate an error if a component is not found, only if
# MyPackageConfig.cmake is missing
find_package(MyPackage COMPONENTS bar foo donotexist REQUIRED)

# Check if the "foo" component is found
if(NOT TARGET MyPackage::foo)
    message("Component 'foo' not found.")
endif()

# Check if the "donotexist" component is found
if(NOT TARGET MyPackage::donotexist)
    message("Component 'donotexist' not found.")
endif()

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} MyPackage::foo MyPackage::bar)
