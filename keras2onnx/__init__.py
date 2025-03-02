###############################################################################
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
###############################################################################
"""
keras2onnx
This package converts keras models into ONNX for use with any inference engine supporting ONNX
"""
__version__ = "1.5.0"
__author__ = "Microsoft Corporation"
__producer__ = "keras2onnx"

__producer_version__ = __version__
__domain__ = "onnx"
__model_version__ = 0

try:
    import sys
    import os.path
    from os.path import dirname, abspath
    import tensorflow
    sys.path.insert(0, os.path.join(dirname(abspath(__file__)), 'ktf2onnx'))
except ImportError:
    raise AssertionError('Please conda install / pip install tensorflow or tensorflow-gpu before the model conversion.')



from .common import Variable, cvtfunc, set_logger_level
from .funcbook import set_converter

from .main import convert_keras


def tfname_to_onnx(name): return Variable.tfname_to_onnx(name)


