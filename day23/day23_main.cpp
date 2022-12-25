#include "day23.h"

#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

void simulate(const std::string& filename, size_t maxRounds) {
	std::deque<std::function<std::pair<int, int>(const std::vector<int>&)>> rules { ruleNorth, ruleSouth, ruleWest, ruleEast };

	auto lines {readFile(filename)};
	auto elves {parseLines(lines)};

	for (size_t round = 0; round < maxRounds; ++round) {
		std::cout << "Round " << round << std::endl;

		// render(elves);

		std::vector<std::pair<int, int>> proposedTargetPositions;

		for (const auto& elf : elves) {
			std::vector<int> neighborsOccupied {getOccupiedNeighbors(elf, elves)};
			auto proposedMove {propose(rules, neighborsOccupied)};
			proposedTargetPositions.push_back(elf + proposedMove);
		}

		if (proposedTargetPositions == elves) {
			std::cout << "Part 2: No more changes in round " << round+1 << std::endl;
			break;
		}

		elves.clear();

		for(size_t i = 0; i < proposedTargetPositions.size(); ++i) {
			if (std::count(proposedTargetPositions.cbegin(), proposedTargetPositions.cend(), proposedTargetPositions[i]) == 1) {
				elves.push_back(proposedTargetPositions[i]);
			} else {
				elves.push_back(elves[i]);
			}
		}

		// Rotate rules
		auto rule {rules.front()};
		rules.pop_front();
		rules.push_back(rule);
	}

	if (maxRounds < SIZE_MAX)
		std::cout << "Part 1: " << countEmptyTiles(elves) << std::endl;
}

int main() {
	simulate("example.txt", 10);
	simulate("example.txt", SIZE_MAX);
	return 0;
}
