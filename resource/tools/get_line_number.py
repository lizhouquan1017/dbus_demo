# -*- coding: utf-8 -*-
import os

dir_list = ['aw', 'frame', 'script', 'resource']
skip_file_list = []


def rep(project_root_path):
    tall = 0
    for item in dir_list:
        for dir_name, subdir, files in os.walk(os.path.join(project_root_path, item)):
            files.sort()
            if '__pycache__' not in dir_name:
                for file in files:
                    if file in skip_file_list:
                        continue
                    elif os.path.splitext(file)[1] != '.py':
                        continue
                    else:
                        print(os.path.join(dir_name, file))

                    with open(os.path.join(dir_name, file), 'r') as f:
                        tall += len(f.readlines())

    for dir_name, subdir, files in os.walk(project_root_path):
        for file in files:
            if file in skip_file_list:
                continue
            elif os.path.splitext(file)[1] != '.py':
                continue
            else:
                print(os.path.join(dir_name, file))

            with open(os.path.join(dir_name, file), 'r') as f:
                tall += len(f.readlines())
        break

    print(tall)


if __name__ == '__main__':
    project_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    rep(project_root_path)
