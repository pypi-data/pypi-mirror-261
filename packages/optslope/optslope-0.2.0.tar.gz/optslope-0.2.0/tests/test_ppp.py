"""Test the phenotypic phase plane functions."""

# The MIT License (MIT)
#
# Copyright (c) 2018 Institute for Molecular Systems Biology, ETH Zurich.
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

import pytest

from optslope import create_extended_core_model, production_envelope


def test_wildtype_acetate_production_envelope():
    """Test the WT acetate production envelope."""
    wt_model = create_extended_core_model()

    grid = production_envelope(
        wt_model, knockouts=[], carbon_sources=["glc__D"], target_reaction="EX_ac_e"
    )

    assert (grid["flux_minimum"] == 0.0).all()
    assert grid.at[0, "flux_maximum"] == pytest.approx(31.98, rel=1e-3)
    assert grid.EX_ac_e.max() == pytest.approx(666.66, rel=1e-3)


def test_deltatpi_acetate_production_envelope():
    """Test the delta-RPI acetate production envelope."""
    wt_model = create_extended_core_model()

    grid = production_envelope(
        wt_model,
        knockouts=["TPI"],
        carbon_sources=["glc__D"],
        target_reaction="EX_ac_e",
    )

    assert (grid["flux_minimum"] == 0.0).all()
    assert grid.at[0, "flux_maximum"] == pytest.approx(12.79, rel=1e-3)
    assert grid.EX_ac_e.max() == pytest.approx(142.85, rel=1e-3)
