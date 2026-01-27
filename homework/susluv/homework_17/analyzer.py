import argparse
import os

from colorama import Fore, Style

parser = argparse.ArgumentParser(description='Find TEXT in files in FOLDER')
parser.add_argument('folder', type=str, help='path to folder')
parser.add_argument('-t', '--text', type=str, help='text you look for')
args = parser.parse_args()

log_files = []

for file in os.listdir(args.folder):
    filename = os.fsdecode(file)
    if filename.endswith('.log'):
        log_files.append(os.path.join(args.folder, filename))


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line


lines_with_words_counter = 0
result_dict = {}
for file in log_files:
    file_dict = {}
    for data_line in read_file(file):
        if args.text.lower() in data_line.lower():
            words = data_line.split()
            target_index = 0
            for index, word in enumerate(words):
                if args.text.lower() in word.lower():
                    target_index = index
                    break
            start_index = max(2, target_index - 5)
            end_index = min(len(words), target_index + 5)
            file_dict[words[0] + ' ' + words[1]] = " ".join(words[start_index:end_index])
            lines_with_words_counter += 1
    result_dict[file] = file_dict

if not result_dict:
    print(Fore.RED + 'Совпадений не найдено')
else:
    print(Fore.RED + f'Найдено {lines_with_words_counter} совпадений в {len(result_dict)} файлах')

    for file, dictionary in result_dict.items():
        print(Fore.GREEN + f'{file}')
        for date, message in dictionary.items():
            print(Fore.BLUE + date, Fore.WHITE + message)
        print()

print(Style.RESET_ALL)
