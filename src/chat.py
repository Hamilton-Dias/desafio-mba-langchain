from search import search_prompt
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def main():
  while True:
    question = input("Ask a question: ")

    chain = search_prompt(question)

    if not chain:
      print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
      return
    
    llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
    pipe = chain | llm

    result = pipe.invoke({'question': question})
    print("LLM's answer: " + result.content)

if __name__ == "__main__":
  main()
