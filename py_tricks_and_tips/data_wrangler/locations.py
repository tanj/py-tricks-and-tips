from enum import IntEnum
import attr

from .models import TDataLocation


class ELoc(IntEnum):
    Mixer = 1
    Extruder = 2
    ChilledWaterInlet = 3
    ChilledWaterOutlet = 4


@attr.s
class NormColNames:
    pres = attr.ib()
    temp = attr.ib()


data_locations = [
    TDataLocation(
        # The plain SqlAlchemy Integer doesn't know how converter an
        # IntEnum type so we explicitly need the ELoc.Mixer.value
        ixDataLocation=ELoc.Mixer.value,
        sDataLocation="Mixer",
    ),
    TDataLocation(ixDataLocation=ELoc.Extruder.value, sDataLocation="Extruder"),
    TDataLocation(
        ixDataLocation=ELoc.ChilledWaterInlet.value, sDataLocation="Chilled Water Inlet"
    ),
    TDataLocation(
        ixDataLocation=ELoc.ChilledWaterOutlet.value,
        sDataLocation="Chilled Water Outlet",
    ),
]

map_column_names = {
    # key: value
    ELoc.Mixer: NormColNames("Mixer Pressure", "Mixer Temperature"),
    ELoc.Extruder: NormColNames("Extruder Pressure", "Extruder Temperature"),
    ELoc.ChilledWaterInlet: NormColNames(
        "Chilled Water Inlet Pressure", "Chilled Water Inlet Temperature"
    ),
    ELoc.ChilledWaterOutlet: NormColNames(
        "Chilled Water Outlet Pressure", "Chilled Water Outlet Temperature"
    ),
}
