
def chatbot(user_input):
    responses = {
        "hi": "Hello! How can I help you?",
        "bye": "Goodbye! Have a great day!",
        "python": "Python is an amazing programming language!",
    }
    return responses.get(user_input.lower(), "I didn't understand that.")

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break
    print(f"Bot: {chatbot(user_input)}")

def calculate_bmi(weight, height):
    bmi=weight/(height**2)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")
#Example usage
weight=float(input("Enter your weight(kg): "))
height=float(input("Enter your height(m): "))
calculate_bmi(weight,height)

