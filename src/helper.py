from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

#Extract data from pdf files in the directory

def load_pdf_file(data):
    loader=DirectoryLoader(data,
                           glob="**/*.pdf",
                           loader_cls=PyPDFLoader)
    documents=loader.load()
    return documents


def text_splitter(extract_data):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)
    text_chunks=text_splitter.split_documents(extract_data)
    return text_chunks


from langchain_community.embeddings import HuggingFaceEmbeddings

#download the embdddings from hugging face

def download_embeddings():
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

