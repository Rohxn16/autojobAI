from modules.models.Models import JobRoleModel
from modules.retrieval_pipeline.retriever import retrieve_top_k
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

class PositionEvaluator:

    def __init__(self):
        self.model = ChatOllama(
            model="gemma:7b",
            temperature=0,
        )
    
    def evaluate_position(self) -> JobRoleModel:
        # Retrieve context from vector database
        query = "User's projects, skills, and work experience for job role recommendation"
        context_docs = retrieve_top_k(query, k=3)
        context_text = "\n".join([doc.page_content for doc in context_docs])

        # Prepare the prompt
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert career advisor. Analyze the user's background and recommend the top 3 most suitable standard industry job roles. OUPUT RULES: 1. Return ONLY the standard job title (e.g., 'Software Engineer', 'Data Scientist', 'Product Manager'). 2. DO NOT add modifiers like 'Junior', 'Senior', 'with AI focus', 'Specialist', etc. 3. The titles must be generic and easily queryable on job boards."),
            ("human", "Context from Resume:\n{context}\n\nBased on the above, identify the 3 best fitting standard job roles."),
        ])

        # Use structured output
        structured_llm = self.model.with_structured_output(JobRoleModel)
        chain = prompt | structured_llm

        result = chain.invoke({"context": context_text})
        return result