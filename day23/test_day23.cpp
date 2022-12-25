#include "day23.h"

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include <fstream>
#include <iostream>
#include <string>

using namespace testing;

TEST(Day23, parseExampleFile) {
	auto lines {readFile("example.txt")};
	EXPECT_EQ(lines.size(), 7);

	auto points {parseLines(lines)};
	ASSERT_THAT(points, ElementsAre(
				Pair(4, 0),
				Pair(2, 1), Pair(3, 1), Pair(4, 1), Pair(6, 1),
				Pair(0, 2), Pair(4, 2), Pair(6, 2),
				Pair(1, 3), Pair(5, 3), Pair(6, 3),
				Pair(0, 4), Pair(2, 4), Pair(3, 4), Pair(4, 4),
				Pair(0, 5), Pair(1, 5), Pair(3, 5), Pair(5, 5), Pair(6, 5),
				Pair(1, 6), Pair(4, 6)));
}

TEST(Day23, rules) {
	// Do nothing if no neighbor at all (applies to any rule)
	EXPECT_EQ(ruleNorth({0, 0, 0, 0, 0, 0, 0, 0}), (std::pair<int, int>{0, 0}));
	EXPECT_EQ(ruleSouth({0, 0, 0, 0, 0, 0, 0, 0}), (std::pair<int, int>{0, 0}));
	EXPECT_EQ(ruleWest({0, 0, 0, 0, 0, 0, 0, 0}), (std::pair<int, int>{0, 0}));
	EXPECT_EQ(ruleEast({0, 0, 0, 0, 0, 0, 0, 0}), (std::pair<int, int>{0, 0}));

	// don't move
	EXPECT_EQ(ruleNorth({1, 0, 0, 0, 0, 0, 0, 0}), (std::pair<int, int>{0, 0}));
	EXPECT_EQ(ruleNorth({0, 1, 0, 0, 0, 0, 0, 0}), (std::pair<int, int>{0, 0}));
	EXPECT_EQ(ruleNorth({0, 0, 1, 0, 0, 0, 0, 0}), (std::pair<int, int>{0, 0}));
	
	// move North
	EXPECT_EQ(ruleNorth({0, 0, 0, 1, 0, 0, 0, 0}), (std::pair<int, int>{0, -1}));
	EXPECT_EQ(ruleNorth({0, 0, 0, 0, 0, 1, 1, 0}), (std::pair<int, int>{0, -1}));

	// don't move
	EXPECT_EQ(ruleSouth({0, 0, 0, 0, 0, 1, 0, 0}), (std::pair<int, int>{0, 0}));
	EXPECT_EQ(ruleSouth({0, 0, 0, 0, 0, 0, 1, 0}), (std::pair<int, int>{0, 0}));
	EXPECT_EQ(ruleSouth({0, 0, 0, 0, 0, 0, 0, 1}), (std::pair<int, int>{0, 0}));
	
	// move South
	EXPECT_EQ(ruleSouth({0, 0, 0, 0, 1, 0, 0, 0}), (std::pair<int, int>{0, 1}));
	
	// don't move
	EXPECT_EQ(ruleWest({1, 0, 0, 0, 0, 0, 0, 0}), (std::pair<int, int>{0, 0}));
	EXPECT_EQ(ruleWest({0, 0, 0, 1, 0, 0, 0, 0}), (std::pair<int, int>{0, 0}));
	EXPECT_EQ(ruleWest({0, 0, 0, 0, 0, 1, 0, 0}), (std::pair<int, int>{0, 0}));
	
	// move West
	EXPECT_EQ(ruleWest({0, 1, 0, 0, 0, 0, 0, 0}), (std::pair<int, int>{-1, 0}));

	// don't move
	EXPECT_EQ(ruleEast({0, 0, 1, 0, 0, 0, 0, 0}), (std::pair<int, int>{0, 0}));
	EXPECT_EQ(ruleEast({0, 0, 0, 0, 1, 0, 0, 0}), (std::pair<int, int>{0, 0}));
	EXPECT_EQ(ruleEast({0, 0, 0, 0, 0, 0, 0, 1}), (std::pair<int, int>{0, 0}));
	
	// move East
	EXPECT_EQ(ruleEast({0, 1, 0, 0, 0, 0, 0, 0}), (std::pair<int, int>{1, 0}));
}

TEST(Day23, selectRules) {
	auto ruleThatApplies {[](const std::vector<int>&) { return std::pair<int, int>(1, 0); }};
	auto ruleThatApplies2 {[](const std::vector<int>&) { return std::pair<int, int>(0, 1); }};
	auto ruleThatDoesntApply {[](const std::vector<int>&) { return std::pair<int, int>(0, 0); }};

	std::deque<std::function<std::pair<int, int>(const std::vector<int>&)>> rules { ruleThatDoesntApply, ruleThatDoesntApply };
	EXPECT_EQ(propose(rules, {}), (std::pair<int, int>(0, 0)));

	rules = { ruleThatDoesntApply, ruleThatDoesntApply, ruleThatApplies };
	EXPECT_EQ(propose(rules, {}), (std::pair<int, int>(1, 0)));

	rules = { ruleThatApplies2 };
	EXPECT_EQ(propose(rules, {}), (std::pair<int, int>(0, 1)));
}

TEST(Day23, rotate) {
	std::deque<std::function<std::pair<int, int>(const std::vector<int>&)>> rules { ruleNorth, ruleSouth, ruleWest, ruleEast };

	auto rule = rules.front();
	rules.pop_front();
	rules.push_back(rule);
}

TEST(Day23, getOccupiedNeighborsExample) {
	auto lines {readFile("example.txt")};
	auto elves {parseLines(lines)};
	auto elf = elves[0];
	std::vector<int> neighborsOccupied = getOccupiedNeighbors(elf, elves);

	ASSERT_THAT(getOccupiedNeighbors(elves[0], elves), ElementsAre(0, 0, 0, 0, 0, 1, 1, 0));
	ASSERT_THAT(getOccupiedNeighbors(elves[1], elves), ElementsAre(0, 0, 0, 0, 1, 0, 0, 0));
	ASSERT_THAT(getOccupiedNeighbors(elves[4], elves), ElementsAre(0, 0, 0, 0, 0, 0, 1, 0));
	ASSERT_THAT(getOccupiedNeighbors(elves[5], elves), ElementsAre(0, 0, 0, 0, 0, 0, 0, 1));
	ASSERT_THAT(getOccupiedNeighbors(elves[6], elves), ElementsAre(1, 1, 0, 0, 0, 0, 0, 1));
}

TEST(Day23, getOccupiedNeighborsExampleSimple) {
	// std::vector<std::string> lines {
	// 	".....",
	// 	"..##.",
	// 	"..#..",
	// 	".....",
	// 	"..##.",
	// 	".....",
	// };

	std::vector<std::string> lines {
		"..##.",
		".....",
		"..#..",
		"...#.",
		"..#..",
		".....",
	};

	auto elves { parseLines(lines) };
	auto elf = elves[0];
	std::vector<int> neighborsOccupied = getOccupiedNeighbors(elf, elves);

	ASSERT_THAT(getOccupiedNeighbors(elf, elves), ElementsAre(0, 0, 0, 0, 1, 0, 0, 0));
}

TEST(Day23, countEmptyTiles) {
	std::vector<std::string> lines {
		"##",
		"..",
		"#.",
		".#",
		"#.",
	};

	auto elves { parseLines(lines) };
	EXPECT_EQ(countEmptyTiles(elves), 5);

	lines = readFile("input.txt");
	EXPECT_EQ(lines.size(), 71);

	elves = parseLines(lines);
	EXPECT_EQ(countEmptyTiles(elves), 2547);
	EXPECT_EQ(elves.size(), 2494);
	EXPECT_EQ(countEmptyTiles(elves) + elves.size(), 71*71);
}
