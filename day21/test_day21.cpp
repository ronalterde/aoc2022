#include "day21.h" 
#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include <fstream>
#include <iostream>
#include <string>

using namespace testing;

TEST(Day21, foo) {
	auto nodes {readFile("example.txt")};
	EXPECT_EQ(nodes.size(), 15);

	EXPECT_EQ(nodes["root"], (std::vector<std::string>{"pppw", "+", "sjmn"}));
	EXPECT_EQ(nodes["lgvd"], (std::vector<std::string>{"ljgn", "*", "ptdq"}));
	EXPECT_EQ(nodes["sllz"], (std::vector<std::string>{"4"}));
}
