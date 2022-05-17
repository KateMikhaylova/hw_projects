import os


def get_files_list(path):
    files_list = [os.path.join(path, file) for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    return files_list


def count_lines(file):
    with open(file, encoding='utf-8') as file_obj:
        return file, len(file_obj.readlines())


def sort_files(files_list):
    files_with_len = list(map(count_lines, files_list))
    return sorted(files_with_len, key=lambda x: x[1])


def create_result_file(result_file, sorted_files_list):
    with open(result_file, 'w') as file_obj:
        for name_len_tuple in sorted_files_list:
            with open(name_len_tuple[0], encoding='utf-8') as initial_file:
                file_obj.write(os.path.basename(name_len_tuple[0]) + '\n')
                file_obj.write(str(name_len_tuple[1]) + '\n')
                for line in initial_file:
                    file_obj.write(line.strip() + '\n')


CURRENT_DIR = os.getcwd()
FILES_FOR_SORTING_DIR = 'sorted'
final_dir = os.path.join(CURRENT_DIR, FILES_FOR_SORTING_DIR)
create_result_file('result.txt', sort_files(get_files_list(final_dir)))
