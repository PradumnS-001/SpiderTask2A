import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.passthrough import RunnablePassthrough

load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ['LANGCHAIN_ENDPOINT'] = os.getenv("LANGCHAIN_ENDPOINT")
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.12,
    max_tokens = 1024)

embed = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vectorstore = Chroma(
    collection_name="EmbeddingMatrixes",
    embedding_function=embed,
    persist_directory="vdb")
retriever = vectorstore.as_retriever(search_kwargs={"k":3})

TEMPLATE = """
You are a helpful AI Assistant.
Using only the factual information form the provided context, answer the given question. If possible, elaborate on your response briefly using only the information in the context. Do not show any external knowledge, if the context lacks relevant facts, just say you can't answer.

---

Context:

{context}

---

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(TEMPLATE)
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

get_answer = lambda query : rag_chain.invoke(query)