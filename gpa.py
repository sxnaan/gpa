def main():

    weights = {
        "a+": 4.0, "a": 4.0, "a-": 3.7,
        "b+": 3.3, "b": 3.0, "b-": 2.7,
        "c+": 2.3, "c": 2.0, "c-": 1.7,
        "d+": 1.3, "d": 1.0, "d-": 0.7,
        "f": 0
    }

    
    gpa = float(input("current gpa? "))
    total_credits = int(input("credits total atm? (excluding ap)? ")) 
    q_points = gpa * total_credits 

    num_classes = int(input("classes taken this semester? "))
    print("")

    # multiply curr gpa by current credits, add new credits,  
    
    term_gpa = 0
    term_credits = 0
    term_qp = 0

    for i in range(num_classes):
        print("class " + str(i+1) + ":")
        class_credits = int(input("how many credits? "))
        letter_grade = input("grade received/expected? ").lower()

        # update cumulative gpa
        total_credits += class_credits
        q_points += weights[letter_grade] * class_credits 
        gpa = q_points / total_credits

        # update term gpa
        term_credits += class_credits
        term_qp += weights[letter_grade] * class_credits
        term_gpa = term_qp / term_credits

        print("")

    print("YOUR TERM GPA IS " + str(term_gpa))
    print("YOUR NEW GPA IS " + str(gpa) + "\n")

main()

