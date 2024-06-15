
def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
        student_name = ""
        student_name = input("Please enter your name: ")
    # Prompt the user for their scores in Math, Science, and English
  
    # Store the scores in the respective variables: math_score, science_score, english_score
        math_score = 0
        science_score = 0
        english_score = 0
        math_score = input("Please enter your math score: ")
        science_score = input("Please enter your science score: ")
        english_score = input("Please enter your English score: ")
    # Calculate the average grade
        average_grade = 0
        average_grade = (int(math_score) + int(science_score) + int(english_score))/3
    #print (student_name, average_grade)
    # Return the student's name and their average grade
        return student_name, average_grade
    

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"")