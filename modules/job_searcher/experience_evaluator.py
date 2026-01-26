from modules.models.Models import EvaluateExperienceModel
from modules.retrieval_pipeline.retriever import retrieve_top_k
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

class ExperienceEvaluator:

    def __init__(self):
        self.model = ChatOllama(
            model="gemma:7b",
            temperature=0,
        )
    
    def evaluate_experience(self) -> EvaluateExperienceModel:
        # Retrieve context from vector database
        query = "User's work experience and resume details"
        context_docs = retrieve_top_k(query, k=5)
        context_text = "\n".join([doc.page_content for doc in context_docs])

        # Prepare the prompt with retrieved context
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert career evaluator. Analyze the user's resume context and determine their experience level. The output must be one of: 'entry level', 'junior', 'senior'."),
            ("human", "Context from Resume:\n{context}\n\nBased on the above, classify the user's experience level."),
        ])

        # Use structured output to match the Pydantic model
        structured_llm = self.model.with_structured_output(EvaluateExperienceModel)
        chain = prompt | structured_llm

        result = chain.invoke({"context": context_text})
        return result
