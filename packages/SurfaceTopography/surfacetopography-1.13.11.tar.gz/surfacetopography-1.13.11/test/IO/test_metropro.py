#
# Copyright 2020-2023 Lars Pastewka
#
# ### MIT license
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import os

import numpy as np
import pytest

from NuMPI import MPI

from SurfaceTopography import read_topography
from SurfaceTopography.IO import MetroProReader

pytestmark = pytest.mark.skipif(
    MPI.COMM_WORLD.Get_size() > 1,
    reason="tests only serial functionalities, please execute with pytest")


def test_read_filestream(file_format_examples):
    """
    The reader has to work when the file was already opened as binary for
    it to work in topobank.
    """
    file_path = os.path.join(file_format_examples, 'metropro-1.dat')

    read_topography(file_path)

    with open(file_path, 'r') as f:
        read_topography(f)

    # This test just needs to arrive here without raising an exception


def test_metropro_metadata(file_format_examples):
    file_path = os.path.join(file_format_examples, 'metropro-1.dat')

    r = MetroProReader(file_path)
    t = r.topography()

    nx, ny = t.nb_grid_pts
    assert nx == 480
    assert ny == 640

    sx, sy = t.physical_sizes
    np.testing.assert_allclose(sx, 0.000527160973433638, rtol=1e-6)
    np.testing.assert_allclose(sy, 0.0007028812979115173, rtol=1e-6)

    assert t.unit == 'm'

    np.testing.assert_allclose(t.rms_height_from_area(), 7.528822204734589e-08, rtol=1e-6)
    np.testing.assert_allclose(t.rms_height_from_profile(), 4.501828e-09, rtol=1e-6)

    t = t.detrend('curvature')
    np.testing.assert_allclose(t.rms_height_from_area(), 3.911386124282179e-09, rtol=1e-6)
    np.testing.assert_allclose(t.rms_height_from_profile(), 3.265267e-09, rtol=1e-6)
