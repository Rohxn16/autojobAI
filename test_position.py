import sys
import os

# Add root to sys.path
sys.path.append(os.getcwd())

from modules.job_searcher.position_evaluator import PositionEvaluator

def main():
    try:
        evaluator = PositionEvaluator()
        print("Evaluating position...")
        result = evaluator.evaluate_position()
        print("Result type:", type(result))
        print("Result:", result)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
