import re

def extract_domain_from_email(email):
   
    pattern = r'@([A-Za-z0-9.-]+)'
    
    match = re.search(pattern, email)
    
    if match:
        return match.group(1)
    else:
        return None

# Example usage:
email = "user@example.com"
domain = extract_domain_from_email(email)
if domain:
    print(f"The domain is: {domain}")
else:
    print("No domain found in the email.")
