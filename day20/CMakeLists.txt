cmake_minimum_required(VERSION 3.14)
project(day20)

# GoogleTest requires at least C++14
set(CMAKE_CXX_STANDARD 14)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

add_library(libday20 day20.cpp day20.h)

add_executable(day20 day20_main.cpp)
target_link_libraries(day20 libday20)

add_executable(test_day20 test_day20.cpp)
target_link_libraries(test_day20 libday20 GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(test_day20)
