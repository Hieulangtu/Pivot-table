import uuid
import random
import json
from datetime import datetime

# def generate_users(num_users):
#     users = []
#     for _ in range(num_users):
#         # Generate UUID for user
#         user_id = uuid.uuid4()

#         # Generate random name and surname
#         names = ["Alice", "Bob", "Charlie", "David", "Emma", "Messi", "Grace", "Hannah", "Ivy", "Jack"]
#         surnames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

#         name = random.choice(names)
#         surname = random.choice(surnames)

#         # Generate email
#         email = f"{name.lower()}.{surname.lower()}@mu.com"

#         user = {
#             "id": str(user_id),
#             "name": name,
#             "surname": surname,
#             "email": email
#         }
#         users.append(user)
#     return users

# # Generate 8 random users
# users = generate_users(8)
# for user in users:
#     print(user)




# Sample users data
users = [
    {"id": "1", "name": "Alice", "surname": "Smith", "email": "alice.smith@mu.com"},
    {"id": "2", "name": "Bob", "surname": "Johnson", "email": "bob.johnson@mu.com"},
    {"id": "3", "name": "Charlie", "surname": "Williams", "email": "charlie.williams@mu.com"},
    {"id": "4", "name": "David", "surname": "Brown", "email": "david.brown@mu.com"},
    {"id": "5", "name": "Emma", "surname": "Jones", "email": "emma.jones@mu.com"}
    # Add more users if needed
]

def generate_group_authors(users):
    group_authors = []
    
    for _ in range(10):
        authors = []
        
        # Random number of authors (1 to 3)
        num_authors = random.randint(1, 3)
        

        total_share = 1.0
        for i in range(num_authors):
            user = random.choice(users)
            
            # Generate share
            # Generate share for the last author
            if i == num_authors - 1:
                share = total_share
            else:
                # Random share between 0.0 and total_share
                share = round(random.uniform(0, total_share), 2)
            
            total_share -= share
            
            author = {
                "user": {
                    "id": user["id"],
                    "name": user["name"],
                    "surname": user["surname"],
                    "email": user["email"]
                },
                "id": str(uuid.uuid4()),
                "order": i + 1,
                "valid": True,
                "lastchange": datetime(year=2024, month=random.randint(1, 12), day=random.randint(1, 28)).isoformat(),
                "share": share
            }
            
            authors.append(author)
        
        group_authors.append( authors)
    
    return group_authors

# Generate group authors
group_authors = generate_group_authors(users)

# Save group authors to group_authors.json
# with open("group_authors.json", "w") as f:
#     json.dump(group_authors, f, indent=4)
for g in group_authors:
    print(g)

