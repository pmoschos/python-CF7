# 🎓 Grade Calculation Script ✅

Welcome to the Grade Calculation Script! This script calculates the final grade for a student based on their scores in assignments, a midterm exam, and a final exam. It also determines the corresponding letter grade based on the final average score.

## Script Overview 📘

The script takes the scores of four assignments, a midterm exam, and a final exam, and calculates the weighted average to determine the final grade. The weights are as follows:
- **Assignments**: 40%
- **Midterm Exam**: 30%
- **Final Exam**: 30%

### :computer: Script Code

```python
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
```

# Key Features 🌟
- **Weighted Average Calculation**: Calculates the final score based on weighted averages of assignments, midterm, and final exam.
- **Letter Grade Determination**: Determines the letter grade based on the calculated average score.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None (uses built-in Python functionalities)

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `02_inner_functions.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `02_inner_functions.py`.
5. Run the script with: `python 02_inner_functions.py`.

## Usage Example 📋
Execute the script to see how it calculates the final grade based on the input scores. The script will demonstrate the calculation and print the final grade along with the average score.

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).


## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by 
  <a href="https://www.linkedin.com/in/panagiotis-moschos" target="_blank">
  Panagiotis Moschos</a> (https://github.com/pmoschos)
</p>
