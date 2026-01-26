from modules.job_searcher.experience_evaluator import ExperienceEvaluator
from modules.job_searcher.position_evaluator import PositionEvaluator
from typing import List

class JobQueryBuilder:
    def __init__(self):
        self.experience_evaluator = ExperienceEvaluator()
        self.position_evaluator = PositionEvaluator()

    def generate_queries(self) -> List[str]:
        """
        Generates a list of job search queries by combining the user's experience level
        with the recommended job roles.
        """
        # Get experience level
        experience_model = self.experience_evaluator.evaluate_experience()
        experience_level = experience_model.experience

        # Get job roles
        job_role_model = self.position_evaluator.evaluate_position()
        roles = [job_role_model.role1, job_role_model.role2, job_role_model.role3]

        # Combine to form queries
        queries = [f"{experience_level} {role}" for role in roles]
        
        return queries
