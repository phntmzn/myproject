cmake_minimum_required(VERSION 3.15)
project(mylib)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Create the library from source
add_library(mylib SHARED
    src/mylib/mylib.cpp
)

# Include header directory
target_include_directories(mylib PUBLIC
    ${PROJECT_SOURCE_DIR}/include
)

# Optional: install the library
install(TARGETS mylib DESTINATION lib)
install(DIRECTORY include/ DESTINATION include)
