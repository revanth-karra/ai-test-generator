# AI Test Generator - Task 6 Complete
# Combining Functions, Lists, and Dictionaries

def generate_test_report(test_case):
    report = "Test: " + test_case["name"] + " | Status: " + str(test_case["expected_status"])
    return report

test_cases = [
    {"name": "Login API Test", "endpoint": "/api/login", "expected_status": 200},
    {"name": "Logout API Test", "endpoint": "/api/logout", "expected_status": 200}
]

print("AI TEST GENERATOR - Ready!")
for test in test_cases:
    print(generate_test_report(test))
