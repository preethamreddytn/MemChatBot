# MemChatBot

MemChatBot is a Python chatbot with conversational memory, built with LangGraph, LangChain, Google's Gemini API, and Streamlit.

The Streamlit interface collects chat messages, while the LangGraph backend maintains conversation state and memory for a configurable thread.

## Features

- Interactive Streamlit chat interface
- Conversation history in the Streamlit session
- LangGraph state management
- In-memory checkpointing for thread-based conversations
- Google Gemini responses through LangChain

## Project Structure

```text
MemChatBot/
├── chatbot_backend.py      # LangGraph chatbot graph and Gemini model setup
├── streamlit_chatbot.py    # Streamlit user interface
└── README.md
```

## Requirements

- Python 3.10 or newer
- A Google Gemini API key

Required packages:

```text
streamlit
langgraph
langchain-core
langchain-google-genai
langchain
```

## Installation

Clone the repository:

```bash
git clone https://github.com/preethamreddytn/MemChatBot.git
cd MemChatBot
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install streamlit langgraph langchain-core langchain-google-genai langchain
```

## Configuration

Open `chatbot_backend.py` and replace `API_KEY_HERE` with your Google Gemini API key:

```python
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    api_key="YOUR_GOOGLE_GEMINI_API_KEY",
)
```

For better security, prefer an environment variable instead of hardcoding the key:

```bash
export GOOGLE_API_KEY="YOUR_GOOGLE_GEMINI_API_KEY"
```

Then update `chatbot_backend.py`:

```python
import os

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    api_key=os.getenv("GOOGLE_API_KEY"),
)
```

On Windows PowerShell:

```powershell
$env:GOOGLE_API_KEY="YOUR_GOOGLE_GEMINI_API_KEY"
```

## Run the Application

Start the Streamlit app:

```bash
streamlit run streamlit_chatbot.py
```

Open the local URL shown in your terminal, type a message into the chat input, and the chatbot will respond.

## How It Works

1. Streamlit captures a user message and stores it in `st.session_state`.
2. The message is passed to the compiled LangGraph graph.
3. The graph routes the state to the `chatbot` node.
4. The node sends the conversation messages to Google's Gemini model.
5. The response is displayed in the Streamlit chat interface.
6. `InMemorySaver` checkpoints state for the configured `thread_id`, so each conversation thread retains its memory while the process is running.

The current thread is configured in `streamlit_chatbot.py`:

```python
CONFIG = {"configurable": {"thread_id": "thread-1"}}
```

## Memory Behavior

The project uses `InMemorySaver`, so conversation memory is temporary. It is retained while the Python process is running but is lost when the app restarts.

For persistent conversations, replace `InMemorySaver` with a durable LangGraph checkpointer implementation.

## Security Note

Do not commit API keys to this repository. Use environment variables or a secrets manager, and keep the key out of source control.

## License

No license has been specified for this repository.
