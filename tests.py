from algs import important_algs as ia
from algs import sort as s


class Test:
    def test_test(self):
        assert True == True # noqa
        assert False == False # noqa


class TestALGS:
    def test_alg_min(self):
        assert ia.alg_min(5, 10) == 5
        assert ia.alg_min(-1, 10) == -1
        assert ia.alg_min(2, 4) == 2
        assert ia.alg_min(1, 100) == 1
        assert ia.alg_min(90, 999) == 90

    def test_alg_max(self):
        assert ia.alg_max(5, 10) == 10
        assert ia.alg_max(-1, 10) == 10
        assert ia.alg_max(2, 4) == 4
        assert ia.alg_max(1, 100) == 100
        assert ia.alg_max(90, 999) == 999

    def test_iter_nww(self):
        assert ia.iter_nww(10, 15) == 30
        assert ia.iter_nww(3, 4) == 12
        assert ia.iter_nww(15, 75) == 75


class TestSort:
    def test_insertion_sort(self):
        array = [12, 11, 13, 5, 6]
        s.insertion_sort(array)
        assert array == [5, 6, 11, 12, 13]
