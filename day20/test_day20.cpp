#include "day20.h"
#include <algorithm>
#include <iostream>

#include <gtest/gtest.h>

TEST(LinkedListTest, init) {
	LinkedList ll{{ 1, 2, 3, 4 }};
	EXPECT_EQ(ll.nodes.size(), 4);
	EXPECT_EQ(ll.nodes[0]->next, ll.nodes[1].get());
	EXPECT_EQ(ll.nodes[3]->next, ll.nodes[0].get());

	EXPECT_EQ(ll.nodes[1]->prev, ll.nodes[0].get());
	EXPECT_EQ(ll.nodes[0]->prev, ll.nodes[3].get());
}

TEST(LinkedListTest, toVector) {
	LinkedList ll{{ 1, 2, 3 }};
	EXPECT_EQ(toVector(ll.nodes[0].get()), std::vector<int>( { 1, 2, 3 }));
	EXPECT_EQ(toVector(ll.nodes[1].get()), std::vector<int>( { 2, 3, 1 }));
	EXPECT_EQ(toVector(ll.nodes[2].get()), std::vector<int>( { 3, 1, 2 }));
}

TEST(LinkedListTest, moveNodeRight) {
	auto ll = LinkedList{{ 1, 2, 3, 4 }};

	auto src = ll.nodes[0].get();
	moveNode(src, 2);
	EXPECT_EQ(toVector(ll.nodes[1].get()), std::vector<int>( { 2, 3, 1, 4 }));

	moveNode(src, 2);
	EXPECT_EQ(toVector(ll.nodes[0].get()), std::vector<int>( { 1, 3, 4, 2 }));
}

TEST(LinkedListTest, moveNodeLeft) {
	auto ll = LinkedList{{ 1, 2, 3, 4 }};

	auto src = ll.nodes[3].get();
	moveNode(src, -1);
	EXPECT_EQ(toVector(ll.nodes[0].get()), std::vector<int>( { 1, 2, 4, 3 }));
}

TEST(LinkedListTest, example) {
	LinkedList ll{{1, 2, -3, 3, -2, 0, 4 }};

	std::vector<Node*> origOrder;
	for (const auto& node : ll.nodes) {
		origOrder.push_back(node.get());
	}

	auto it = origOrder.begin();

	// 1 moves 1 to the right:
	auto node = *it++;
	moveNode(node, node->value);
	EXPECT_EQ(toVector(ll.nodes[1].get()), std::vector<int>( { 2, 1, -3, 3, -2, 0, 4 }));

	// 2 moves 2 to the right:
	node = *it++;
	moveNode(node, node->value);
	EXPECT_EQ(toVector(ll.nodes[0].get()), std::vector<int>( { 1, -3, 2, 3, -2, 0, 4 }));

	// -3 moves 3 to the left:
	node = *it++;
	moveNode(node, node->value);
	EXPECT_EQ(toVector(ll.nodes[0].get()), std::vector<int>( { 1, 2, 3, -2, -3, 0, 4 }));

	// 3 moves 3 to the right:
	node = *it++;
	moveNode(node, node->value);
	EXPECT_EQ(toVector(ll.nodes[0].get()), std::vector<int>( { 1, 2, -2, -3, 0, 3, 4 }));

	// -2 moves
	node = *it++;
	moveNode(node, node->value);
	EXPECT_EQ(toVector(ll.nodes[0].get()), std::vector<int>( { 1, 2, -3, 0, 3, 4, -2 }));

	// 0 does not move
	node = *it++;
	moveNode(node, node->value);
	EXPECT_EQ(toVector(ll.nodes[0].get()), std::vector<int>( { 1, 2, -3, 0, 3, 4, -2 }));

	// 4 moves
	node = *it++;
	moveNode(node, node->value);
	EXPECT_EQ(toVector(ll.nodes[0].get()), std::vector<int>( { 1, 2, -3, 4, 0, 3, -2 }));
}

TEST(LinkedListTest, example_integrated) {
	LinkedList ll{readFile("example.txt")};

	mix(ll);
	auto res = toVector(ll.nodes[0].get());

	auto result = std::find(res.begin(), res.end(), 0);
	EXPECT_NE(result, res.end());
	auto zeroIndex = result - res.begin();

	EXPECT_EQ(res[(zeroIndex+1000) % (res.size())], 4);
	EXPECT_EQ(res[(zeroIndex+2000) % (res.size())], -3);
	EXPECT_EQ(res[(zeroIndex+3000) % (res.size())], 2);

	EXPECT_EQ(res[(zeroIndex+1000) % (res.size())] +
			res[(zeroIndex+2000) % (res.size())] +
			res[(zeroIndex+3000) % (res.size())], 3);
}

TEST(DISABLED_LinkedListTest, realData) {
	LinkedList ll{readFile("input.txt")};

	mix(ll);
	auto res = toVector(ll.nodes[0].get());

	auto result = std::find(res.begin(), res.end(), 0);
	EXPECT_NE(result, res.end());
	auto zeroIndex = result - res.begin();

	EXPECT_EQ(res[(zeroIndex+1000) % (res.size())], 4);
	EXPECT_EQ(res[(zeroIndex+2000) % (res.size())], -3);
	EXPECT_EQ(res[(zeroIndex+3000) % (res.size())], 2);

	EXPECT_EQ(res[(zeroIndex+1000) % (res.size())] +
			res[(zeroIndex+2000) % (res.size())] +
			res[(zeroIndex+3000) % (res.size())], 3);
}
