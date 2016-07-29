"""
https://www.coursera.org/learn/algorithms-on-strings/

>>> trie = Trie()
>>> trie.insert_many(['ATAGA', 'ATC', 'GAT'])
>>> list(format_trie(trie.root))
0->1:A
1->2:T
2->3:A
3->4:G
4->5:A
2->6:C
0->7:G
7->8:A
8->9:T
"""

import itertools


class Trie:

    def __init__(self):
        self.counter = itertools.count(0)
        self.root = self._create_node()

    def insert(self, s):
        current = self.root[1]
        for ch in s:
            if ch not in current:
                current[ch] = self._create_node()
            current = current[ch][1]

    def insert_many(self, strings):
        for s in strings:
            self.insert(s)

    def _create_node(self):
        return [next(self.counter), {}]

    def __repr__(self):
        return repr(self.root)


def format_trie(node, start=None, char=None):
    if start is not None:
        yield '%d->%d:%s' % (start, node[0], char)
    for char in node[1]:
        yield from format_trie(node[1][char], start=node[0], char=char)
