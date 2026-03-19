# PDF RAG Chatbot

## 프로젝트 소개

PDF 문서를 업로드한 뒤 질문하면 관련 내용을 검색하여 답변하는 Retrieval-Augmented Generation 시스템입니다.

## 주요 기능

- PDF 업로드
- 문서 chunking
- embedding 생성
- vector DB 저장 (FAISS)
- retrieval 기반 질문 응답

## 기술 스택

- Python
- FastAPI
- LangChain
- FAISS
- Ollama / OpenAI

## 시스템 구조

1. PDF 업로드
2. 텍스트 분할
3. embedding 생성
4. vector 저장
5. 질문 시 유사 문서 검색
6. LLM 응답 생성

## 구현 포인트

- chunk size 조절을 통한 retrieval 정확도 개선
- context 최소화로 응답 효율 최적화

## 실행 방법

```bash
uvicorn app.main:app --reload
```
