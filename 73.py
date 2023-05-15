def extract_username(email):
    # Split the email address at the "@" symbol
    parts = email.split("@")
    
    # Extract and return the username (the first part)
    username = parts[0]
    return username

# Example usage
email_address = "john@google.com"
username = extract_username(email_address)
print("Username:", username)
