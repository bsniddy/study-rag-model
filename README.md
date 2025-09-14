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

## Example

======================================================================
UNIVERSAL COMPUTER ARCHITECTURE STUDY ASSISTANT
======================================================================
This system uses BOTH your notes AND the LLM's knowledge!
Ask questions about Computer Architecture!
Type 'quit' to exit, 'help' for examples
======================================================================

Your question: What is a multiplexor

Thinking...

Answer:
--------------------------------------------------
Based on the context provided by the student's notes, a multiplexor is an electronic circuit that selects one of several input signals and sends it to a output. In the context of computer architecture, a multiplexor is used in an adder to give the option of selecting either the original binary number or its inverted value, depending on the Binvert signal. The figure provided in the notes shows how this works.

However, there are some additional details and concepts that can help expand on this answer. A multiplexor is essentially a simple electronic switch that selects one of several inputs based on a control signal. In the context of computer architecture, multiplexors are used to implement various logical operations, such as AND, OR, and NOT.

In addition to the information provided in the notes, there are a few key concepts related to multiplexors that can help deepen understanding:

1. Multiplexors can be used to implement binary arithmetic operators, such as addition and subtraction. By using a multiplexor to select either the original binary number or its inverted value, these operations can be performed in a simple and efficient manner.
2. The use of multiplexors in computer architecture is based on the principle of two's complement representation, which is a way of representing integers in binary form. In this system, each bit of an integer is represented by a power of 2 (i.e., 0, 1, 2, 4, 8, etc.), and the most significant bit (MSB) represents the sign of the number. By inverting the MSB and adding 1, the two's complement representation can be obtained.
3. The simplicity of the hardware design of a two's complement adder helps explain why two's complement representation has become the universal standard for integer computer arithmetic. This is because the use of two's complement representation allows for easy implementation of addition and subtraction operations using simple electronic circuits, such as multiplexors.
4. In addition to their use in adders, multiplexors can also be used in other logical circuits, such as decoders and encoders. These circuits are used to implement various logical operations, such as encoding binary data for storage or decoding it for retrieval.

In summary, a multiplexor is an electronic circuit that selects one of several input signals and sends it to a output. In computer architecture, multiplexors are used to implement binary arithmetic operators, such as addition and subtraction, using the principle of two's complement representation. By understanding how multiplexors work and their role in computer architecture, programmers can optimize the performance of their programs and improve their overall efficiency.

Sources from your notes (3 chunks):
  1. Section 7.5 - CS 25000_ Computer Architecture _ zyBooks.pdf (chunk 7)
  2. Section 1.1 - CS 25000_ Computer Architecture _ zyBooks.pdf (chunk 21)
  3. Section 1.1 - CS 25000_ Computer Architecture _ zyBooks.pdf (chunk 22)

---

*This RAG system combines the power of your personal notes with the knowledge of a large language model to create a personalized study assistant for any subject.*