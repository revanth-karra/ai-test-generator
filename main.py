# Function to greet user
def greet_user(name):
    message = "Hello, " + name + "! Welcome to AI Test Generator"
    return message

# Function to calculate version info
def get_version_info(version):
    full_version = "Version " + str(version)
    return full_version


print(greet_user("Revanth"))
print(get_version_info(1.0))
