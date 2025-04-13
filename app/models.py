from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime


class Device(Base):
    __tablename__ = "device"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)

    measures = relationship("Measure", back_populates="device")


class Measure(Base):
    __tablename__ = "measure"

    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
    time_stamp = Column(DateTime, default=datetime.utcnow)
    device_id = Column(Integer, ForeignKey("device.id"))
    device = relationship("Device", back_populates="measures")
