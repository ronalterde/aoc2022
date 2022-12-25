#include "day23.h"
#include <cassert>
#include <fstream>
#include <iostream>
#include <algorithm>

namespace {

bool allZero(const std::vector<int>& vec) {
	return std::all_of(vec.cbegin(), vec.cend(), [](int x) { return x == 0; });
}

auto getMinMax(const std::vector<std::pair<int, int>>& vec) {
	auto min_x = std::min_element(vec.begin(), vec.end(),
			[](const std::pair<int, int>& a, const std::pair<int, int>& b) { return a.first < b.first; } );

	auto min_y = std::min_element(vec.begin(), vec.end(),
			[](const std::pair<int, int>& a, const std::pair<int, int>& b) { return a.second < b.second; } );

	auto max_x = std::max_element(vec.begin(), vec.end(),
			[](const std::pair<int, int>& a, const std::pair<int, int>& b) { return a.first < b.first; } );

	auto max_y = std::max_element(vec.begin(), vec.end(),
			[](const std::pair<int, int>& a, const std::pair<int, int>& b) { return a.second < b.second; } );

	return std::make_tuple(min_x->first, min_y->second, max_x->first, max_y->second);
}

}

std::vector<std::string> readFile(const std::string& filename) {
	std::ifstream infile{filename};
	std::vector<std::string> lines;
	std::string line;
	while (!infile.eof()) {
		infile >> line;
		lines.push_back(line);
	}
	return lines;
}

std::vector<std::pair<int, int>> parseLines(const std::vector<std::string>& lines) {
	int x{0};
	int y{0};
	std::vector<std::pair<int, int>> p;

	for (const auto& i : lines) {
		auto it = i.cbegin();
		while(true) {
			it = find(it, i.cend(), '#');
			if (it == i.cend())
				break;
			else
				p.push_back(std::make_pair(it-i.cbegin(), y));
				it = std::next(it);
		}
		y++;
	}
	return p;
}

std::pair<int, int> propose(const std::deque<std::function<std::pair<int, int>(const std::vector<int>&)>>& rules,
		const std::vector<int>& vec) {
	for (auto& rule : rules) {
		auto ret = rule(vec);
		// TODO: Use std::optional for "not matching"?
		if (ret.first != 0 || ret.second != 0)
			return ret;
	}
	return std::pair<int, int>(0, 0);
}

std::pair<int, int> ruleNorth(const std::vector<int>& vec) {
	if (allZero(vec))
		return std::pair<int, int>(0, 0);

	if (std::any_of(vec.cbegin(), vec.cbegin()+3, [](int x) { return x == 1; }))
		return std::pair<int, int>(0, 0);
	else
		return std::pair<int, int>(0, -1);
}

std::pair<int, int> ruleSouth(const std::vector<int>& vec) {
	if (allZero(vec))
		return std::pair<int, int>(0, 0);

	if (std::any_of(vec.cend()-3, vec.cend(), [](int x) { return x == 1; }))
		return std::pair<int, int>(0, 0);
	else
		return std::pair<int, int>(0, 1);
}

std::pair<int, int> ruleWest(const std::vector<int>& vec) {
	if (allZero(vec))
		return std::pair<int, int>(0, 0);

	if (vec[0] == 1 || vec[3] == 1 || vec[5] == 1)
		return std::pair<int, int>(0, 0);
	else
		return std::pair<int, int>(-1, 0);
}

std::pair<int, int> ruleEast(const std::vector<int>& vec) {
	if (allZero(vec))
		return std::pair<int, int>(0, 0);

	if (vec[2] == 1 || vec[4] == 1 || vec[7] == 1)
		return std::pair<int, int>(0, 0);
	else
		return std::pair<int, int>(1, 0);
}

std::pair<int, int> operator+(const std::pair<int, int>& x, const std::pair<int, int>& y) {
    return std::make_pair(x.first + y.first, x.second + y.second);
}

std::vector<int> getOccupiedNeighbors(const std::pair<int, int>& elf, const std::vector<std::pair<int, int>>& elves) {
	// Put all eight neighbors in a vector (1 if occupied, 0 if not)

	/* 
	 * 0 1 2
	 * 3 o 4
	 * 5 6 7
	 *
	 * x -> right
	 * y -> down
	 */


	std::vector<std::pair<int, int>> neighborPoints {
		{ elf + std::pair<int, int>(-1, -1) },
		{ elf + std::pair<int, int>(0, -1) },
		{ elf + std::pair<int, int>(1, -1) },
		{ elf + std::pair<int, int>(-1, 0) },
		{ elf + std::pair<int, int>(1, 0) },
		{ elf + std::pair<int, int>(-1, 1) },
		{ elf + std::pair<int, int>(0, 1) },
		{ elf + std::pair<int, int>(1, 1) },
	};

	std::vector<int> neighborsOccupied;
	for (const auto& neighbor : neighborPoints) {
		auto value { std::find(elves.cbegin(), elves.cend(), neighbor) == elves.cend() ? 0 : 1 };
		neighborsOccupied.push_back(value);
	}
	return neighborsOccupied;
}

void render(const std::vector<std::pair<int, int>>& vec) {
	auto [min_x, min_y, max_x, max_y] = getMinMax(vec);

	for(int y = min_y; y <= max_y; ++y) {
		for(int x = min_x; x <= max_x; ++x) {
			if (std::find(vec.cbegin(), vec.cend(),
					std::pair<int, int>(x, y)) != vec.cend()) {
				std::cout << "#";
			} else {
				std::cout << ".";
			}
		}
		std::cout << std::endl;
	}
}

int countEmptyTiles(const std::vector<std::pair<int, int>>& vec) {
	auto [min_x, min_y, max_x, max_y] = getMinMax(vec);

	int sum{0};

	for(int y = min_y; y <= max_y; ++y) {
		for(int x = min_x; x <= max_x; ++x) {
			if (std::find(vec.cbegin(), vec.cend(),
					std::pair<int, int>(x, y)) != vec.cend()) {
			} else {
				sum += 1;
			}
		}
	}

	return sum;
}
