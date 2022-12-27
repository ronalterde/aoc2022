#include "day21.h"

#include <cassert>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <regex>
#include <variant>
#include <unordered_map>
#include <cstdint>
#include <iomanip>

std::unordered_map<std::string, std::vector<std::string>> nodes;

int64_t f(const std::string& node) {
	// std::cout << "f: " << node << std::endl;

	auto n = nodes[node];
	if (n.size() == 1) {
		return std::stoi(n[0]);
	} else if (n.size() == 3) {
		auto left{n[0]};
		auto op{n[1]};
		auto right{n[2]};
		if (op == "+")
			return f(left) + f(right);
		else if (op == "-")
			return f(left) - f(right);
		else if (op == "*")
			return f(left) * f(right);
		else if (op == "/")
			return f(left) / f(right);
		else
			assert(false);
	} else {
		assert(false);
	}
}

bool g(const std::string& node) {
	auto n = nodes[node];
	if (n.size() == 1) {
		// leaf
		return node == "humn";
	} else if (n.size() == 3) {
		auto left{n[0]};
		auto op{n[1]};
		auto right{n[2]};
		return g(left) || g(right);
	} else {
		assert(false);
	}
}

int64_t f2(const std::string& node, int64_t result) {
	// std::cout << "f2: " << node << std::endl;

	auto n = nodes[node];
	if (n.size() == 1) {
		return result;
	} else if (n.size() == 3) {
		auto left{n[0]};
		auto op{n[1]};
		auto right{n[2]};
		if (g(left)) {
			if (op == "+")
				return f2(left, result - f(right));
			else if (op == "-")
				return f2(left, result + f(right));
			else if (op == "*")
				return f2(left, result / f(right));
			else if (op == "/")
				return f2(left, result * f(right));
			else
				assert(false);
		} else {
			if (op == "+")
				return f2(right, result - f(left));
			else if (op == "-")
				return f2(right, result + f(left));
			else if (op == "*")
				return f2(right, result / f(left));
			else if (op == "/")
				return f2(right, result * f(left));
			else
				assert(false);
		}
	} else {
		assert(false);
	}
}

int main() {
	nodes = readFile("example.txt");

	std::cout << "Part 1: " << f("root") << std::endl;

	// Part 2:
	// 1. Calculate some of other branch (where 'humn' is not in)
	// 2. Go down the branch where 'humn' is in, inverting operations
	int64_t sum{0};
	std::string part2Start;
	if (g(nodes["root"][0])) {
		sum = f(nodes["root"][2]);
		part2Start = nodes["root"][0];
	} else if (g(nodes["root"][2])) {
		sum = f(nodes["root"][0]);
		part2Start = nodes["root"][2];
	}

	// std::cout << "sum: " << sum << std::endl;
	std::cout << "Part 2: " << f2(part2Start, sum) << std::endl;
	// 8759966720571 is NOT the right solution.

	return 0;
}
