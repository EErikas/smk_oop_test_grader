import os
import csv
from shutil import rmtree, copy2
from tests2 import perform_tests

base_dir = os.path.dirname(os.path.realpath(__file__))
ex_points = [4, 3, 4, 2, 2, 3, 7]


def write_results(filename, extension, data, delimiter=','):
    results_dir = os.path.join(base_dir, 'results')
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)
    with open(os.path.join(results_dir, '{}_results.{}'.format(filename, extension)), 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)


def get_name(dirname, separator='_', connector=' '):
    return connector.join(dirname.split(separator)[:1])


def prepare_for_grading(directory):
    grading_dir = os.path.join(base_dir, 'grading')
    # clean directory from previous files:
    if os.path.exists(grading_dir):
        rmtree(grading_dir)
    os.mkdir(grading_dir)
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for file in files:
        copy2(file, grading_dir)


def list_students(groups=['KZA', 'PRM'], verbose_output=False):
    submissions_dir = os.path.join(base_dir, 'submissions')
    for group in groups:
        if verbose_output:
            print('\n{}:'.format(group))

        csv_data = [['Name', *['ex-{}'.format(i + 1) for i in range(len(ex_points))], 'Total', 'Grade']]
        group_dir = os.path.join(submissions_dir, group)
        students = sorted(os.listdir(group_dir), key=lambda x: get_name(x).split()[-1])

        for dir in students:
            student_dir = os.path.join(group_dir, dir)
            if os.path.isdir(student_dir):
                prepare_for_grading(student_dir)
                scores = [i * j for i, j in zip(perform_tests(), ex_points)]
                total_score = sum(scores)
                grade = total_score / sum(ex_points) * 10
                # row.extend(scores),
                # row.extend([total_score, grade])
                row = [
                    get_name(dir),
                    *scores,
                    total_score,
                    grade
                ]
                csv_data.append(row)
                if verbose_output:
                    print('{} got {} points which is {}'.format(get_name(dir), total_score, grade))
        write_results(group, 'csv', csv_data)
        write_results(group, 'xls', csv_data, '\t')


if __name__ == '__main__':
    show_results = True
    print('* Grading submissions...')
    if show_results:
        print('{:-^40}'.format('Results'))
    list_students(verbose_output=show_results)
    print('* Done!')
