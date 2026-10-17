from pathlib import Path
import sys

# ----------------------------------------------------
# Add the Pct root to the Python's module search path
# ------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from langchain_classic.memory import ConversationSummaryMemory

from llm_client import get_llm
from utils.helpers import print_separator, print_title

def main():
    print_title("Conversation Summary Memory")
    llm = get_llm()

    memory = ConversationSummaryMemory(
        llm = llm,
    )

    conversations = [
        ("Hi", "Hello"),
                        ("My name is Manpreet", "Nice to meet you Manpreet."),
                        ("I am learning Langchain", "Great Choice!"),
                        ("Tell me about RAG", "RAG combines retrieval with generation."),
                        ("What are AI Agents?", "AI Agents can plan, reason, and use tools."), 
    ]

    for human, ai in conversations:
        memory.save_context(
            {"input": human},
            {"output": ai},
        )

    history = memory.load_memory_variables({})

    print("Conversation Summary:\n")
    print(history["history"])

if __name__ == "__main__":
    main()        