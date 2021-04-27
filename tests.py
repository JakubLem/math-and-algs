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
        assert ia.iter_nww(3, 6) == 6

    def test_quadratic_equation(self):
        a = 1
        b = 6
        c = 9
        assert ia.quadratic_equation(a, b, c).string == "(x-3.0)(x-3.0)"

    def test_array_min(self):
        array = [9, 2, 15, 16, 17]
        assert ia.array_min(array) == 2

        array = [190, 7, 18, 17, 20]
        assert ia.array_min(array) == 7

    def test_array_max(self):
        array = [9, 2, 15, 16, 17]
        assert ia.array_max(array) == 17

        array = [190, 7, 18, 17, 20]
        assert ia.array_max(array) == 190

    def test_int_to_binary(self, random_numbers):
        for rn in random_numbers:
            print(rn)
            assert ia.int_to_binary_v1(rn) == "{0:b}".format(rn)


class TestSort:
    def test_insertion_sort(self, my_lists):
        for my_list in my_lists:
            correct = sorted(my_list)
            s.insertion_sort(my_list)
            assert correct == my_list

    def test_bubble_sort_1(self, my_lists):
        for my_list in my_lists:
            correct = sorted(my_list)
            assert s.bubble_sort_v1(my_list) == correct

    def test_bubble_sort_2(self, my_lists):
        for my_list in my_lists:
            correct = sorted(my_list)
            assert s.bubble_sort_v2(my_list) == correct

    def test_bubble_sort_3(self, my_lists):
        for my_list in my_lists:
            correct = sorted(my_list)
            assert s.bubble_sort_v3(my_list) == correct

    def test_bubble_sort_4(self, my_lists):
        for my_list in my_lists:
            correct = sorted(my_list)
            assert s.bubble_sort_v4(my_list) == correct

    def test_heap_sort(self, my_lists):
        for my_list in my_lists:
            correct = sorted(my_list)
            s.heap_sort(my_list)
            assert my_list == correct


class TestPower:
    def test_iter_power(self, correct_powers):
        for correct_power in correct_powers:
            assert ia.iter_pow(correct_power.n, correct_power.p) == correct_power.correct_power

    def test_rec_power(self, correct_powers):
        for correct_power in correct_powers:
            assert ia.rec_pow(correct_power.n, correct_power.p) == correct_power.correct_power
