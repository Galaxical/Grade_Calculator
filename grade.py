def calc_grade(*scores):
    """
    This function takes multiple student scores as an input 
    and prints out the corresponding based on the criteria.
    
    100 - 70 -> A
    69- 65   -> B
    64 - 55  -> C
    54 - 45  -> D
    44 - 0   -> F

    """

    for score in scores:

        if 70 <= score <= 100:
            grade = 'A'

        elif 65 <= score <= 69:
            grade = 'B'
        
        elif 55 <= score <=64:
            grade = 'C'
        
        elif 45 <= score <= 54:
            grade = 'D'
        
        elif 0 <= score <= 45:
            grade = 'F'
        
        else:
            grade = 'Invalid Score' #handles cases where scores is not available
        
        print(f"Score: {score} -> Grade: {grade}")

calc_grade(85, 72, 90, 71, 65, 31, 56, 100, 110, 48)

