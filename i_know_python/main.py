"""Test if you have as much Python experience as you think.

"""

import pkg_resources


def run():
    libraries = pkg_resources.resource_filename(__name__, 'data/library37.txt')
    used = []
    unused = []
    welcome = "Welcome to 'I know Python'!\nAnswer these questions to the best of your ability.\n"
    print(welcome)
    with open(libraries, encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if '—' in line:
                while True:
                    result = input(f"Have you used:\n\t {line}\n[y/n]? ").lower()
                    if result == 'y':
                        used.append(line)
                        break
                    elif result == 'n':
                        unused.append(line)
                        break
                    else:
                        print("Please respond with 'y' or 'n'.")
    print('='*12 + '\nUsed modules\n' + '='*12)
    for module in used:
        print(module)
    print('\n' + '='*14 + '\nUnused modules\n' + '='*14)
    for module in unused:
        print(module)
    print(f'\n# of used modules: {len(used)}\n# of unused modules: {len(unused)}')


if __name__ == '__main__':
    run()
