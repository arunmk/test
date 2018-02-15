# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
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
# ==============================================================================
"""Tests for VGG16 application."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.python.keras._impl import keras
from tensorflow.python.platform import test


class VGG16Test(test.TestCase):

  def test_with_top(self):
    model = keras.applications.VGG16(weights=None)
    self.assertEqual(model.output_shape, (None, 1000))

  def test_no_top(self):
    model = keras.applications.VGG16(weights=None, include_top=False)
    self.assertEqual(model.output_shape, (None, None, None, 512))

  def test_with_pooling(self):
    model = keras.applications.VGG16(weights=None,
                                     include_top=False,
                                     pooling='avg')
    self.assertEqual(model.output_shape, (None, 512))

  def test_weight_loading(self):
    with self.assertRaises(ValueError):
      keras.applications.VGG16(weights='unknown',
                               include_top=False)
    with self.assertRaises(ValueError):
      keras.applications.VGG16(weights='imagenet',
                               classes=2000)

if __name__ == '__main__':
  test.main()
