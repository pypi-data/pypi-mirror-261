# ---------------------------------------------------------------------------
# ustreamer driver for MTDA
# ---------------------------------------------------------------------------
#
# This software is a part of MTDA.
# Copyright (C) 2024 Siemens AG
#
# ---------------------------------------------------------------------------
# SPDX-License-Identifier: MIT
# ---------------------------------------------------------------------------

# System imports
import os
import socket
import threading
import signal
import subprocess

# Local imports
from mtda.video.controller import VideoController
from mtda.utils import SystemdDeviceUnit


class UStreamerVideoController(VideoController):

    def __init__(self, mtda):
        self.dev = "/dev/video0"
        self.executable = "ustreamer"
        self.lock = threading.Lock()
        self.mtda = mtda
        self.worker = None
        self.ustreamer = None
        self.port = 8080
        self.desired_fps = 30
        self.resolution = "1280x780"
        self.www = None

    def configure(self, conf):
        self.mtda.debug(3, "video.ustreamer.configure()")

        if 'device' in conf:
            self.dev = conf['device']
            self.mtda.debug(4, 'video.ustreamer.'
                               f'configure(): will use {str(self.dev)}')
        if 'executable' in conf:
            self.executable = conf['executable']
        if 'port' in conf:
            self.port = conf['port']
        if 'resolution' in conf:
            self.resolution = conf['resolution']
        if 'www' in conf:
            self.www = conf['www']

    def configure_systemd(self, dir):
        dropin = os.path.join(dir, 'auto-dep-video.conf')
        SystemdDeviceUnit.create_device_dependency(dropin, self.dev)

    @property
    def format(self):
        return "MJPG"

    def probe(self):
        self.mtda.debug(3, 'video.ustreamer.probe()')

        if self.executable is None:
            raise ValueError('ustreamer executable not specified!')

        result = True
        try:
            subprocess.check_call([self.executable, '--version'])
        except subprocess.SubprocessError as e:
            self.mtda.debug(1, 'error calling %s: %s', self.executable, str(e))
            result = False

        self.mtda.debug(3, f'video.ustreamer.probe(): {str(result)}')
        return result

    def start(self):
        self.mtda.debug(3, 'video.ustreamer.start()')

        options = [
            '-d', self.dev, '-r', self.resolution,
            '-s', '0.0.0.0',
            '-p', str(self.port),
            '--drop-same-frames', '30',
            '-c', 'HW',    # do not transcode frames (if supported)
            '-f', str(self.desired_fps),
            '--slowdown',  # capture with 1 fps when no client
            ]
        if self.www:
            options += ['--static', self.www]

        with self.lock:
            self.ustreamer = subprocess.Popen([self.executable] + options)

        return True

    def stop(self):
        self.mtda.debug(3, 'video.ustreamer.stop()')

        with self.lock:
            if self.ustreamer.poll() is None:
                self.ustreamer.send_signal(signal.SIGINT)
            try:
                self.ustreamer.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.mtda.debug(2, 'video.ustreamer.stop: '
                                   'process did not finish, killing')
                self.ustreamer.kill()

        return True

    def url(self, host="", opts=None):
        self.mtda.debug(3, f"video.ustreamer.url(host='{str(host)}')")

        if host is None or host == "":
            host = socket.getfqdn()
            self.mtda.debug(3, "video.ustreamer."
                               f"url: using host='{str(host)}'")
        result = f"http://{host}:{self.port}/?action=stream"

        self.mtda.debug(3, f'video.ustreamer.url(): {str(result)}')
        return result


def instantiate(mtda):
    return UStreamerVideoController(mtda)
