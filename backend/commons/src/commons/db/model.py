from pydantic import BaseModel
from sqlalchemy import Column, String, DateTime, TEXT


class User(BaseModel):
    __tablename__ = "User"
    ID = Column(String(37))
    FIRST_NAME = Column(String(37))
    LAST_NAME = Column(String(37))
    EMAIL = Column(String(100))


class Document(BaseModel):
    __tablename__ = "Document"
    ID = Column(String(37))
    NAME = Column(String(250))
    DOC_TEXT = Column(TEXT)
    CREATED_TS = Column(DateTime(timezone=True))
    MODIFIED_TS = Column(DateTime(timezone=True))


class TASK(BaseModel):
    __tablename__ = "Task"
    ID = Column(String(37))
    DOC_ID = Column(str(37))
    RESULT = Column(TEXT)
    CREATED_TS = Column(DateTime(timezone=True))
    MODIFIED_TS = Column(DateTime(timezone=True))


if __name__ == '__main__':
    print(f'Creating the database...')
    pass
