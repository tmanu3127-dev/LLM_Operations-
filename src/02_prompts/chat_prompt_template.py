from pathlib import Path
import sys

# --------------------------------------
# Add the Project root to Python's module search path.
# --------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from langchain_core.prompts import ChatPromptTemplate

from llm_client import get_llm
from utils.helpers import print_separator, print_title

def main():
    print_title("ChatPromptTemplate")
    llm = get_llm()

    chat_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an experienced {profession} who explains concept in a simple and begginer-freindly way.",

            ),
            (
                "human",
                "Explain the concept of {topic} in less than {word_limit} words.",
            ),
            # (
            #     "ai",
            #     "Sure! I will explain it in clear and concise manner.",
            # ),
        ]


    )

    messages = chat_prompt.invoke(
        {
            "profession":"AI Engineer",
            "topic":"Prompt Engineering",
            "word_limit":500,
        }
    )

    print("Formatted Messaged:\n")
    # for message in messages.messages:
    #     print(f"{messages.type.upper()}:")
    #     print(message.content)                 {what done earlier }
    #     print()

    # {New }:

    chat_messages = messages.to_messages()
    for message in chat_messages:
        print(f"{message.type.upper()}:")
        print(message.content)   # use text inspite of content
        print()

    print_separator()

    response = llm.invoke(messages)

    print("LLM Response:\n")
    print(response.content)

if __name__=="__main__":
    main()

