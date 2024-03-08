from __future__ import annotations

from functools import lru_cache, partial

import jax
import jax.numpy as jnp
import sax
from gplugins.sax.models import bend, coupler, grating_coupler, straight

nm = 1e-3

################
# PassThrus
################


@lru_cache(maxsize=None)
def _2port(p1, p2):
    @jax.jit
    def _2port(wl=1.5):
        wl = jnp.asarray(wl)
        return sax.reciprocal({(p1, p2): jnp.ones_like(wl)})

    return _2port


@lru_cache(maxsize=None)
def _3port(p1, p2, p3):
    @jax.jit
    def _3port(wl=1.5):
        wl = jnp.asarray(wl)
        thru = jnp.ones_like(wl) / jnp.sqrt(2)
        return sax.reciprocal(
            {
                (p1, p2): thru,
                (p1, p3): thru,
            }
        )

    return _3port


@lru_cache(maxsize=None)
def _4port(p1, p2, p3, p4):
    @jax.jit
    def _4port(wl=1.5):
        wl = jnp.asarray(wl)
        thru = jnp.ones_like(wl) / jnp.sqrt(2)
        cross = 1j * thru
        return sax.reciprocal(
            {
                (p1, p4): thru,
                (p2, p3): thru,
                (p1, p3): cross,
                (p2, p4): cross,
            }
        )

    return _4port


################
# Waveguides
################

straight_sc = partial(straight, wl0=1.55, neff=2.4, ng=4.2)
straight_so = partial(straight, wl0=1.31, neff=2.4, ng=4.2)
straight_rc = partial(straight, wl0=1.55, neff=2.4, ng=4.2)
straight_ro = partial(straight, wl0=1.31, neff=2.4, ng=4.2)
straight_nc = partial(straight, wl0=1.55, neff=2.4, ng=4.2)
straight_no = partial(straight, wl0=1.31, neff=2.4, ng=4.2)

bend_sc = partial(bend, loss=0.03)
bend_so = partial(bend, loss=0.03)
bend_rc = partial(bend, loss=0.03)
bend_ro = partial(bend, loss=0.03)
bend_nc = partial(bend, loss=0.03)
bend_no = partial(bend, loss=0.03)

################
# Transitions
################

trans_sc_rc10 = _2port("o1", "o2")
trans_sc_rc20 = _2port("o1", "o2")
trans_sc_rc50 = _2port("o1", "o2")

################
# MMIs
################

mmi1x2_rc = coupler
mmi2x2_rc = coupler
mmi1x2_sc = coupler
mmi2x2_sc = coupler
mmi1x2_ro = coupler
mmi2x2_ro = coupler
mmi1x2_so = coupler
mmi2x2_so = coupler
mmi1x2_no = coupler
mmi2x2_no = coupler
mmi1x2_nc = coupler
mmi2x2_nc = coupler

##############################
# grating couplers Rectangular
##############################

_gco = partial(grating_coupler, loss=6, bandwidth=35 * nm, wl0=1.31)
_gcc = partial(grating_coupler, loss=6, bandwidth=35 * nm, wl0=1.55)
gc_rectangular_so = _gco
gc_rectangular_ro = _gco
gc_rectangular_no = _gco
gc_rectangular_sc = _gcc
gc_rectangular_rc = _gcc
gc_rectangular_nc = _gcc


################
# Crossings
################
@jax.jit
def _crossing(wl=1.5):
    wl = jnp.asarray(wl)
    one = jnp.ones_like(wl)
    return sax.reciprocal(
        {
            ("o1", "o3"): one,
            ("o2", "o4"): one,
        }
    )


crossing_so = _crossing
crossing_rc = _crossing
crossing_sc = _crossing


################
# Dummies
################
pad = _2port("o1", "o2")  # dummy model
heater = _2port("o1", "o2")  # dummy model

models = dict(
    _2port=_2port("o1", "o2"),
    _3port=_3port("o1", "o2", "o3"),
    _4port=_4port("o1", "o2", "o3", "o4"),
    straight_sc=straight_sc,
    straight_so=straight_so,
    straight_rc=straight_rc,
    straight_ro=straight_ro,
    straight_nc=straight_nc,
    straight_no=straight_no,
    bend_sc=bend_sc,
    bend_so=bend_so,
    bend_rc=bend_rc,
    bend_ro=bend_ro,
    bend_nc=bend_nc,
    bend_no=bend_no,
    trans_sc_rc10=trans_sc_rc10,
    trans_sc_rc20=trans_sc_rc20,
    trans_sc_rc50=trans_sc_rc50,
    mmi1x2_rc=mmi1x2_rc,
    mmi2x2_rc=mmi2x2_rc,
    mmi1x2_sc=mmi1x2_sc,
    mmi2x2_sc=mmi2x2_sc,
    mmi1x2_ro=mmi1x2_ro,
    mmi2x2_ro=mmi2x2_ro,
    mmi1x2_so=mmi1x2_so,
    mmi2x2_so=mmi2x2_so,
    mmi1x2_no=mmi1x2_no,
    mmi2x2_no=mmi2x2_no,
    mmi1x2_nc=mmi1x2_nc,
    mmi2x2_nc=mmi2x2_nc,
    gc_rectangular_so=gc_rectangular_so,
    gc_rectangular_ro=gc_rectangular_ro,
    gc_rectangular_no=gc_rectangular_no,
    gc_rectangular_sc=gc_rectangular_sc,
    gc_rectangular_rc=gc_rectangular_rc,
    gc_rectangular_nc=gc_rectangular_nc,
    crossing_so=crossing_so,
    crossing_rc=crossing_rc,
    crossing_sc=crossing_sc,
    pad=pad,
    heater=heater,
)


if __name__ == "__main__":
    print(coupler())
