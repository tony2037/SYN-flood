import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', '-t', required = True, help = 'Victim ip address')
    args = parser.parse_args()
    print('The victim IP: %s' % args.target)
