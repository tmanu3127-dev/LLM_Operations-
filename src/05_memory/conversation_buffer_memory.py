"""
File: conversation_buffer_memory.py

Description
-----------
Demonstrates ConversationBufferMemory.

ConversationBufferMemory stores the complete conversation history.
Every user message and AI response is retained and provided as context
for future interactions.
"""

# got error to erase that used special line

from pathlib import Path
import sys

# -------------------------------------------------------------------
# Add the project root to Python's module search path.
# -------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from langchain_classic.memory import ConversationBufferMemory
# updated special line:
memory = ConversationBufferMemory(return_messages=True)

from utils.helpers import print_separator, print_title


def main() -> None:
    """Demonstrates ConversationBufferMemory."""

    print_title("Conversation Buffer Memory")

    memory = ConversationBufferMemory(
        return_messages=True
    )

    # Simulate a conversation
    memory.save_context(
        {"input": "Hi! My name is Vikash."},
        {"output": "Hello Vikash! Nice to meet you."},
    )

    memory.save_context(
        {"input": "I am learning LangChain."},
        {"output": "That's great! LangChain is an excellent framework for building LLM applications."},
    )

    memory.save_context(
        {"input": "I also want to learn RAG."},
        {"output": "RAG is one of the most important concepts in modern GenAI applications."},
    )

    print("Complete Conversation History:\n")

    history = memory.load_memory_variables({})

    for index, message in enumerate(history["history"], start=1):
        print(f"Message {index}")
        print(f"Type    : {message.type}")
        print(f"Content : {message.content}")
        print_separator()


if __name__ == "__main__":
    main()


# =============================================================================
# ChatMessageHistory vs ConversationBufferMemory
#
# ChatMessageHistory:
# -------------------
# - Simply stores conversation messages (Human, AI, System, etc.).
# - Think of it as a list or notebook of chat messages.
# - You manually add, retrieve, and manage the messages.
#
# ConversationBufferMemory:
# -------------------------
# - A memory implementation built on top of ChatMessageHistory.
# - Automatically stores user inputs and AI responses.
# - Provides the complete conversation history whenever the LLM needs context.
# - Commonly used in conversational AI applications and chatbots.
#
# In short:
# ChatMessageHistory = Message Storage
# ConversationBufferMemory = Memory Manager


# from pathlib import Path
# import sys

# # ----------------------------------------
# # Add the Project root to Python's module search path
# # ----------------------------------------

# PROJECT_ROOT = Path(__file__).resolve().parents[2]

# if str(PROJECT_ROOT) not in sys.path:
#     sys.path.insert(0, str(PROJECT_ROOT))

# from langchain_classic.memory import ConversationBufferMemory

# from utils.helpers import print_separator, print_title

# def main():
#     print_title("Conversation Buffer Memory")
#     memory = ConversationBufferMemory(return_message=True)

#     memory.save_context(
#         {"input" : "Hi my name is Manpreet Singh"},
#         {"output" : "Hello Manpreet ! nice to meet you"},
#     )

#     memory.save_context(
#             {"input" : "I am learning Langchain."},
#             {"output" : "That's great! Langchain is excellent framework for building LLM applications."},
#         )

#     memory.save_context(
#             {"input" : "I also want to learn RAG."},
#             {"output" : "RAG is one of the most interesting concepts of GenAI. "},
#         )

#     print("Complete Conversation History:\n")
#     history = memory.load_memory_variables({})

     
#     for index, message in enumerate(history["history"], start=1):
#         print(f"Message    {index}")
#         print(f"Type:{message.type}")
#         print(f"Content:{message.content}")
#         print_separator()

# if __name__ == "__main__":
#     main()            

    

