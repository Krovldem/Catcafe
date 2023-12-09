from Place import Coord, Place
import pytest

def test_coord():
    coord1=Coord(row=1, column=2)
    assert(repr(coord1)=="(1, 2)")