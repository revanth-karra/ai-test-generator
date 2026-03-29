test_case = {
    "name": "Login API Test",
    "endpoint": "/api/login",
    "method": "POST",
    "expected_status": 200,
    "is_active": True
}

# 2. Print Individual Values
print("Test Case Details:")
print("_" * 40)
print("Name:", test_case["name"])
print("Endpoint:", test_case["endpoint"])
print("Method:", test_case["method"])
print("Expected Status:", test_case["expected_status"])
print("Is Active:", test_case["is_active"])
print("_" * 40)

# Loop Through Dictionary
print("All Test Properties:")
for key, value in test_case.items():
    print(key + ":", value)
