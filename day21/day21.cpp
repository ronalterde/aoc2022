#include "day21.h"
#include <cassert>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <regex>
#include <variant>
#include <unordered_map>

namespace {
}

std::unordered_map<std::string, std::vector<std::string>> readFile(const std::string& filename) {
	std::unordered_map<std::string, std::vector<std::string>> nodes;

	std::ifstream infile{filename};
	std::vector<std::string> lines;
	std::string line;
	while(std::getline(infile, line)) {
		std::smatch match;

		if(std::regex_match(line, match, std::regex{"(.*): (.*) ([+-\\\\*/]) (.*)"})) {
			auto nodeName {match[1].str()};
			auto left {match[2].str()};
			auto op {match[3].str()};
			auto right {match[4].str()};
			nodes[nodeName] = std::vector<std::string> { left, op, right };
		} else if(std::regex_match(line, match, std::regex{"(.*): (.*)"})) {
			auto nodeName {match[1].str()};
			auto value {match[2].str()};
			nodes[nodeName] = std::vector<std::string> { value };
		}
	}
	return nodes;
}
