desired_grade = input("Enter desired grade:")

minimum_mean = float(input("Enter the minimum average required:"))

current_mean = float(input("Enter the current average in course:"))

final_weight = float(input("Enter the weight of the final in percentage:")) / 100

final_score = (minimum_mean-current_mean*(1-final_weight))/final_weight

print("You need a score of",final_score,"on the final to get a", desired_grade )

