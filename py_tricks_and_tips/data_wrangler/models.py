import sqlalchemy as db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy_utils import generic_repr

Base = declarative_base()
metadata = Base.metadata


@generic_repr
class TRecord(Base):
    __tablename__ = "tRecord"

    ixRecord = db.Column(db.Integer, primary_key=True)
    dtTimestamp = db.Column(db.Date)
    dblAmbientTemp = db.Column(db.Float)
    dblAmbientHumidity = db.Column(db.Float)

    norm_data = relationship("TNormalizedData")


@generic_repr
class TDataLocation(Base):
    __tablename__ = "tDataLocation"

    ixDataLocation = db.Column(db.Integer, primary_key=True)
    sDataLocation = db.Column(db.Text)


@generic_repr
class TNormalizedData(Base):
    __tablename__ = "tNormalizedData"

    ixNormalizeData = db.Column(db.Integer, primary_key=True)
    ixRecord = db.Column(db.Integer, db.ForeignKey("tRecord.ixRecord"), nullable=False)
    ixDataLocation = db.Column(
        db.Integer, db.ForeignKey("tDataLocation.ixDataLocation"), nullable=False
    )

    dblPressure = db.Column(db.Float)
    dblTemperature = db.Column(db.Float)

    data_location = relationship("TDataLocation", uselist=False)
    record = relationship("TRecord", uselist=False, viewonly=True)
