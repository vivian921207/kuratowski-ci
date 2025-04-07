import unittest
from kuratowski_2 import is_5, is_3, cut_two

def build_empty_graph(n):
    return [[False] * (n + 1) for _ in range(n + 1)]

class TestKuratowskiMainFunctions(unittest.TestCase):

    def test_is_5_true(self):
        graph = build_empty_graph(6)
        group = [1, 2, 3, 4, 5]
        for i in group:
            for j in group:
                if i != j:
                    graph[i][j] = True
        self.assertTrue(is_5(graph, group))

    def test_is_5_false_missing_edge(self):
        graph = build_empty_graph(6)
        group = [1, 2, 3, 4, 5]
        for i in group:
            for j in group:
                if i != j:
                    graph[i][j] = True
        graph[1][2] = False
        graph[2][1] = False
        self.assertFalse(is_5(graph, group))

    def test_is_3_true(self):
        graph = build_empty_graph(7)
        g1 = [1, 2, 3]
        g2 = [4, 5, 6]
        for i in g1:
            for j in g2:
                graph[i][j] = graph[j][i] = True
        self.assertTrue(is_3(graph, g1 + g2))

    def test_is_3_false_internal_link(self):
        graph = build_empty_graph(7)
        g1 = [1, 2, 3]
        g2 = [4, 5, 6]
        for i in g1:
            for j in g2:
                graph[i][j] = graph[j][i] = True
        graph[1][2] = graph[2][1] = True  # g1 應該不相連
        self.assertFalse(is_3(graph, g1 + g2))
    
    def test_is_3_false_cross_missing(self):
        graph = build_empty_graph(7)
        g1 = [1, 2, 3]
        g2 = [4, 5, 6]
        for i in g1:
            for j in g2:
                graph[i][j] = graph[j][i] = True
        graph[1][4] = graph[4][1] = False  # 缺一條必要邊
        self.assertFalse(is_3(graph, g1 + g2))

    def test_cut_two_simplifies_correctly(self):
        graph = build_empty_graph(4)
        graph[1][2] = graph[2][1] = True
        graph[2][3] = graph[3][2] = True
        graph[2][4] = graph[4][2] = True  # node 2 has degree 3
        deg = [0, 1, 3, 1, 1]  # index 0 unused
        cut_two(graph, deg, 4)
        # node 2 remains, not simplified, because deg != 2
        self.assertTrue(graph[2][1])
        self.assertTrue(graph[2][3])
        self.assertTrue(graph[2][4])

        # now make deg[2] = 2 and test cut
        graph[2][4] = graph[4][2] = False
        deg = [0, 1, 2, 1, 0]
        cut_two(graph, deg, 4)
        # node 2 should be removed, 1-3 connected
        self.assertFalse(graph[1][2])
        self.assertFalse(graph[2][3])
        self.assertTrue(graph[1][3])

if __name__ == "__main__":
    unittest.main()
