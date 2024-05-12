import ormar
from typing import Optional
import config

import sqlalchemy
import databases

database = databases.Database(config.DB_URL)
metadata = sqlalchemy.MetaData()

class Task(ormar.Model):
    ormar_config = ormar.OrmarConfig(
        database=database, metadata=metadata, tablename="tasks"
    )

    id : Optional[int] = ormar.Integer(primary_key=True, autoincrement=True)
    #author: User = ormar.ForeignKey(User, related_name="author")
    name : str = ormar.String(max_length=100)
    description : str = ormar.Text()
    #executor : User = ormar.ForeignKey(User, related_name="executor")
    another : str = ormar.String(max_length=100)
