# Copyright (c) 2023 Christophe Dufaza <chris@openmarl.org>
#
# SPDX-License-Identifier: Apache-2.0

"""Snippets about devicetree.edtlib."""

# Relax pylint a bit for unit tests.
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=pointless-statement


import pytest

from devicetree import edtlib

from .dtsh_uthelpers import DTShTests


def test_edtlib_props() -> None:
    model: edtlib.EDT = DTShTests.get_sample_edt()

    dt_soc = model.get_node("/soc")
    dt_soc_compat = dt_soc.props["compatible"]
    assert dt_soc_compat

    print(f"Property: {dt_soc_compat.name}")
    print(f"Path: {dt_soc_compat.spec.path}")
    print(f"Desc: {dt_soc_compat.spec.description}")

    dt_i2c = model.get_node("/soc/i2c@40003000")
    dt_i2c_compat = dt_i2c.props["compatible"]
    assert dt_i2c_compat

    print(f"Property: {dt_i2c_compat.name}")
    print(f"Path: {dt_i2c_compat.spec.path}")
    print(f"Desc: {dt_i2c_compat.spec.description}")

    # Would fail.
    # assert dt_soc_compat.spec.path == dt_i2c_compat.spec.path
    # assert dt_soc_compat.spec.description == dt_i2c_compat.spec.description


def test_compound_property() -> None:
    model: edtlib.EDT = DTShTests.get_sample_edt()

    # edtlib.Property:
    # Properties of type 'compound' currently do not get Property instances,
    # as it's not clear what to generate for them.

    # dts/bindings/gpio/gpio-nexus.yaml:
    # property "gpio-map-pass-thru" of type "compound"
    #
    # zephyr.dts:
    # gpio-map-pass-thru = < 0x0 0x3f >;
    dt_connector = model.get_node("/connector")
    with pytest.raises(KeyError):
        dt_connector.props["gpio-map-pass-thru"]

    compound_props = []
    for node in model.nodes:
        for prop in node.props.values():
            if prop.type == "compound":
                compound_props.append(prop)

    # Would fail: assert not compound_props
    # The "/soc" node has a "ranges" property,
    # of type "compound", with None value.
    assert 1 == len(compound_props)
    prop = compound_props[0]
    print(prop)
    assert "ranges" == prop.name
    assert prop.spec
    assert not prop.spec.path


def test_phandle_array_property() -> None:
    model: edtlib.EDT = DTShTests.get_sample_edt()

    props = []
    for node in model.nodes:
        for prop in node.props.values():
            if prop.type == "phandle-array":
                props.append(prop)

    print()
    for prop in props:
        print(f"{prop.name}: {str(prop.val)}")
        print()


def test_phandle_property() -> None:
    model: edtlib.EDT = DTShTests.get_sample_edt()

    props = []
    for node in model.nodes:
        for prop in node.props.values():
            if prop.type == "phandle":
                props.append(prop)

    print()
    for prop in props:
        print(f"{prop.name}: {str(prop.val)}")
        print()
