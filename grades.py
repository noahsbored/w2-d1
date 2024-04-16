def graadeees(grades):
  
 

 
    average_grade = sum(grades) / len(grades)


    highest_grade = max(grades)
    lowest_grade = min(grades)

    return average_grade, highest_grade, lowest_grade


grades = [85, 90, 92, 78, 88]
average, highest, lowest = graadeees(grades)
print("average ", average)
print("highest ", highest)
print("lowest ", lowest)
