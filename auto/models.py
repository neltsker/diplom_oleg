import ormar
from typing import Optional, List
import config
import pydantic
import datetime
import sqlalchemy
import databases

database = databases.Database(config.DB_URL)
metadata = sqlalchemy.MetaData()





class Detail(ormar.Model):
    ormar_config = ormar.OrmarConfig(
        database=database,
        metadata=metadata
    )
    
    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=300)
    icon: str = ormar.String(max_length=300)
    installation_datetime: datetime.datetime = pydantic.Field(
        default=datetime.datetime.now
    )
    price: int = ormar.Integer(nullable=True)

class Payment(ormar.Model):
    ormar_config = ormar.OrmarConfig(
        database=database,
        metadata=metadata
    )
    
    id: int = ormar.Integer(primary_key=True)
    price: Optional[int] = ormar.Integer()
    name: str = ormar.String(max_length=300)
    payload: pydantic.Json =  ormar.JSON()
    bill_photo: str = ormar.String(max_length=100)
    date: datetime.datetime = pydantic.Field(
        default=datetime.datetime.now
    )

class Mileage(ormar.Model):
    ormar_config = ormar.OrmarConfig(
        database=database,
        metadata=metadata
    )
    
    id: int = ormar.Integer(primary_key=True)
    mileage: int = ormar.Integer()
    data: datetime.datetime = pydantic.Field(
        default=datetime.datetime.now
    )


class Automobile(ormar.Model):
    ormar_config = ormar.OrmarConfig(
        database=database,
        metadata=metadata
    )

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)
    mark: str = ormar.String(max_length=100)
    model: str = ormar.String(max_length=100)
    mileage: Optional[Mileage] = ormar.ForeignKey(Mileage)
    mileage_history: Optional[List[Mileage]] = ormar.ManyToMany(Mileage, related_name="mileage_history")