import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="mode", required=True)
    parser.add_argument("-v", "--verbose", action="store_true")
    generate_mode = subparsers.add_parser("generate")
    generate_mode.add_argument("-m", "--model", choices=["aig", "mig", "xaig", "xmig"], required=True)
    generate_mode.add_argument("-n", "--variables", type=int, required=True)
    group = generate_mode.add_mutually_exclusive_group(required=True)
    group.add_argument("-c", "--complexity", type=int)
    group.add_argument("-d", "--depth", type=int)
    check_mode = subparsers.add_parser("check")
    check_mode.add_argument("-a", "--algorithm", choices=["simple", "full"], default="simple")
    check_mode.add_argument("circuits", nargs="+")
    return parser.parse_args()


if __name__ == "__main__":
    exec(sys.stdin.read())
