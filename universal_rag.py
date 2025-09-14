#!/usr/bin/env python3
"""
Universal RAG system that works with any subject
"""

import os
import sys
import json
from pathlib import Path
import PyPDF2 as pypdf2
import ollama
import re

class UniversalRAG:
    def __init__(self, subject="your subject"):
        print(f"Initializing Universal RAG System for {subject}...")
        print("This system uses BOTH your notes AND the LLM's knowledge!")
        
        # Initialize Ollama
        print("Connecting to Ollama...")
        try:
            ollama.list()
            print("Connected to Ollama")
        except Exception as e:
            print(f"Error connecting to Ollama: {e}")
            print("Please make sure Ollama is running: ollama serve")
            sys.exit(1)
        
        self.documents = []
        self.subject = subject
        self.vectorstore_file = f"universal_vectorstore_{subject.replace(' ', '_').lower()}.json"
        
    def load_documents(self, directory_path):
        """Load all PDF documents from a directory"""
        print(f"Loading documents from {directory_path}...")
        
        documents = []
        pdf_files = list(Path(directory_path).glob("*.pdf"))
        
        if not pdf_files:
            print("No PDF files found in the directory")
            return []
        
        print(f"Found {len(pdf_files)} PDF files:")
        for pdf_file in pdf_files:
            print(f"  - {pdf_file.name}")
        
        for pdf_file in pdf_files:
            try:
                print(f"Processing {pdf_file.name}...")
                text = self.extract_text_from_pdf(str(pdf_file))
                chunks = self.split_text_into_chunks(text, chunk_size=1000, overlap=200)
                
                for i, chunk in enumerate(chunks):
                    documents.append({
                        'text': chunk,
                        'source': pdf_file.name,
                        'chunk_id': i
                    })
                
                print(f"  Created {len(chunks)} chunks")
            except Exception as e:
                print(f"  Error loading {pdf_file.name}: {e}")
        
        self.documents = documents
        print(f"Total: {len(documents)} text chunks created")
        return documents
    
    def extract_text_from_pdf(self, pdf_path):
        """Extract text from PDF file"""
        text = ""
        with open(pdf_path, 'rb') as file:
            pdf_reader = pypdf2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text
    
    def split_text_into_chunks(self, text, chunk_size=1000, overlap=200):
        """Split text into overlapping chunks"""
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            
            if end < len(text):
                last_period = chunk.rfind('.')
                if last_period > chunk_size * 0.7:
                    chunk = chunk[:last_period + 1]
                    end = start + last_period + 1
            
            chunks.append(chunk.strip())
            start = end - overlap
            
        return [chunk for chunk in chunks if chunk.strip()]
    
    def simple_search(self, query, top_k=3):
        """Simple keyword-based search"""
        if not self.documents:
            return []
        
        query_words = set(query.lower().split())
        results = []
        
        for doc in self.documents:
            doc_words = set(doc['text'].lower().split())
            overlap = len(query_words.intersection(doc_words))
            if overlap > 0:
                results.append({
                    'document': doc,
                    'score': overlap
                })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]
    
    def save_vectorstore(self):
        """Save vectorstore to file"""
        data = {'documents': self.documents}
        with open(self.vectorstore_file, 'w') as f:
            json.dump(data, f)
    
    def load_vectorstore(self):
        """Load vectorstore from file"""
        if os.path.exists(self.vectorstore_file):
            print("Loading existing vector database...")
            with open(self.vectorstore_file, 'r') as f:
                data = json.load(f)
            self.documents = data['documents']
            print("Loaded existing vector database!")
            return True
        return False
    
    def query(self, question):
        """Enhanced query that uses both notes and LLM knowledge"""
        if not self.documents:
            return "Please load documents first!", []
        
        # Search for relevant documents
        search_results = self.simple_search(question, top_k=3)
        
        # Prepare context from your notes
        notes_context = ""
        sources = []
        if search_results:
            notes_context = "\n\n".join([result['document']['text'] for result in search_results])
            sources = [result['document'] for result in search_results]
        
        # Create enhanced prompt that uses both notes and LLM knowledge
        if notes_context:
            prompt = f"""You are a helpful tutor for {self.subject}. Answer the question using BOTH the provided context from the student's notes AND your own knowledge about {self.subject}.

CONTEXT FROM STUDENT'S NOTES:
{notes_context}

QUESTION: {question}

INSTRUCTIONS:
1. First, try to answer using the context from the student's notes
2. If the notes don't contain enough information, supplement with your own knowledge
3. Clearly indicate when you're using information from the student's notes vs. your general knowledge
4. Provide a comprehensive, helpful answer that combines both sources
5. If the student's notes have specific details or examples, prioritize those
6. Use your knowledge to explain concepts that might not be fully covered in the notes

Please provide a clear, comprehensive answer:"""
        else:
            # If no relevant notes found, use only LLM knowledge
            prompt = f"""You are a helpful tutor for {self.subject}. Answer the question using your knowledge about {self.subject}.

QUESTION: {question}

Please provide a clear, comprehensive answer about {self.subject} concepts:"""
        
        try:
            response = ollama.generate(
                model='llama2',
                prompt=prompt,
                options={'temperature': 0.7}
            )
            
            answer = response['response']
            return answer, sources
            
        except Exception as e:
            return f"Error querying Ollama: {str(e)}", []
    
    def interactive_mode(self):
        """Start interactive question-answering mode"""
        print("\n" + "="*70)
        print(f"UNIVERSAL {self.subject.upper()} STUDY ASSISTANT")
        print("="*70)
        print("This system uses BOTH your notes AND the LLM's knowledge!")
        print(f"Ask questions about {self.subject}!")
        print("Type 'quit' to exit, 'help' for examples")
        print("="*70)
        
        while True:
            try:
                question = input("\nYour question: ").strip()
                
                if question.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break
                
                if question.lower() == 'help':
                    self.show_help()
                    continue
                
                if not question:
                    continue
                
                print("\nThinking...")
                answer, sources = self.query(question)
                
                print(f"\nAnswer:")
                print("-" * 50)
                print(answer)
                
                if sources:
                    print(f"\nSources from your notes ({len(sources)} chunks):")
                    for i, source in enumerate(sources, 1):
                        print(f"  {i}. {source['source']} (chunk {source['chunk_id']})")
                else:
                    print("\nAnswer based on LLM's general knowledge (no relevant notes found)")
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def show_help(self):
        """Show example questions"""
        examples = [
            f"What are the main concepts in {self.subject}?",
            f"Explain the key principles from my {self.subject} notes",
            f"What did I learn about [specific topic] in {self.subject}?",
            f"How do the concepts in {self.subject} relate to each other?",
            f"What are the important formulas/theorems in {self.subject}?",
            f"Can you explain [difficult concept] from {self.subject}?",
            f"What are the practical applications of {self.subject}?",
            f"How does [concept A] differ from [concept B] in {self.subject}?",
            f"What should I focus on for my {self.subject} exam?",
            f"Can you summarize the main points from my {self.subject} readings?"
        ]
        
        print("\nExample questions you can ask:")
        print("-" * 50)
        for i, example in enumerate(examples, 1):
            print(f"  {i}. {example}")

def main():
    # Get subject from user or use default
    print("Welcome to the Universal RAG Study Assistant!")
    print("This system can help you study any subject using your notes and AI knowledge.")
    print()
    
    subject = input("What subject are you studying? (e.g., 'Computer Architecture', 'Calculus', 'Biology'): ").strip()
    if not subject:
        subject = "your subject"
    
    rag = UniversalRAG(subject)
    
    # Check if vector database already exists
    if not rag.load_vectorstore():
        print(f"\nNo existing knowledge base found for {subject}.")
        print(f"Let's create one from your {subject} notes!")
        
        # Load documents from notes directory
        notes_dir = "notes"
        documents = rag.load_documents(notes_dir)
        
        if not documents:
            print("No documents found. Please make sure PDF files are in the 'notes/' directory.")
            return
        
        # Save vectorstore
        rag.save_vectorstore()
    
    # Start interactive mode
    rag.interactive_mode()

if __name__ == "__main__":
    main()
