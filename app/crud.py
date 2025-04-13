import datetime
from sqlalchemy.orm import Session
from app import models, schemas
from typing import List, Optional


def create_device(db, device):
    db_device = models.Device(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device


def create_measure(db, measure, device_id):
    db_measure = models.Measure(**measure.dict(), device_id=device_id)
    db.add(db_measure)
    db.commit()
    db.refresh(db_measure)
    return db_measure


def get_device(db, device_id):
    return db.query(models.Device).filter(models.Device.id == device_id).first()


def get_measures(db, device_id, start_time=None, end_time=None):
    query = db.query(models.Measure).filter(models.Measure.device_id == device_id)
    if start_time:
        query = query.filter(models.Measure.time_stamp >= start_time)
    if end_time:
        query = query.filter(models.Measure.time_stamp <= end_time)
    return query.all()