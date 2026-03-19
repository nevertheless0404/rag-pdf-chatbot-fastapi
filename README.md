# PDF RAG Chatbot with FastAPI

## 프로젝트 소개

PDF 문서를 업로드한 뒤 질문하면 관련 내용을 검색하여 답변하는 Retrieval-Augmented Generation 기반 질의응답 시스템입니다.

## 주요 기능

- PDF 업로드 API
- 문서 chunking
- embedding 생성
- FAISS vector store 저장
- 파일별 질의응답
- 질문 히스토리 저장
- 사용자별 문서 관리

## 기술 스택

- Python
- FastAPI
- LangChain
- FAISS
- SQLite
- Ollama (llama3)

## 시스템 구조

1. 사용자 PDF 업로드
2. 문서 텍스트 분할
3. embedding 생성
4. vector store 저장
5. 질문 입력
6. 유사 문서 retrieval
7. LLM 응답 생성
8. 질문/답변 DB 저장성

## 구현 포인트

- chunk size 조절을 통한 retrieval 정확도 개선
- context 최소화로 응답 효율 최적화

## 실행 방법

```bash
uvicorn app.main:app --reload
```

2. Ollama 실행
   ollama run llama3

3. 서버 실행
   uvicorn app.main:app --reload
   Swagger 테스트
   http://127.0.0.1:8000/docs

POST /upload

질문하기

GET /ask

## 구현 포인트

- 다중 PDF 업로드 대응 구조 설계
- 파일별 vector store 관리
- 질문 히스토리 DB 저장

## 향후 개선

- 파일 목록 조회 API
- 질문 기록 조회 API
- 사용자 인증 고도화
