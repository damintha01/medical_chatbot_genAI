from pinecone import ServerlessSpec
from pinecone.grpc import PineconeGRPC as pinecone
import os
from dotenv import load_dotenv
load_dotenv()
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
from src.helper import load_pdf_file,text_splitter,download_embeddings

os.environ["PINECONE_API_KEY"]=PINECONE_API_KEY
OpenAI_API_KEY=os.environ.get("OPENAI_API_KEY")


extract_data=load_pdf_file("Data/")
text_chunks=text_splitter(extract_data)
embeddings=download_embeddings()


pc=pinecone(api_key=PINECONE_API_KEY)

index_name="medicalbot"

# Check if index exists before creating
if index_name not in pc.list_indexes().names():
    pc.create_index(name=index_name,
                    dimension=384,
                    metric="cosine",
                    spec=ServerlessSpec(cloud="aws",
                                        region="us-east-1"))
    print(f"Index '{index_name}' created. Waiting for it to be ready...")
    
    # Wait for the index to be ready
    import time
    while not pc.describe_index(index_name).status['ready']:
        time.sleep(1)
    print(f"Index '{index_name}' is now ready!")
else:
    print(f"Index '{index_name}' already exists")



from langchain_pinecone import PineconeVectorStore

docsearch=PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)