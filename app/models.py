from sqlalchemy import Column, Integer, String
from app.database import Base


class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    filename = Column(String)


class QuestionHistory(Base):
    __tablename__ = "question_history"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    question = Column(String)
    answer = Column(String)