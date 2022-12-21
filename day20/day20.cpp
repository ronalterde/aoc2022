#include "day20.h"
#include <fstream>
#include <iostream>

void moveNode(Node* src, int count) {
	if (count == 0)
		return;

	auto old_left = src->prev;
	auto old_right = src->next;

	// Advance to insert pos.
	auto curr = src;
	if (count > 0) {
		for (int i = 0; i < count; ++i) {
			curr = curr->next;
		}
	} else {
		for (int i = 0; i >= count; --i) {
			curr = curr->prev;
		}
	}

	auto new_left = curr;
	auto new_right = curr->next;

	// Fix pointers
	src->prev = new_left;
	src->next = new_right;

	new_left->next = src;
	new_right->prev = src;

	old_left->next = old_right;
	old_right->prev = old_left;
}

std::vector<int> toVector(const Node* start) {
	std::vector<int> v;
	const Node* curr = start;
	do {
		v.push_back(curr->value);
		curr = curr->next;
	} while (curr != start);
	return v;
}

void mix(LinkedList& ll) {
	std::vector<Node*> origOrder;
	for (const auto& node : ll.nodes) {
		origOrder.push_back(node.get());
	}

	for (auto& it : origOrder) {
		moveNode(it, it->value);
	}
}

std::vector<int> readFile(const std::string& filename) {
	std::ifstream infile{filename};

	std::vector<int> inVec;
	for (std::string line; getline(infile, line); ) {
		inVec.push_back(atoi(line.c_str()));
	}

	return inVec;
}
