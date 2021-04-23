import argparse
from pathlib import Path

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

import pyexcel

from py_tricks_and_tips.data_wrangler.models import (
    metadata,
    TDataLocation,
    TRecord,
    TNormalizedData,
)
from py_tricks_and_tips.data_wrangler.locations import (
    data_locations,
    map_column_names,
)


def valid_file(arg):
    parg = Path(arg)
    if parg.is_file():
        if parg.suffix.lower() in [".csv", ".xls", ".xlsx"]:
            return arg
    raise argparse.ArgumentTypeError(f"{arg!r} is not a valid file")


def make_database(engine="sqlite", filename="extruder.db"):
    if engine != "sqlite":
        raise Exception(f"Engine {engine} Not Implemented")
    eng = create_engine(f"{engine}:///{filename}")
    metadata.create_all(bind=eng)
    return eng


def populate_known_data(session):
    (count_loc,) = session.query(func.count(TDataLocation.ixDataLocation)).one()
    if count_loc == 0:
        session.add_all(data_locations)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def process_extruder(session, extruder_file):
    sheet = pyexcel.get_sheet(file_name=extruder_file, name_columns_by_row=0)
    colnames = sheet.colnames
    for row in sheet:
        record = TRecord(
            dtTimestamp=row[colnames.index("Timestamp")],
            dblAmbientTemp=row[colnames.index("Ambient Temperature")],
            dblAmbientHumidity=row[colnames.index("Humidity")],
        )
        for key, value in map_column_names.items():
            record.norm_data.append(
                TNormalizedData(
                    ixDataLocation=key.value,
                    dblPressure=row[colnames.index(value.pres)],
                    dblTemperature=row[colnames.index(value.temp)],
                ),
            )
        session.add(record)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def get_session(engine):
    eng = create_engine(engine)
    DBSession = sessionmaker(bind=eng)
    return DBSession()


def main():
    parser = argparse.ArgumentParser(description="Convert Extruder Data to SQL")
    parser.add_argument(
        "EXTRUDER_FILE", type=valid_file, help="Extruder File [*.csv, *.xls, *.xlsx]"
    )
    parser.add_argument("--dblocation", help="path to sqlite file")

    args = parser.parse_args()

    dbfile = "extruder.db"
    if args.dblocation:
        dbfile = args.dblocation
    engine = make_database(filename=dbfile)
    DBSession = sessionmaker(bind=engine)
    Session = DBSession()
    populate_known_data(Session)
    process_extruder(Session, args.EXTRUDER_FILE)
    return


# Normally you wouldn't leave something like this here, but I want to
# use this interactively.
session = get_session("sqlite:///extruder.db")

if __name__ == "__main__":
    main()
