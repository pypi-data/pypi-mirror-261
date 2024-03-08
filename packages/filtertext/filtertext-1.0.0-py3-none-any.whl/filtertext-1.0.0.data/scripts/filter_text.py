#!python

"""Filter text and save result to file or print to output!
If no output file or output directory is specified, filter_text.py will output to console"""

import sys
import os
import shutil
import argparse
from pathlib import Path

from filtertext import RemoveDuplicatedLinesTextFilter
from filtertext import RemoveWhitespaceLinesTextFilter

def config_arg_parser():
    arg_parser = argparse.ArgumentParser(
        prog=Path(__file__).name, formatter_class=argparse.RawDescriptionHelpFormatter,
            description=__doc__,
        epilog='<> with ♥ by Micha Grandel <hello@michagrandel.de> (Apache 2.0 License)')
    filter_group = arg_parser.add_argument_group('Filter')
    filter_group.add_argument('-w', action='store_true', help='Remove lines that only contain whitespace')
    filter_group.add_argument('-d', action='store_true', help='Remove duplicate lines')
    
    input_group = arg_parser.add_argument_group('Input')
    input_group.add_argument('file', metavar="FILE", nargs='+', help='files to filter')
    input_group.add_argument('-l', metavar="LIST_FILE", help='Input file with list of files to filter, one file per line')
    
    output_group = arg_parser.add_argument_group('Output')
    output_group.add_argument('-D', metavar="OUTPUT_PATH", help='Output directory (if it exists, it will be deleted first)')
    output_group.add_argument('-o', metavar="OUTPUT_FILE", help='Output file path (if it exists, it will be deleted first)')
    return arg_parser


def main(application, args):
    os.chdir(Path(__file__).parent)

    arg_parser = config_arg_parser()
    parsed = arg_parser.parse_args(args)

    files = parsed.file

    if parsed.o and parsed.D:
        sys.exit("{}: error: Either specify an output file or an output direction, not both!".format(Path(__file__).name))

    filters = []
    if parsed.w:
        filters.append(RemoveWhitespaceLinesTextFilter)
    if parsed.d:
        filters.append(RemoveDuplicatedLinesTextFilter)

    if parsed.l:
        with open(parsed.l, "r") as list_file:
            files.extend(list_file.readlines())

    if parsed.o:
        Path.unlink(parsed.o, missing_ok=False)
    if parsed.D:
        shutil.rmtree(parsed.D, ignore_errors=True)

    _output_to_console = False
    for file_path in files: 
        file_path = Path(file_path)
        if not file_path.is_file:
            continue

        data = file_path
        for filter in filters:
            filter = filter()
            filter.filter(data)
            data = filter.text
    
        if parsed.o:
            with open(parsed.o, "a") as file:
                file.write(data+('' if parsed.w else '\n'))
        elif parsed.D:
            file_path = Path(parsed.D) / file_path.name
            with open(file_path, "a") as file:
                file.write(data+('' if parsed.w else '\n'))
        else:
            _output_to_console = True
    if _output_to_console:
        print(data)

if __name__ == "__main__":
    main(sys.argv[0], sys.argv[1:])
