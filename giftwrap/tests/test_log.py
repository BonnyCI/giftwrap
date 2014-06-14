# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2014, John Dewey
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import unittest2 as unittest
from nose.plugins.logcapture import LogCapture

from giftwrap import log


class TestLog(unittest.TestCase):
    def test_get_logger(self):
        lc = LogCapture()
        lc.begin()
        logger = log.get_logger()
        logger.debug('testing')
        lc.end()

        self.assertEquals("unknown: DEBUG: testing", lc.handler.buffer[0])