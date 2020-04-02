from importlib import reload
from submission_tests.correct_answers import ex1, ex2, ex5
from submission_tests.correct_answers import ex3, ex4, ex7, ex6


def check_ex_1():
    try:
        import grading.ex1
        reload(grading.ex1)
        vals = [
            [[14, 57, 93, 1], 8],
            [[8, 23, 4, 11], 2],
            [[33, 45, 7, 101]]
        ]
        for val in vals:
            if ex1.sorted_and_multiplied(*val) != grading.ex1.sorted_and_multiplied(*val):
                return 0.5
        return 1
    except:
        return 0


def check_ex_2():
    try:
        import grading.ex2
        reload(grading.ex2)
        vals = [
            (3, 4, 5),
            (3, 8, 5),
            (5, 12, 13)
        ]
        for val in vals:
            if ex2.pythagorean_checker(*val) != grading.ex2.pythagorean_checker(*val):
                return 0.5
        return 1
    except:
        return 0


def check_ex_3():
    try:
        import grading.ex3
        reload(grading.ex3)
        vals = [
            ['ABCDEFGH', 2],
            ['AABCAAADA', 3],
            ['AABCADAA', 4],
            ['AABCAAADA', 'trys'],
            ['AABCAAADA', 5]
        ]
        for val in vals:
            if ex3.split_values(*val) != grading.ex3.split_values(*val):
                return 0.5
        return 1
    except:
        return 0


def check_ex_4():
    try:
        import grading.ex4
        reload(grading.ex4)
        vals = [
            'aaavvvfdff',
            'avtvvvff'
        ]
        for val in vals:
            if ex4.pack(val) != grading.ex4.pack(val):
                return 0.5
        return 1
    except:
        return 0


def check_ex_5():
    try:
        import grading.ex5
        reload(grading.ex5)
        vals = [
            [
                [1, 10, 34, 110, 400, 30, 20],
                [-5, -10, 55, 120, 30],
                [2, 67, 23, 78, 200],
            ],
            [
                [-1, 45, 23, 32, 999],
                [67, 99, 23],
                [23],
            ]
        ]
        for val in vals:
            if ex5.list_operations(val) != [list(foo) for foo in grading.ex5.list_operations(val)]:
                return 0.5
        return 1
    except:
        return 0


def check_ex_6():
    try:
        import grading.ex6
        reload(grading.ex6)
        vals = [
            ['Federal Bureau of Investigation'],
            ['Customs and Border Protection', ' '],
            ['Central Intelligence Agency', '.']
        ]
        for val in vals:
            if ex6.get_acronym(*val) != grading.ex6.get_acronym(*val):
                return 0.5
        return 1
    except:
        return 0


def check_ex_7():
    try:
        import grading.ex7
        reload(grading.ex7)
        vals = [
            ('10', '10', '10'),
            ('12', '43', '2'),
            ('101', 'a', '11'),
            ('1', '20', 'z'),
            ('10', '85', '11')
        ]
        for val in vals:
            if ex7.calculate(*val) != grading.ex7.calculate(*val):
                return 0.5
        return 1
    except:
        return 0


def perform_tests():
    return [
        check_ex_1(),
        check_ex_2(),
        check_ex_3(),
        check_ex_4(),
        check_ex_5(),
        check_ex_6(),
        check_ex_7()
    ]
