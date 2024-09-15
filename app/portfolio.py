import pandas as pd
import chromadb
import uuid
import streamlit as st

class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            st.write("Loading portfolio into ChromaDB...")
            for _, row in self.data.iterrows():
                st.write(f"Adding Techstack: {row['Techstack']}, Links: {row['Links']}")
                self.collection.add(
                    documents=row["Techstack"],
                    metadatas={"links": row["Links"]},
                    ids=[str(uuid.uuid4())]
                )
            #st.write("Portfolio loaded successfully!")
        else:
            #st.write(f"Portfolio already loaded with {self.collection.count()} items.")
            st.write("Your mail is ready...")

    def query_links(self, skills):
        # Ensure skills is a list and not empty
        if not skills:
            st.error("No skills provided for query.")
            return []
        if isinstance(skills, str):
            skills = [skills]  # Convert to list if it's a string

        # Debug: check the skills and portfolio size before querying
        st.write(f"Querying skills: {skills}")
        #st.write(f"Number of documents in the collection: {self.collection.count()}")

        try:
            # Perform the query
            result = self.collection.query(query_texts=skills, n_results=2)
            #st.write(f"Query result: {result}")
            return result.get('metadatas', [])
        except Exception as e:
            st.error(f"Error during query: {e}")
            return []
