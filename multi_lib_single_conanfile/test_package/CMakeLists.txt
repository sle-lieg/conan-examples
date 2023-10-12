cmake_minimum_required(VERSION 3.5.0)
project(testpackage)

option(RUN_CONAN_INSTALL "execute conan install step" OFF)

if(${RUN_CONAN_INSTALL})
    set(CMAKE_PREFIX_PATH "${CMAKE_CURRENT_BINARY_DIR}")
    set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_BINARY_DIR}")
    # set(CMAKE_BUILD_TYPE "Release")
    execute_process(COMMAND conan install ${CMAKE_SOURCE_DIR}) # Execution conan install
endif()

find_package(MyPackage REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} MyPackage::foo MyPackage::bar)
