from fastapi import FastAPI, UploadFile, File
from app.database import Base, engine, SessionLocal
from app.models import UploadedFile, QuestionHistory
from app.rag import process_pdf, ask_question
import os

app = FastAPI()

Base.metadata.create_all(bind=engine)

UPLOAD_DIR = "app/upload"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

db_vector_list = {}


@app.get("/")
def root():
    return {"message": "RAG multi pdf system"}


@app.post("/upload")
async def upload_pdf(username: str, file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    db = SessionLocal()

    new_file = UploadedFile(
        username=username,
        filename=file.filename
    )

    db.add(new_file)
    db.commit()

    vector_db = process_pdf(file_path)

    db_vector_list[file.filename] = vector_db

    db.close()

    return {"message": f"{file.filename} 업로드 완료"}

#질문
@app.get("/ask")
def ask(username: str, filename: str, query: str):
    db = SessionLocal()

    if filename not in db_vector_list:
        return {"error": "파일 없음"}

    answer = ask_question(db_vector_list[filename], query)

    history = QuestionHistory(
        username=username,
        question=query,
        answer=answer
    )

    db.add(history)
    db.commit()
    db.close()

    return {"answer": answer}