#!/user/bin/env python3.8

# Week 13 LUIT project: EC2 Random Name Generator

# Objective: 
# Several departments share an AWS environment. You need to ensure that the EC2s are properly named and are
# unique so team members can easily tell who the EC2 instances belong to. Use Python to create your unique EC2 
# names, so that the users can then attach to the instances. 

#The Python Script should:

# 1. Allow the user to input the name of their department that is used in the unique name.
# 2. Allow the user to input how many EC2 instances they want names for and output the same amount of unique names.
# 3. Generate random characters and numbers that will be included in the unique name.

import random
import string

# Prompt the user with a message and get their input.
# Convert their input to lowercase.
depts = set(['marketing', 'accounting', 'finops'])
depts_name = input("Hello! What is the name of your department: ").lower()

if depts_name not in depts: 
    print("Your Department is not available. Please try again.")
    exit()
    
# Prompt the user with a yes/no.
# Convert their input to lowercase.
ec2_inst = input("Will you need unique generated names for your department? Please enter YES/NO to continue:").lower()

if ec2_inst== "yes":
    print("Thank you. Please continue: ")
    
elif ec2_inst== "no":
    print("Thank you for visiting. Goodbye!")
    exit()

# Prompt the user with a message and get number of EC2 instances needed. 
ec2_inst = input("How many EC2 instances will you unique names generated for: ")
ec2_inst = int(ec2_inst)
for _ in range(ec2_inst):

# Print Department name along with random number from 0 to 100000000.
    n = random.randint(0,100000000)
    print("Department Name Generator: ")
    print(depts_name,'_', str(n))