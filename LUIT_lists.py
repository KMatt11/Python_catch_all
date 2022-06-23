#!/user/bin/env python3.8

# Week 12 LUIT project: Create a list of services using Python

# Objectives: 
# Create a list of services using Python. IE: S3, Lambda, EC2, etc.
# 1. The list should be empty initially.
# 2. Populate the list using append or insert.
# 3. Print the list and the length of the list.
# 4. Remove two specific services from the list by name or by index.
# 5. Print the new list and the new length of the list.

# Objective 1 - Create an empty list
services = []

# Objective 2 - Populate the list using append or insert
services.append("S3")
services.append("Lamba")
services.append("EC2")
services.append("DynamoDB")
services.append("CloudFormation")

# Objective 3 - Print the list and the length of the list
print(services)

# Objective 4 - Remove two specific services from the list by name or by index
services.remove("S3")
services.remove("CloudFormation")
print(services)

# Objective 5 - Print the new list and the new length of the list
print (len(services))
