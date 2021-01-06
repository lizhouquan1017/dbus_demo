# -*- coding:utf-8 -*-
import os
import time

import openpyxl


def get_mark(script_root_path):
    sp2_list = []
    sp3_list = []
    for dir_name, subdir, files in os.walk(script_root_path):
        files.sort()
        if '__pycache__' not in dir_name:
            for file in files:
                with open(os.path.join(dir_name, file), 'r') as f:
                    content_list = f.readlines()

                for line in content_list:
                    if '@pytest.mark.sp2' in line:
                        sp2_list.append(os.path.join(dir_name, file))

                    elif '@pytest.mark.sp3' in line:
                        sp3_list.append(os.path.join(dir_name, file))
    import pprint
    print(f"{'=' * 50}")
    print(len(sp2_list))
    pprint.pprint(sp2_list)
    print(f"{'=' * 50}")
    pprint.pprint(sp3_list)
    print(len(sp3_list))
    print(f"{'=' * 50}")


if __name__ == '__main__':
    project_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    script_root_path = os.path.join(project_root_path, 'script')
    get_mark(script_root_path)
