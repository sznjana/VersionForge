# This program collects feedback from students

def collect_feedback():
    print("===== Student Feedback Form =====")
    
    # Ask for the student's name
    student_name = input("What is your name? ")
    
    # Ask for the course name
    course = input("What course are you rating? ")
    
    # Ask for a rating from 1 to 5
    rating = 0
    while rating < 1 or rating > 5:
        try:
            rating = int(input("How would you rate this course from 1-5? "))
            if rating < 1 or rating > 5:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("That's not a number! Please enter a number between 1 and 5.")
    
    # Ask for any comments
    comments = input("Do you have any other comments? ")
    
    # Create a feedback dictionary (like a container with labeled sections)
    feedback = {
        "student_name": student_name,
        "course": course,
        "rating": rating,
        "comments": comments
    }
    
    print("Thank you for your feedback!")
    return feedback

def save_feedback(feedback, filename="feedback_data.txt"):
    # This makes sure we have a data folder
    import os
    os.makedirs("data", exist_ok=True)
    
    # Save the feedback to a file
    with open(f"data/{filename}", "a") as file:
        file.write(f"{feedback['student_name']}|{feedback['course']}|{feedback['rating']}|{feedback['comments']}\n")
    
    print("Your feedback has been saved!")

# When we run this file directly
if __name__ == "__main__":
    feedback = collect_feedback()
    save_feedback(feedback)
