project(Acme CXX)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_compile_options(-std=c++14)

include_directories(
    src
    ${CONAN_INCLUDE_DIRS})


add_custom_target(check COMMAND ${CMAKE_CTEST_COMMAND})

add_library(AcmeLib src/acme.cpp)
target_link_libraries(AcmeLib ${CONAN_LIBS})


add_executable(test_acme_exe src/test_acme.cpp)
target_link_libraries(test_acme_exe  AcmeLib)

add_test(test_acme ${EXECUTABLE_OUTPUT_PATH}/bin/test_acme)
add_dependencies(check test_acme)
