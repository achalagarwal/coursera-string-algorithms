from week1.trie import format_trie
from week1.trie import Trie


class TestTrieInsert:

    def test_builds_a_trie(self):
        trie = Trie()
        trie.insert('ATC')
        assert trie.root == [0, {
            'A': [1, {
                'T': [2, {
                    'C': [3, {}],
                    }],
                }],
            }]


class TestTrieInsertMany:

    def test_builds_a_trie_1(self):
        trie = Trie()
        trie.insert_many(['AT', 'AG', 'AC'])
        assert trie.root == [0, {
            'A': [1, {
                'C': [4, {}],
                'G': [3, {}],
                'T': [2, {}],
            }],
        }]



    def test_builds_a_trie_2(self):
        trie = Trie()
        trie.insert_many(['ATAGA', 'ATC', 'GAT'])
        assert trie.root == [0, {
            'A': [1, {
                'T': [2, {
                    'A': [3, {
                        'G': [4, {
                            'A': [5, {}],
                            }],
                        }],
                    'C': [6, {}],
                    }]
                }],
            'G': [7, {
                'A': [8, {
                    'T': [9, {}],
                    }],
                }],
            }]


class TestFormatTrie:

    def test_returns_a_list_of_edges(self):
        trie = Trie()
        trie.insert_many(['ATAGA', 'ATC', 'GAT'])
        assert sorted(list(format_trie(trie.root))) == [
            '0->1:A',
            '0->7:G',
            '1->2:T',
            '2->3:A',
            '2->6:C',
            '3->4:G',
            '4->5:A',
            '7->8:A',
            '8->9:T',
        ]
