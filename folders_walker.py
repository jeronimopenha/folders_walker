import argparse
import os
import sys

p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not p in sys.path:
    sys.path.insert(0, p)


def folders_walker(path: str):
    content = []
    for actual_dir, dir_in_actual_dir, arch_in_actual_dir in os.walk(path):
        content.append([actual_dir, dir_in_actual_dir, arch_in_actual_dir])
    return content



def create_args():
    parser = argparse.ArgumentParser('folders_walker -h')
    parser.add_argument('-p', '--path', help='Initial folder for the folders walker can walks.', type=str)

    return parser.parse_args()


if __name__ == '__main__':
    args = create_args()
    running_path = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    root = os.getcwd()

    if args.path:
        content = folders_walker(args.path)
        for adir, dir, arch in content:
            print("Actual directory: ", adir)
            print("Directories in actual directory: ", dir)
            print("Archives in actual diredtory: ", arch)
            print()
    else:
        msg = 'Missing parameters. Run folders_walker -h to see all parameters needed'
        raise Exception(msg)
