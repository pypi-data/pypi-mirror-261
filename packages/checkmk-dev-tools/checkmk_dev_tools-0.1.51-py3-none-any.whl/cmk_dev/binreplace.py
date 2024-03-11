#!/usr/bin/env python3

"""Does string search and replace on binary files, assuming 0-terminated strings
"""

# Still missing:
# - treat text files differently
# - allow pattern matching for src string

import sys
from argparse import ArgumentParser
from pathlib import Path


def apply_cli_arguments(parser: ArgumentParser) -> None:
    """Adds binreplace CLI arguments to @parser (for reusability)"""
    parser.add_argument("--dry-run", "-d", action="store_true")
    parser.add_argument("--inplace", "-p", action="store_true")
    parser.add_argument("--stop-after-first", action="store_true")
    parser.add_argument("source", type=str)
    parser.add_argument("destination", type=str)
    parser.add_argument("target", type=Path, nargs="+")


def binary_replace(buffer: bytes, src: bytes, dst: bytes, replace_all: bool) -> None | bytes:
    """Searches @buffer for @src and replaces it with @dst, keeping the same length and
    taking null termination into account
    >>> sequence_in = b"replace: ABCDdef\\x00but not this"
    >>> sequence_out = binary_replace(sequence_in, b"ABCD", b"abc", True)
    >>> print(sequence_out)
    b'replace: abcdef\\x00\\x00but not this'
    >>> assert len(sequence_in) == len(sequence_out)
    """
    start_pos = 0
    something_replaced = None
    while (pos := buffer[start_pos:].find(src)) != -1:
        abs_start = start_pos + pos
        nul_pos = buffer[abs_start:].find(b"\0")
        if 0 < nul_pos < 1000:
            nul_padding = b"\0" * (len(src) - len(dst))
            replaced = dst + buffer[abs_start + len(src) : abs_start + nul_pos] + nul_padding
            buffer = buffer[:abs_start] + replaced + buffer[abs_start + nul_pos :]
            something_replaced = buffer
        start_pos = abs_start + 1

        if not replace_all:
            break
    return something_replaced


def binreplace_file(  # pylint: disable=too-many-arguments
    src: str,
    dst: str,
    path: Path,
    *,
    replace_all: bool = True,
    inplace: bool = False,
    dry_run: bool = False,
) -> bool:
    """I/O and error handling wrapper for binary_replace"""
    assert len(dst) <= len(src)
    assert (src[-1] == "/") == (dst[-1] == "/")
    try:
        with path.open("rb") as binfile:
            replaced = binary_replace(binfile.read(), src.encode(), dst.encode(), replace_all)
        if replaced:
            print(path)
            if dry_run:
                print("found search string but skip writing due to dry run", file=sys.stderr)
                return False
            with (path if inplace else path.parent / f"{path.name}.replaced").open("bw") as binfile:
                binfile.write(replaced)
                return True
    except PermissionError as exc:
        print(f"Could not open: {exc}", file=sys.stderr)
    return False


def binreplace(
    src: str,
    dst: str,
    *paths: str | Path,
    replace_all: bool = True,
    inplace: bool = False,
    dry_run: bool = False,
) -> None:
    """Traverse"""
    for path in map(Path, paths):
        if path.is_dir():
            for file_path in (p for p in path.glob("**/*") if p.is_file()):
                binreplace_file(
                    src,
                    dst,
                    file_path.absolute(),
                    replace_all=replace_all,
                    inplace=inplace,
                    dry_run=dry_run,
                )
        else:
            binreplace_file(
                src, dst, path.absolute(), replace_all=replace_all, inplace=inplace, dry_run=dry_run
            )


def main() -> None:
    """Main entry point"""
    parser = ArgumentParser()
    apply_cli_arguments(parser)
    args = parser.parse_args()
    binreplace(
        args.source,
        args.destination,
        *args.target,
        replace_all=not args.stop_after_first,
        inplace=args.inplace,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
