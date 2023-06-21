# -*- coding: utf-8 -*-
#
# escpos/exceptions.py
#
# Copyright 2015 Base4 Sistemas Ltda ME
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals


class TimeoutException(Exception):
    pass


class CashDrawerException(Exception):
    pass


class NonWritableSocketError(Exception):
    pass


class NonReadableSocketError(Exception):
    pass

class Error(Exception):
    """Base class for ESC/POS errors"""

    def __init__(self, msg, status=None):
        Exception.__init__(self)
        self.msg = msg
        self.resultcode = 1
        if status is not None:
            self.resultcode = status

    def __str__(self):
        return self.msg


class BarcodeTypeError(Error):
    """No Barcode type defined.

    This exception indicates that no known barcode-type has been entered. The barcode-type has to be
    one of those specified in :py:meth:`escpos.escpos.Escpos.barcode`.
    The returned error code is `10`.
    """

    def __init__(self, msg=""):
        Error.__init__(self, msg)
        self.msg = msg
        self.resultcode = 10

    def __str__(self):
        return "No Barcode type is defined ({msg})".format(msg=self.msg)


class BarcodeSizeError(Error):
    """Barcode size is out of range.

    This exception indicates that the values for the barcode size are out of range.
    The size of the barcode has to be in the range that is specified in :py:meth:`escpos.escpos.Escpos.barcode`.
    The resulting returncode is `20`.
    """

    def __init__(self, msg=""):
        Error.__init__(self, msg)
        self.msg = msg
        self.resultcode = 20

    def __str__(self):
        return "Barcode size is out of range ({msg})".format(msg=self.msg)


class BarcodeCodeError(Error):
    """No Barcode code was supplied, or it is incorrect.

    No data for the barcode has been supplied in :py:meth:`escpos.escpos.Escpos.barcode` or the the `check` parameter
    was True and the check failed.
    The returncode for this exception is `30`.
    """

    def __init__(self, msg=""):
        Error.__init__(self, msg)
        self.msg = msg
        self.resultcode = 30

    def __str__(self):
        return "No Barcode code was supplied ({msg})".format(msg=self.msg)