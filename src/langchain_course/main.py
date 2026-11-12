import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()  # reads OPENAI_API_KEY from .env


def main() -> None:
    # llm = ChatOpenAI(model="gpt-4o-mini")
    # response = llm.invoke("Say hello in one sentence.")
    # print(response.content)
    print("hello from langchain")
    print(os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
