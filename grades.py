import os
import csv
from shutil import rmtree, copy2
import xlsxwriter
from submission_tests.tests2 import perform_tests

base_dir = os.path.dirname(os.path.realpath(__file__))
submissions_dir = os.path.join(base_dir, 'submissions')
results_dir = os.path.join(base_dir, 'results')
ex_points = [4, 3, 4, 2, 2, 3, 7]


def write_results_csv(filename, extension, data, delimiter=','):
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)
    with open(os.path.join(results_dir, '{}_results.{}'.format(filename, extension)), 'w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)


def write_results_xlsx(groups_data):
    workbook = xlsxwriter.Workbook(os.path.join(results_dir, 'results.xlsx'))
    for group_data in groups_data:
        # Get group name and results
        group_name, group_results = tuple(group_data.items())[0]
        worksheet = workbook.add_worksheet(group_name)
        worksheet.set_column('A:A', 25)
        for row in range(len(group_results)):
            for col in range(len(group_results[row])):
                data_to_write = [row, col, group_results[row][col]]
                if row == 0 or col == 0:
                    worksheet.write(*data_to_write)
                else:
                    worksheet.write_number(*data_to_write)
    workbook.close()


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


def list_students(groups, verbose_output=False):
    all_results = []
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
                row = [
                    get_name(dir),
                    *scores,
                    total_score,
                    grade
                ]

                csv_data.append(row)
                if verbose_output:
                    print('{} got {} points which is {}'.format(get_name(dir), total_score, grade))
        all_results.append({group: csv_data})
        write_results_csv(group, 'csv', csv_data)
    write_results_xlsx(all_results)


if __name__ == '__main__':
    groups = ['KZA', 'PRM']
    show_results = True
    # Check submissions if submission folder exists
    if os.path.exists(submissions_dir):
        print('* Grading submissions...')
        if show_results:
            print('{:-^40}'.format('Results'))
        list_students(groups, verbose_output=show_results)
        print('* Done!')
    # Create submission folder structure
    else:
        print('Creating submission directory structure... ')
        os.mkdir(submissions_dir)
        for group in groups:
            os.mkdir(os.path.join(submissions_dir, group))
        print('* Done!')
