"""Test the slope functions."""

# The MIT License (MIT)
#
# Copyright (c) 2019 Institute for Molecular Systems Biology, ETH Zurich.
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
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import pandas as pd
import pytest

from optslope import calculate_slope, calculate_slope_multi, create_extended_core_model


def test_deltarpi_slopes():
    """Test the delta-RPI slopes."""
    model = create_extended_core_model(
        ["EDD", "EDA", "RBC", "PRK"], ["dhap", "xu5p__D"]
    )

    s1 = calculate_slope(model, ("RPI", "EDD", "EDA"), ("dhap",), "RBC")
    assert s1 == pytest.approx(2.156, rel=1e-3)

    s2 = calculate_slope(model, ("RPI", "EDD", "EDA"), ("xu5p__D",), "RBC")
    assert s2 == pytest.approx(15.923, rel=1e-3)


def test_deltarpi_slopes_multi():
    """Test the delta-RPI slopes in multi mode."""
    model = create_extended_core_model(
        ["EDD", "EDA", "RBC", "PRK"], ["dhap", "xu5p__D"]
    )
    single_kos = ["RPI", "EDD|EDA", "ENO", "TPI", "RPE"]

    result_df = calculate_slope_multi(
        model, ("dhap",), single_kos, "RBC", max_knockouts=3, num_processes=4
    )

    assert pd.isnull(result_df[result_df.knockouts == ("EDD|EDA", "ENO")].slope).all()

    assert result_df.slope.max() == pytest.approx(26.41, rel=1e-3)
