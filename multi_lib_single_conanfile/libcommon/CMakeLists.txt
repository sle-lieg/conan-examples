cmake_minimum_required(VERSION 3.5.0)
project(common)

set(COMMON_INCLUDE_DIR include)
set(COMMON_SRC_DIR src)

set(COMMON_HEADER_FILES ${COMMON_INCLUDE_DIR}/common.h)
set(COMMON_SRC_FILES ${COMMON_SRC_DIR}/common.cpp)


add_library(${PROJECT_NAME} STATIC ${COMMON_SRC_FILES})
target_include_directories(${PROJECT_NAME} PUBLIC ${COMMON_INCLUDE_DIR})

# So we can link this static library with libfoo.so and libbar.so
set_property(TARGET ${PROJECT_NAME} PROPERTY POSITION_INDEPENDENT_CODE ON)
