from pathlib import Path
import sys

# -------------------------------------------------
# Add the Project root to Python's module search path
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage

from utils.helpers import print_separator, print_title

def main():
    print_title("Chat Message History")
    chat_history = InMemoryChatMessageHistory()

    chat_history.add_message(
        HumanMessage(content= "What is Langchain")
    )

    chat_history.add_message(
        AIMessage(content= "Lnagchain is a framework for building LLM-powered applications.")
    )

    chat_history.add_message(
        HumanMessage(content= "What are Prompt Templates")
    )

    chat_history.add_message(
        AIMessage(content= "A prompt template is a reusable, pre-structured blueprint for interacting with Large Language Models (LLMs)"\
        " that uses dynamic placeholders or variables (such as {topic} or {customer_name}) to generate consistent prompts on demand.")
    )

    print("Conversation History:\n")

    for index, message in enumerate(chat_history.messages, start=1):
        print(f"Message  {index}")
        print(f"Type    :{message.type}")
        print(f"Content :{message.content}")
        print_separator()

if __name__ == "__main__":
    main()
