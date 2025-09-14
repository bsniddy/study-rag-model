# Universal RAG Study Assistant

A Retrieval-Augmented Generation (RAG) system for studying any subject using your personal notes and Ollama for local LLM inference. This system combines your study materials with the LLM's pre-trained knowledge to provide comprehensive, personalized answers.

## Features

- **Document Processing**: Upload and process PDF notes (lectures, labs, homework, textbooks)
- **Hybrid Knowledge**: Uses BOTH your notes AND the LLM's general knowledge
- **Local LLM**: Runs completely on your machine using Ollama (no API costs, privacy)
- **Smart Search**: Finds relevant information from your documents
- **Interactive Chat**: Ask questions and get detailed answers
- **Source Citation**: Shows which parts of your documents were used
- **Personalized**: Tailored to your specific study materials
- **Universal**: Works with any subject - math, science, history, literature, etc.

## Quick Start

### 1. Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai) installed and running

### 2. Installation

```bash
# Clone or download this repository
cd rag-model

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r simple_requirements.txt

# Install Ollama model
ollama pull llama2
```

### 3. Add Your Notes

Place your PDF files in the project directory:
- Lecture notes
- Lab instructions
- Homework solutions
- Textbook chapters
- Any other study materials

### 4. Run the System

```bash
# Activate virtual environment
source venv/bin/activate

# Run the universal RAG system
python universal_rag.py
```

The system will ask you what subject you're studying, then process your notes and start the interactive chat.

## How It Works

### The RAG Process

1. **Document Loading**: Your PDFs are processed and split into searchable chunks
2. **Retrieval**: When you ask a question, the system finds the most relevant chunks from your notes
3. **Generation**: The LLM combines your notes with its knowledge to generate a comprehensive answer
4. **Response**: You get a personalized answer with source citations

### Hybrid Knowledge Approach

The system uses a **two-tier approach**:

1. **Your Notes First**: Prioritizes information from your specific study materials
2. **LLM Knowledge**: Supplements with general knowledge when needed
3. **Smart Combination**: Clearly indicates which source provided which information

## Example Questions by Subject

### Computer Science
- "What did I learn about algorithms in my data structures class?"
- "Explain the concepts from my operating systems notes"
- "How do the lab instructions explain recursion?"

### Mathematics
- "What are the key formulas from my calculus notes?"
- "Explain the proof techniques from my linear algebra homework"
- "How do I solve differential equations based on my notes?"

### Science
- "What are the main principles from my physics lab?"
- "Explain the chemical reactions from my chemistry notes"
- "What did I learn about cell biology in my textbook?"

### Literature/History
- "What are the main themes from my literature readings?"
- "Explain the historical events from my notes"
- "How do the authors' arguments relate to each other?"

## File Structure

```
rag-model/
├── universal_rag.py         # Main universal RAG system
├── enhanced_rag.py          # Enhanced RAG system
├── requirements.txt         # Python dependencies
├── .gitignore               # Git ignore file
├── README.md                # This documentation
├── notes/                   # Directory for your study materials (PDFs)
│   └── [your_pdf_files.pdf] # Your uploaded study materials
├── venv/                    # Python virtual environment
└── universal_vectorstore_[subject].json # Saved document database (auto-generated)
```

## Configuration

### Changing the LLM Model

Edit the model name in `universal_rag.py`:

```python
response = ollama.generate(
    model='llama2',  # Change to 'mistral', 'codellama', etc.
    prompt=prompt,
    options={'temperature': 0.7}
)
```

### Available Models

- `llama2` - Good general purpose model
- `mistral` - Fast and efficient
- `codellama` - Specialized for code and technical content
- `phi3` - Microsoft's compact model
- `gemma` - Google's efficient model

Install with: `ollama pull <model-name>`

## Supported File Types

- **PDF**: Lecture slides, scanned notes, textbooks, lab reports
- **TXT**: Text files, code, notes (if you want to add support)

## Sample Output

```
======================================================================
UNIVERSAL COMPUTER ARCHITECTURE STUDY ASSISTANT
======================================================================
This system uses BOTH your notes AND the LLM's knowledge!
Ask questions about Computer Architecture!
Type 'quit' to exit, 'help' for examples
======================================================================

Your question: What is a cache?

Thinking...

Answer:
--------------------------------------------------
A cache is a small, fast memory storage location used to store frequently accessed data or instructions in a computer system. It helps improve performance by reducing the time it takes to access data from slower main memory...

Sources from your notes (3 chunks):
  1. Section 1.1 - CS 25000_ Computer Architecture _ zyBooks.pdf (chunk 21)
  2. Section 1.1 - CS 25000_ Computer Architecture _ zyBooks.pdf (chunk 22)
  3. Section 1.1 - CS 25000_ Computer Architecture _ zyBooks.pdf (chunk 23)
```

---

*This RAG system combines the power of your personal notes with the knowledge of a large language model to create a personalized study assistant for any subject.*