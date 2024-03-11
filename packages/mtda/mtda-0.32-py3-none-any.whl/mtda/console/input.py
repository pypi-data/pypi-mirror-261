# ---------------------------------------------------------------------------
# Console input for MTDA
# ---------------------------------------------------------------------------
#
# This software is a part of MTDA.
# Copyright (C) 2021 Siemens Digital Industries Software
#
# ---------------------------------------------------------------------------
# SPDX-License-Identifier: MIT
# ---------------------------------------------------------------------------

# System imports
import atexit
import codecs
import fcntl
import termios
import sys
import tty


class ConsoleInput:

    def __init__(self):
        if sys.version_info.major >= 3 and sys.version_info.minor >= 7:
            sys.stdin.reconfigure(encoding='utf-8', errors='ignore')
        else:
            sys.stdin = codecs.getreader('utf-8')(sys.stdin.detach())
        if sys.stdin.isatty():
            self.fd = sys.stdin.fileno()
            self.old = termios.tcgetattr(self.fd)
            atexit.register(self.cleanup)

    def start(self):
        if sys.stdin.isatty():
            new = termios.tcgetattr(self.fd)
            new[3] = new[3] & ~termios.ICANON & ~termios.ECHO & ~termios.ISIG
            new[6][termios.VMIN] = 1
            new[6][termios.VTIME] = 0
            termios.tcsetattr(self.fd, termios.TCSANOW, new)
            tty.setraw(sys.stdin)

    def getkey(self):
        c = sys.stdin.read(1)
        if c == chr(0x7f):
            c = chr(8)  # map the BS key (which yields DEL) to backspace
        return c

    def cancel(self):
        if sys.stdin.isatty():
            fcntl.ioctl(self.fd, termios.TIOCSTI, b'\0')

    def cleanup(self):
        if sys.stdin.isatty():
            termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old)
