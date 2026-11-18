#!/usr/bin/env python3
"""Entry program: copy the bundled front-page image to /output/entry.png.

Standard library only. No network, no clock, no randomness, so two runs
write identical bytes.
"""
import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_BYTES = 1 << 20  # competition limit: image at most 1 MiB


def main():
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit(f"error: missing {src}")
    size = os.path.getsize(src)
    if size == 0 or size > MAX_BYTES:
        raise SystemExit(f"error: entry.png is {size} bytes, limit is {MAX_BYTES}")
    with open(src, "rb") as fh:
        head = fh.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
        raise SystemExit("error: entry.png is not a PNG file")
    width, height = struct.unpack(">II", head[16:24])
    if (width, height) != (1024, 1024):
        raise SystemExit(f"error: entry.png is {width}x{height}, expected 1024x1024")
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, "entry.png")
    shutil.copyfile(src, dst)
    with open(src, "rb") as fh:
        src_hash = hashlib.sha256(fh.read()).hexdigest()
    with open(dst, "rb") as fh:
        dst_hash = hashlib.sha256(fh.read()).hexdigest()
    if src_hash != dst_hash:
        raise SystemExit("error: copied bytes differ from source")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
