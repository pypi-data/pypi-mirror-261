"""FabC example."""

from __future__ import annotations

import sys
from functools import partial

from pydantic import BaseModel

import gdsfactory as gf
from gdsfactory.add_pins import add_pins_inside1nm
from gdsfactory.cross_section import get_cross_sections, strip
from gdsfactory.port import select_ports
from gdsfactory.technology import LayerLevel, LayerStack
from gdsfactory.typings import Layer


class LayerMap(BaseModel):
    WG: Layer = (10, 1)
    WG_CLAD: Layer = (10, 2)
    WGN: Layer = (34, 0)
    WGN_CLAD: Layer = (36, 0)
    PIN: Layer = (1, 10)


LAYER = LayerMap()
WIDTH_NITRIDE_OBAND = 0.9
WIDTH_NITRIDE_CBAND = 1.0

select_ports_optical = partial(select_ports, layers_excluded=((100, 0),))


def get_layer_stack_fab_c(thickness: float = 350.0) -> LayerStack:
    """Returns generic LayerStack."""
    return LayerStack(
        layers=dict(
            wg=LayerLevel(
                layer=(1, 0),
                zmin=0.0,
                thickness=0.22,
            ),
            wgn=LayerLevel(
                layer=LAYER.WGN,
                zmin=0.22 + 0.1,
                thickness=0.4,
            ),
        )
    )


add_pins = partial(add_pins_inside1nm, pin_length=0.5)

# cross_sections

strip_nc = partial(
    strip,
    width=WIDTH_NITRIDE_CBAND,
    layer=LAYER.WGN,
    bbox_layers=[LAYER.WGN_CLAD],
    bbox_offsets=[3],
    add_pins_function_name="add_pins",
    add_pins_function_module="gdsfactory.samples.pdk.fab_c",
)
strip_no = partial(
    strip_nc,
    width=WIDTH_NITRIDE_OBAND,
)

xs_nc = strip_nc()
xs_no = strip_no()

# LEAF COMPONENTS have pins
bend_euler_nc = partial(
    gf.components.bend_euler, cross_section=xs_nc, post_process=[add_pins]
)
straight_nc = partial(
    gf.components.straight, cross_section=xs_nc, post_process=[add_pins]
)
bend_euler_o = partial(
    gf.components.bend_euler, cross_section=xs_no, post_process=[add_pins]
)
straight_o = partial(
    gf.components.straight, cross_section=xs_no, post_process=[add_pins]
)


mmi1x2_nc = partial(
    gf.components.mmi1x2,
    width=WIDTH_NITRIDE_CBAND,
    width_mmi=3,
    cross_section=xs_nc,
    post_process=[add_pins],
)
mmi1x2_no = partial(
    gf.components.mmi1x2,
    width=WIDTH_NITRIDE_OBAND,
    cross_section=xs_no,
    post_process=[add_pins],
)

gc_nc = partial(
    gf.components.grating_coupler_elliptical,
    grating_line_width=0.6,
    layer_slab=None,
    cross_section=xs_nc,
    post_process=[add_pins],
)

# HIERARCHICAL COMPONENTS made of leaf components

mzi_nc = partial(
    gf.components.mzi,
    cross_section=xs_nc,
    splitter=mmi1x2_nc,
    straight=straight_nc,
    bend=bend_euler_nc,
)
mzi_no = partial(
    gf.components.mzi,
    cross_section=xs_no,
    splitter=mmi1x2_no,
    straight=straight_o,
    bend=bend_euler_o,
)


cells = dict(
    mmi1x2_nc=mmi1x2_nc,
    mmi1x2_no=mmi1x2_no,
    bend_euler_nc=bend_euler_nc,
    straight_nc=straight_nc,
    mzi_nc=mzi_nc,
    mzi_no=mzi_no,
    gc_nc=gc_nc,
)


layer_stack = get_layer_stack_fab_c()
cross_sections = get_cross_sections(sys.modules[__name__])

pdk = gf.Pdk(
    name="fab_c_demopdk",
    cells=cells,
    cross_sections=cross_sections,
    layer_stack=layer_stack,
)


if __name__ == "__main__":
    # c2 = mmi1x2_nc()
    # d2 = c2.to_dict()

    # from jsondiff import diff

    # d = diff(d1, d2)
    # c.show(show_ports=True)

    c = mzi_nc()
    c.show()
