#pragma once

#include <vector>
#include <memory>

struct Node {
	Node(int value, Node* next, Node* prev) : value(value), next(next), prev(prev) {
	}

	int value;
	Node* prev;
	Node* next;
};

struct LinkedList {
	LinkedList(std::vector<int> input) {
		for (auto i : input)
			nodes.push_back(std::make_unique<Node>(i, nullptr, nullptr));

		// Init next pointers
		for (size_t i = 0; i < nodes.size() - 1; ++i) {
			nodes[i]->next = nodes[i+1].get();
		}
		nodes[nodes.size()-1]->next = nodes[0].get();

		// Init prev. pointers
		for (size_t i = nodes.size()-1; i > 0; --i) {
			nodes[i]->prev = nodes[i-1].get();
		}
		nodes[0]->prev = nodes[nodes.size()-1].get();
	}

	std::vector<std::unique_ptr<Node>> nodes;
};

void moveNode(Node* src, int count);
std::vector<int> toVector(const Node* start);
void mix(LinkedList& ll);
std::vector<int> readFile(const std::string& filename);
