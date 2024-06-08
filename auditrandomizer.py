import random

# Prompt user to enter items separated by new lines
print("Enter Ids from Airtable. Press Enter twice to finish:")
user_input = []
while True:
    line = input()
    if line == "":
        break
    user_input.append(line)

# Strip any extra whitespace from the items
items = [item.strip() for item in user_input]

# Randomly select 5 items from the list
random_selection = random.sample(items, 5)

# Print the selected items
counter = 0
print("Randomly selected items:")
for item in random_selection:
    counter += 1
    print(f"{counter}: {item}")
