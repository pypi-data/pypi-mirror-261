# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2021-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import re
import typing as t

import click
import pytermor as pt

from es7s.shared import FrozenStyle, get_logger, get_stdout
from es7s.shared.demo import get_demo_highlight_num_text
from ._base import _BaseAction


class WhitespaceBytesSquasher(pt.IFilter[bytes, bytes]):
    def __init__(self):
        super().__init__()
        self._pattern = re.compile(br"\s+")
        self._repl = lambda m: b"."*len(m.group())

    def _apply(self, inp: bytes, extra: t.Any = None) -> bytes:
        return self._pattern.sub(self._repl, inp)


class action(_BaseAction):
    CHUNK_SIZE = 1024

    RAW_FILTERS = [
        pt.OmniSanitizer(b"."),
        WhitespaceBytesSquasher(),
    ]

    def __init__(self, file: click.File | None, demo: bool, *args, **kwargs):
        self._line_num = 1
        self._offset = 0
        self._input: t.TextIO

        if demo:
            file = get_demo_highlight_num_text().open('rt')
        elif file is None:
            file = click.open_file("-", "r")
            get_stdout().echo('> ', nl=False)

        try:
            self._assign_input(file)
            self._run(demo)
        finally:
            if not file.closed:
                file.close()

    def _run(self, demo: bool):
        if demo:
            self._run_demo()
        self._read_and_process_input()
        self._close_input()

    def _run_demo(self):
        headers = [pt.Text(s, FrozenStyle(bold=True)) for s in ["Input:", "Output:"]]
        get_stdout().echo_rendered(headers.pop(0))
        self._read_and_process_input(remove_sgr=True)
        self._reset_input()
        get_stdout().echo_rendered(headers.pop(0))

    def _read_and_process_input(self, remove_sgr: bool = False):
        logger = get_logger()
        try:
            while line := self._input.readline(self.CHUNK_SIZE):
                processed_line = self._process_decoded_line(line)
                if remove_sgr:
                    processed_line = pt.SgrStringReplacer("").apply(processed_line)
                get_stdout().echo(processed_line)
            return
        except UnicodeDecodeError as e:
            logger.error(str(e))
            logger.warning("Switching to raw output")

        self._reset_input(self._offset)
        newline = logger.setup.stderr_allowed_debug
        try:
            while chunk := self._input.buffer.read(self.CHUNK_SIZE):
                get_stdout().echo(self._process_raw_chunk(chunk), nl=newline)
        except Exception as e:
            logger.error(str(e))

    def _process_decoded_line(self, line: str | None) -> str:
        if line is None:
            return ""
        get_logger().debug(f"(#{self._line_num}) Read line:\n"+line)
        line_len = len(line.encode())
        result = pt.highlight(line.strip("\n"))

        get_logger().debug(f"(#{self._line_num}) Processed {line_len} bytes, offset {self._offset}")
        self._line_num += 1
        self._offset += line_len
        return get_stdout().render(result)

    def _process_raw_chunk(self, chunk: bytes|None) -> str:
        if chunk is None:
            return ""
        logger = get_logger()
        logger.debug(pt.dump(chunk, pt.BytesTracer, pt.TracerExtra(f"(#{self._line_num}) Read chunk")))
        line_len = len(chunk)
        result = pt.apply_filters(chunk, *self.RAW_FILTERS)

        logger.debug(f"(#{self._line_num}) Processed {line_len} bytes, offset {self._offset}")
        self._line_num += 1
        self._offset += line_len
        return result

    def _assign_input(self, inp: t.TextIO | t.IO):
        self._input = inp
        get_logger().info(f"Current input stream is {self._input.__class__}")

    def _close_input(self):
        if not self._input.closed:
            get_logger().info(f"Closing input stream {self._input.__class__}")
            self._input.close()

    def _reset_input(self, offset: int = 0):
        if self._input.seekable():
            get_logger().info(f"Resetting input stream position to {offset}")
            self._input.seek(offset)
