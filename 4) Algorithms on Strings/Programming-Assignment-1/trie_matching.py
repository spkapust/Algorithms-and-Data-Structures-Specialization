# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4

def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    nodes = 1
    for p in patterns:
        currentNode = 0
        for c in p:
            if c not in tree[currentNode]:
                tree[currentNode][c] = nodes
                tree[nodes] = {}
                nodes += 1  
            currentNode = tree[currentNode][c]
    return tree

def prefix_trie_matching(text, trie):
	currentNode = 0
	for c in text:
		if c not in trie[currentNode]:
			return False
		else:
			currentNode = trie[currentNode][c]
			if trie[currentNode] == {}:
				return True


def solve (text, n, patterns):
	trie = build_trie(patterns)
	result = []
	for idx, _ in enumerate(text):
		t = text[idx:]
		if prefix_trie_matching(t, trie):
			result.append(idx)

	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
