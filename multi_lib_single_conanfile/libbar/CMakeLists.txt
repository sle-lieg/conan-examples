cmake_minimum_required(VERSION 3.5.0)
project(bar)

set(INCLUDE_DIR include)
set(SRC_DIR src)

set(HEADER_FILES ${INCLUDE_DIR}/bar.h)
set(SRC_FILES ${SRC_DIR}/bar.cpp)

add_library(${PROJECT_NAME} SHARED ${SRC_FILES})
target_link_libraries(${PROJECT_NAME} common)
target_include_directories(${PROJECT_NAME} PUBLIC ${INCLUDE_DIR})

set_target_properties(${PROJECT_NAME} PROPERTIES PUBLIC_HEADER ${HEADER_FILES})

install(
    TARGETS ${PROJECT_NAME}
    LIBRARY DESTINATION lib/${PROJECT_NAME}
    PUBLIC_HEADER DESTINATION include/${PROJECT_NAME}
)
