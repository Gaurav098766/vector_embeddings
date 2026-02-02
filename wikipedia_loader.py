from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_community.document_loaders import WikipediaLoader
from .model import get_model

load_dotenv()

def answer_question_about(person_name, question, model):
    loader = WikipediaLoader(query=person_name, load_max_docs=1)
    context_text = loader.load()[0].page_content
    template = "Answer this question:\n{question}. Here is some extra context:\n{document}"
    human_prompt = HumanMessagePromptTemplate.from_template(template)
    chat_prompt = ChatPromptTemplate.from_template([human_prompt])
    result = model(chat_prompt.format_prompt(question=question, document=context_text).to_messages())
    print(result)
    return result.content


if __name__ == "__main__":
    model = get_model()
    answer_question_about("Cristiano Ronaldo","When was he born?",model)
