import os
from dotenv import load_dotenv
load_dotenv()
from psychicapi import Psychic, ConnectorId
from langchain.schema import Document
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain

try:
    psychic = Psychic(secret_key=os.getenv("PSYCHIC_SECRET_KEY"))
    #replace connector_id and account_id with the ones you used when creating a new connection at https://dashboard.psychic.dev/playground
    psychic_docs = psychic.get_documents(connector_id=ConnectorId.confluence, account_id="account_id", chunked=True)
    docs = [
        Document(page_content=doc["content"], metadata={"title": doc["title"], "source": doc["uri"]})
        for doc in psychic_docs
    ]

    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vdb = Chroma.from_documents(docs, embeddings)
    while True:
        question = input("✨ Ask a question: ")
        chain = RetrievalQAWithSourcesChain.from_chain_type(OpenAI(temperature=0), chain_type="stuff", retriever=vdb.as_retriever())
        answer = chain({"question": question}, return_only_outputs=True)
        print(answer)
        print("")
except Exception as e:
    print(e)
