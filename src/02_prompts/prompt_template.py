from pathlib import Path
import sys

# ---------------------------------------------------
# Add the project root to Python's Module search path
# ---------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

    from langchain_core.prompts import PromptTemplate

    from llm_client import get_llm
    from utils.helpers import print_separator, print_title

    def main():
        print_title("PromptTemplate")
        llm = get_llm()

        prompt_template = PromptTemplate(
            template = """
    You are an expert {profession}.
    Explain the concept of {topic} in simple words.
    Keep the explanation under {word_limit} words.
    """,
             input_variables = ["profession", "topic", "word_limit"], 

        )

        prompt=prompt_template.invoke(
            {
                "profession": "AI Engineer",
                "topic": "Transformer",
                "word_limit": 100,
            }
        )

        print("Formatted Prompt:\n")
        print(prompt.text)

        print_separator()
        response = llm.invoke(prompt)

        print("LLM Response:\n")
        print(response.text)

if __name__=="__main__":
    main()
