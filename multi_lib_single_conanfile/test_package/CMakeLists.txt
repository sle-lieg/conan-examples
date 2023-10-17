cmake_minimum_required(VERSION 3.5.0)
project(testpackage)

option(RUN_CONAN_INSTALL "execute conan install step" OFF)

if(${RUN_CONAN_INSTALL})
    set(CMAKE_PREFIX_PATH "${CMAKE_CURRENT_BINARY_DIR}")
    set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_BINARY_DIR}")
    execute_process(COMMAND conan install ${CMAKE_SOURCE_DIR}) # Execution conan install
endif()

# This syntax is purely informative, cmake does not generate an error if a component is not found, only if
# MyPackageConfig.cmake is missing or not in
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
