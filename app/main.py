from fastapi import FastAPI, UploadFile, File
from app.database import Base, engine, SessionLocal
from app.models import UploadedFile
from app.rag import process_pdf, ask_question
import os

app = FastAPI()

Base.metadata.create_all(bind=engine)

db_vector = None

UPLOAD_DIR = "app/upload"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


@app.get("/")
def root():
    return {"message": "RAG server running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global db_vector

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    db = SessionLocal()

    new_file = UploadedFile(filename=file.filename)
    db.add(new_file)
    db.commit()
    db.close()

    db_vector = process_pdf(file_path)

    return {"message": "PDF 업로드 완료"}


@app.get("/ask")
def ask(query: str):
    global db_vector

    if db_vector is None:
        return {"error": "먼저 PDF 업로드 필요"}

    answer = ask_question(db_vector, query)

    return {"answer": answer}