#pragma once

#include <string>
#include <vector>
#include <deque>
#include <functional>

std::vector<std::string> readFile(const std::string& filename);
std::vector<std::pair<int, int>> parseLines(const std::vector<std::string>& lines);
std::pair<int, int> propose(const std::deque<std::function<std::pair<int, int>(const std::vector<int>&)>>& rules,
		const std::vector<int>& vec);
std::pair<int, int> ruleNorth(const std::vector<int>& vec);
std::pair<int, int> ruleSouth(const std::vector<int>& vec);
std::pair<int, int> ruleWest(const std::vector<int>& vec);
std::pair<int, int> ruleEast(const std::vector<int>& vec);
std::vector<int> getOccupiedNeighbors(const std::pair<int, int>& elf, const std::vector<std::pair<int, int>>& elves);
std::pair<int, int> operator+(const std::pair<int, int>& x, const std::pair<int, int>& y);
void render(const std::vector<std::pair<int, int>>& vec);
int countEmptyTiles(const std::vector<std::pair<int, int>>& vec);
