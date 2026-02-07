# Medical Chatbot

AI chatbot that answers medical questions from PDF documents.

## Setup

```bash
git clone https://github.com/damintha01/medical_chatbot_genAI.git
cd medical_chatbot_genAI
pip install -r requirements.txt
```

Create `.env` file:
```
PINECONE_API_KEY=your_key
OPENAI_API_KEY=your_key
```

## Run

```bash
python store_index.py  # First time only
python app.py
```



## Tech Stack

Python, Flask, LangChain, Pinecone, OpenAI

## Docker

```bash
docker build -t medibot .
docker run -d -p 8080:8080 -e PINECONE_API_KEY=key -e OPENAI_API_KEY=key medibot
```

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?logo=flask)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![Pinecone](https://img.shields.io/badge/Pinecone-VectorDB-purple)
![OpenAI](https://img.shields.io/badge/OpenAI-LLM-orange?logo=openai)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20ECR-orange?logo=amazonaws)

---

## 📌 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Running Locally](#running-locally)
- [Docker Deployment](#docker-deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [Screenshots](#screenshots)
- [License](#license)

---

## Overview

MediBot is a conversational AI assistant that answers medical and health-related questions. It works by:

1. **Extracting** text from medical PDF documents
2. **Splitting** text into manageable chunks
3. **Embedding** chunks using HuggingFace `sentence-transformers/all-MiniLM-L6-v2`
4. **Storing** embeddings in a Pinecone vector database
5. **Retrieving** the most relevant chunks for a user's question
6. **Generating** concise answers using OpenAI's LLM via a RAG chain

---

## Architecture

```
User Question
      │
      ▼
┌──────────┐     ┌─────────────┐     ┌──────────┐
│  Flask    │────▶│  LangChain  │────▶│  OpenAI  │
│  Web App  │     │  RAG Chain  │     │   LLM    │
└──────────┘     └──────┬──────┘     └──────────┘
                        │
                        ▼
                 ┌─────────────┐
                 │  Pinecone   │
                 │  Vector DB  │
                 └─────────────┘
                        ▲
                        │
              ┌─────────────────┐
              │  Medical PDFs   │
              │  (Embedded via  │
              │  HuggingFace)   │
              └─────────────────┘
```

---

## Tech Stack

| Component         | Technology                                  |
| ----------------- | ------------------------------------------- |
| **LLM**           | OpenAI GPT                                  |
| **Embeddings**    | HuggingFace `all-MiniLM-L6-v2`             |
| **Vector Store**  | Pinecone                                    |
| **Framework**     | LangChain (RAG, Retrieval Chain)            |
| **Backend**       | Flask                                       |
| **Frontend**      | HTML, CSS, JavaScript (jQuery)              |
| **Containerization** | Docker                                   |
| **CI/CD**         | GitHub Actions                              |
| **Cloud**         | AWS (EC2, ECR)                              |

---

## Project Structure

```
medical_chatbot_genAI/
├── .github/
│   └── workflows/
│       └── cicd.yaml            # GitHub Actions CI/CD pipeline
├── Data/                        # Medical PDF documents
├── research/
│   └── trials.ipynb             # Jupyter notebook for experimentation
├── src/
│   ├── __init__.py
│   ├── helper.py                # PDF loader, text splitter, embeddings
│   └── prompts.py               # System prompt for RAG chain
├── static/
│   └── style.css                # Stylesheet
├── templates/
│   └── chat.html                # Chat UI frontend
├── app.py                       # Main Flask application
├── store_index.py               # Script to index PDFs into Pinecone
├── setup.py                     # Package setup
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker configuration
├── .env                         # Environment variables (not committed)
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- [Pinecone](https://www.pinecone.io/) account & API key
- [OpenAI](https://platform.openai.com/) API key
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/medical_chatbot_genAI.git
   cd medical_chatbot_genAI
   ```

2. **Create and activate a virtual environment**
   ```bash
   conda create -p venv python=3.10 -y
   conda activate venv/
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** — Create a `.env` file in the root directory:
   ```env
   PINECONE_API_KEY=your_pinecone_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Add your medical PDFs** — Place your PDF documents in the `Data/` directory.

6. **Index documents into Pinecone**
   ```bash
   python store_index.py
   ```

---

## Environment Variables

| Variable            | Description                        |
| ------------------- | ---------------------------------- |
| `PINECONE_API_KEY`  | API key for Pinecone vector store  |
| `OPENAI_API_KEY`    | API key for OpenAI                 |

---

## Running Locally

```bash
python app.py
```

The app will be available at **http://localhost:8080**

---

## Docker Deployment

### Build the Docker image

```bash
docker build -t medibot .
```

### Run the container

```bash
docker run -d \
  -p 8080:8080 \
  -e PINECONE_API_KEY=your_pinecone_api_key \
  -e OPENAI_API_KEY=your_openai_api_key \
  medibot
```

Visit **http://localhost:8080** to access the chatbot.

---

## CI/CD Pipeline

The project includes a fully automated CI/CD pipeline using **GitHub Actions**:

### Workflow: `.github/workflows/cicd.yaml`

| Stage                     | Description                                         |
| ------------------------- | --------------------------------------------------- |
| **Continuous Integration** | Builds & pushes Docker image to AWS ECR             |
| **Continuous Deployment**  | Pulls image on EC2 (self-hosted runner) & runs it   |

### Required GitHub Secrets

| Secret                   | Description                              |
| ------------------------ | ---------------------------------------- |
| `AWS_ACCESS_KEY_ID`      | AWS IAM access key                       |
| `AWS_SECRET_ACCESS_KEY`  | AWS IAM secret key                       |
| `AWS_REGION`             | AWS region (e.g., `us-east-1`)           |
| `AWS_ACCOUNT_ID`         | AWS account ID                           |
| `ECR_REPOSITORY`         | ECR repository name                      |
| `PINECONE_API_KEY`       | Pinecone API key                         |
| `OPENAI_API_KEY`         | OpenAI API key                           |

---

## Screenshots

### Chat Interface
> _A professional, modern chat UI with real-time responses._

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---
