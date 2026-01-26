import sys
import os

# Add root to sys.path
sys.path.append(os.getcwd())

from modules.job_searcher.experience_evaluator import ExperienceEvaluator

def main():
    try:
        evaluator = ExperienceEvaluator()
        print("Evaluating experience...")
        result = evaluator.evaluate_experience()
        print("Result type:", type(result))
        print("Result:", result)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
