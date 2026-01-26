from pydantic import BaseModel, Field

class EvaluateExperienceModel(BaseModel):
    """
    Model for experience that will be used to evaluate the experience of the user based on his previous work experience
    Returns one of the following words:
    - entry level
    - junior
    - senior
    """
    experience: str = Field(..., description="Previous work experience of the user")

class JobRoleModel(BaseModel):
    """
    Determines the job roles that best fit the user based on his previous work experiences and projects from the context.
    Avoid using extra words in the job role names like "SWE with AI specialization" or "SWE with IoT" instead keep the job roles clear and concise with a maximum of 4 words in each role. No more than that.
    Returns 3 separate job roles for the user
    """
    role1: str = Field(..., description="First standard job role. Must be a generic industry title (e.g. '<Field> <Role name>'). Max 3 words.")
    role2: str = Field(..., description="Second standard job role. Must be a generic industry title (e.g. '<Field> <Role name>'). Max 3 words.")
    role3: str = Field(..., description="Third standard job role. Must be a generic industry title (e.g. '<Field> <Role name>'). Max 3 words.")