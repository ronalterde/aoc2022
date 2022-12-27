cmake_minimum_required(VERSION 3.14)
project(day21)

# GoogleTest requires at least C++14
set(CMAKE_CXX_STANDARD 20)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

add_library(libday21 day21.cpp day21.h)

add_executable(day21 day21_main.cpp)
target_link_libraries(day21 libday21)

add_executable(test_day21 test_day21.cpp)
target_link_libraries(test_day21 libday21 GTest::gtest_main gmock_main)

include(GoogleTest)
gtest_discover_tests(test_day21)
