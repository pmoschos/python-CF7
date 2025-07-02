from typing import List, Tuple, Union

# 4 exercises, 1 midterm exam, 1 final exam
# Weights: 40% for exercises, 30% for midterm, 30% for final

def calculate_grade(assignment_scores: List[Union[int, float]], mid_score: Union[int, float], final_score: Union[int, float]) -> Tuple[float, str]:
    """
    Calculate the final grade based on assignment scores, midterm score, and final exam score.

    Args:
        assignment_scores (list of int/float): Scores of the assignments.
        mid_score (int/float): Score of the midterm exam.
        final_score (int/float): Score of the final exam.

    Returns:
        tuple: A tuple containing the final average score and the corresponding letter grade.
    """
    
    def weighted_average() -> float:
        """
        Calculate the weighted average of the assignment scores, midterm score, and final exam score.
        
        Returns:
            float: The weighted average score.
        """
        # Calculate the average of the assignment scores
        assignment_score = sum(assignment_scores) / len(assignment_scores)
        
        # Calculate the weighted average
        return (assignment_score * 0.4) + (mid_score * 0.3) + (final_score * 0.3)

    def determine_grade(average: float) -> str:
        """
        Determine the letter grade based on the average score.
        
        Args:
            average (float): The average score.
        
        Returns:
            str: The letter grade.
        """
        # Determine the letter grade based on the average score
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    
    # Calculate the weighted average
    average = weighted_average()
    
    # Determine the letter grade
    grade = determine_grade(average)

    return average, grade

def main():
    # Test the function
    final_average, final_grade = calculate_grade([85, 90, 88, 92], 92, 84)
    print(f"The final grade is {final_grade} with average: {int(final_average)}")

if __name__ == '__main__':
    main()
