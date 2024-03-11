# ---------------------------------------------------------------------------
# usbrelay power driver for MTDA
# ---------------------------------------------------------------------------
#
# This software is a part of MTDA.
# Copyright (C) 2024 Siemens Digital Industries Software
#
# ---------------------------------------------------------------------------
# SPDX-License-Identifier: MIT
# ---------------------------------------------------------------------------

# System imports
import os
import re
import time
import subprocess

# Local imports
from mtda.power.controller import PowerController
import mtda.constants as CONSTS


class UsbRelayPowerController(PowerController):

    def __init__(self, mtda):
        self.dev = None
        self.exe = "/usr/bin/usbrelay"
        self.mtda = mtda
        self.lines = []

    def configure(self, conf):
        if 'lines' in conf:
            self.lines = conf['lines'].split(',')

    def probe(self):
        if self.lines is None:
            raise ValueError("usbrelay: 'lines' not configured!")

        if os.path.exists(self.exe) is False:
            raise ValueError(f"{self.exe} was not found!")

        # Make sure all configured lines were detected
        statuses = self._get_lines()
        for line in self.lines:
            if line not in statuses:
                raise ValueError(f"usbrelay: {line} not detected!")

    def command(self, args):
        return False

    def on(self):
        if self._set_lines("1") is False:
            return False
        return self._poll_status_until(self.POWER_ON)

    def off(self):
        if self._set_lines("0") is False:
            return False
        return self._poll_status_until(self.POWER_OFF)

    def status(self):
        statuses = self._get_lines()
        first = True
        result = self.POWER_UNSURE
        for line in self.lines:
            value = statuses[line]
            if value == '1':
                value = self.POWER_ON
            else:
                value = self.POWER_OFF
            self.mtda.debug(3, "power.usbrelay."
                               f"status: line {line} is {value}")
            if first is True:
                first = False
                result = value
            elif value != result:
                result = self.POWER_UNSURE
        return result

    def _poll_status_until(self, desired_state):
        for i in range(0, CONSTS.RPC.TIMEOUT // 2 + 1):
            if self.status() == desired_state:
                return True
            time.sleep(0.5)
        return False

    def _get_lines(self):
        result = {}
        try:
            lines = subprocess.check_output(
                    [self.exe]).decode("utf-8").splitlines()
            for line in lines:
                m = re.match(r"(\w+)=([01])", line)
                if m is not None:
                    name = m[1]
                    value = m[2]
                    result[name] = value
        except subprocess.CalledProcessError:
            result = None

        return result

    def _set_lines(self, value):
        try:
            for line in self.lines:
                subprocess.check_call(
                        [self.exe, f"{line}={value}"])
        except subprocess.CalledProcessError:
            return False
        return True


def instantiate(mtda):
    return UsbRelayPowerController(mtda)
