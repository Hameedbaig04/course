import re

# Search for digits
match = re.search(r"\d+", "Price: 250")
print("Search result:", match.group() if match else "No match")

# Find all words
words = re.findall(r"\w+", "Hello World!")
print("Findall result:", words)

# Replace spaces with hyphens
replaced = re.sub(r"\s+", "-", "Hello   World")
print("Sub result:", replaced)