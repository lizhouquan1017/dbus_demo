# -*- coding: utf-8 -*-
import os

project_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
script_dir = os.path.join(project_root_path, 'script')


def get_case_list():
    global project_root_path
    global script_dir

    case_dict = {}
    for dirname, subdirs, files in os.walk(script_dir):

        files.sort()

        if '__pycache__' in dirname:
            continue

        if ('__pycache__' in subdirs and len(subdirs) == 1) or not subdirs:
            key = dirname.split(project_root_path)[1]
            case_dict[key] = []
            for file in files:
                if file != '__init__.py' and '.py' == os.path.splitext(file)[1]:
                    case_dict[key].append(file)
        else:
            continue

    for key in case_dict:
        print(f'{key}:  {len(case_dict[key])}')


if __name__ == "__main__":
    get_case_list()
