#!/usr/bin/env python3

"""Does string search and replace on binary files, assuming 0-terminated strings
"""

# Still missing:
# - command line options
# - search only
# - treat text files differently
# - allow pattern matching for src string

import sys
from pathlib import Path


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


def binreplace_file(
    src: str, dst: str, path: Path, *, replace_all: bool = True, inplace: bool = False
) -> bool:
    """I/O and error handling wrapper for binary_replace"""
    assert len(dst) <= len(src)
    assert (src[-1] == "/") == (dst[-1] == "/")
    try:
        print("---", path)
        with path.open("rb") as binfile:
            replaced = binary_replace(binfile.read(), src.encode(), dst.encode(), replace_all)
        if replaced:
            with (path if inplace else path.parent / f"{path.name}.replaced").open("bw") as binfile:
                binfile.write(replaced)
                return True
    except PermissionError as exc:
        print(f"Could not open: {exc}", file=sys.stderr)
    return False


def binreplace(src: str, dst: str, *paths: str | Path) -> None:
    """Traverse"""
    for path in map(Path, paths):
        if path.is_dir():
            for file_path in (p for p in path.glob("**/*") if p.is_file()):
                binreplace_file(src, dst, file_path.absolute())
        else:
            binreplace_file(src, dst, path.absolute())


def main() -> None:
    """Main entry point"""
    binreplace(*sys.argv[1:])


if __name__ == "__main__":
    main()
