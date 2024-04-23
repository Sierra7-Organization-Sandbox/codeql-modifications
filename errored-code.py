# Error 1: Unused import statement
# import math

# # Error 2: Function with a syntax error
# def greet(name)
#     print("Hello, " + name)

# # Error 3: Function with a semantic error
# def divide(a, b):
#     return a * b  # Should be return a / b

# # Error 4: Variable name shadowing
# def calculate_area(radius):
#     area = math.pi * radius * radius
#     radius = 10  # Shadows the function parameter

# # Error 5: Potential SQL injection vulnerability
# def fetch_user_data(user_id):
#     query = "SELECT * FROM users WHERE id = " + user_id  # Concatenating user input directly into SQL query

# # Error 6: Unhandled exception
# def read_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#         return content
#     except FileNotFoundError:  # Error not handled properly
#         pass

# # Error 7: Infinite loop
# def countdown():
#     while True:
#         print("3...")
#         print("2...")
#         print("1...")
#         print("Blastoff!")

# # Error 8: Unused variable
# x = 5

if __name__ == "__main__":
    # Error 9: Calling non-existent function
    # result = add(3, 5)
    # print(result)
    print('No problems here')
