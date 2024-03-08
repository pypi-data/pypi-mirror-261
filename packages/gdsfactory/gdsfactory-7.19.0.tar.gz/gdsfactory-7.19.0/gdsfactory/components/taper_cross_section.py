from __future__ import annotations

from functools import partial
from itertools import islice

import gdsfactory as gf
from gdsfactory.cell import cell
from gdsfactory.component import Component
from gdsfactory.cross_section import strip_rib_tip
from gdsfactory.typings import Callable, CrossSectionSpec, Metadata


@cell
def taper_cross_section(
    cross_section1: CrossSectionSpec = strip_rib_tip,
    cross_section2: CrossSectionSpec = "xs_rc",
    length: float = 10,
    npoints: int = 100,
    linear: bool = False,
    width_type: str = "sine",
    post_process: Callable | list[Callable] | None = None,
    info: Metadata | None = None,
    **kwargs,
) -> Component:
    r"""Returns taper transition between cross_section1 and cross_section2.

    Args:
        cross_section1: start cross_section factory.
        cross_section2: end cross_section factory.
        length: transition length.
        npoints: number of points.
        linear: shape of the transition, sine when False.
        width_type: shape of the transition ONLY IF linear is False.
        post_process: optional list of functions to post process the component.
        info: additional information to add to the component.
        kwargs: cross_section settings for both cross_sections.


    .. code::

                           _____________________
                          /
                  _______/______________________
                        /
       cross_section1  |        cross_section2
                  ______\_______________________
                         \
                          \_____________________


    """
    x1 = gf.get_cross_section(cross_section1, **kwargs)
    x2 = gf.get_cross_section(cross_section2, **kwargs)
    transition = gf.path.transition(
        cross_section1=x1,
        cross_section2=x2,
        width_type="linear" if linear else width_type,
    )
    taper_path = gf.path.straight(length=length, npoints=npoints)

    c = gf.Component()
    ref = c << gf.path.extrude_transition(taper_path, transition=transition)
    c.add_ports(ref.ports)
    c.absorb(ref)

    # set one pin for each cross section
    x1.add_pins(
        c,
        select_ports=lambda ports: {(port_name := next(iter(ports))): ports[port_name]},
    )
    x2.add_pins(
        c,
        select_ports=lambda ports: {
            (port_name := next(islice(iter(ports), 1, None))): ports[port_name],
        },
    )

    if "type" in x1.info and x1.info["type"] == x2.info.get("type"):
        c.add_route_info(cross_section=x1, length=length, taper=True)

    c.post_process(post_process)
    c.info.update(info or {})

    c.info["length"] = length
    return c


taper_cross_section_linear = partial(taper_cross_section, linear=True, npoints=2)
taper_cross_section_sine = partial(taper_cross_section, linear=False, npoints=101)
taper_cross_section_parabolic = partial(
    taper_cross_section, linear=False, width_type="parabolic", npoints=101
)

taper_sc_nc_sine = partial(
    taper_cross_section,
    linear=False,
    npoints=101,
    cross_section1="xs_nc_sc_tip",
    cross_section2="xs_sc_nc_tip",
)

if __name__ == "__main__":
    # x1 = partial(strip, width=0.5)
    # x2 = partial(strip, width=2.5)
    # c = taper_cross_section_linear(x1, x2)

    # x1 = partial(strip, width=0.5)
    # x2 = partial(rib, width=2.5)
    # c = taper_cross_section_linear(x1, x2)

    # c = taper_cross_section(gf.cross_section.strip, gf.cross_section.rib)
    # c = taper_cross_section_sine()
    # c = taper_cross_section_linear()
    # print([i.name for i in c.get_dependencies()])
    # cross_section1 = gf.cross_section.rib_heater_doped(width=2)
    # cross_section2 = gf.cross_section.strip_rib_tip
    # c = taper_cross_section(cross_section1, cross_section2)
    # c = taper_sc_nc_sine(length=10)
    c = taper_cross_section_linear(length=10)
    c.show(show_ports=True)
    print(c.get_polygon_enclosure())
