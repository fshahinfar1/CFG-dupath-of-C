import argparse
import traceback
import graph_gen
import os


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('cfile', type=str, help='path to c file')
    parser.add_argument('--output-type', type=str, default='pdf', help='output file type')
    args = parser.parse_args()
    return args


def main():
    args = parse()
    try:
        filename = os.path.splitext(os.path.basename(args.cfile))[0]
        graph_gen.build_graph(args.cfile, filename, args.output_type)
    except Exception:
        print('Failed!')
        traceback.print_exc()

if __name__ == '__main__':
    main()
