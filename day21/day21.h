#pragma once

#include <string>
#include <vector>
#include <deque>
#include <functional>

std::unordered_map<std::string, std::vector<std::string>> readFile(const std::string& filename);
