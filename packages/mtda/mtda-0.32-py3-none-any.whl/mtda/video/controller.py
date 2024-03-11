# ---------------------------------------------------------------------------
# Video interface for MTDA
# ---------------------------------------------------------------------------
#
# This software is a part of MTDA.
# Copyright (C) 2024 Siemens Digital Industries Software
#
# ---------------------------------------------------------------------------
# SPDX-License-Identifier: MIT
# ---------------------------------------------------------------------------

import abc


class VideoController(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def configure(self, conf):
        """ Configure this video controller from the provided
            configuration"""
        return

    @property
    def format(self):
        return None

    @abc.abstractmethod
    def probe(self):
        """ Check presence of the video controller"""
        return

    @abc.abstractmethod
    def start(self):
        """ Start video capture """
        return False

    @abc.abstractmethod
    def stop(self):
        """ Stop video capture """
        return False

    @abc.abstractmethod
    def url(self, host="", opts=None):
        """ URL for the video stream """
        return None
