#!/usr/bin/env python3
#-------------------------------------------------------------------------------
# Extract YAML frontmatter from a text file
#-------------------------------------------------------------------------------

def main():
    import argparse
    import sys

    try:
        parser = argparse.ArgumentParser(description='Extract YAML frontmatter from a text file')
        parser.add_argument('filename', help='File to extract from.')

        args = parser.parse_args()

    except Exception as ex:
        print(f'Error: {ex}')
        sys.exit(1)

    output = []
    try:
        with open(args.filename) as f:
            line = f.readline()[:-1]
            assert line == '---', 'First line was expected to be `---`, stopped parsing.'

            finished = False
            while not finished:
                line = f.readline()[:-1]

                if not line or line == '---':
                    finished = True
                else:
                    output.append(line)

    except Exception as ex:
        print(f'Error: {ex}')
        sys.exit(1)

    for l in output:
        print(l)

if __name__ == '__main__':
    main()
