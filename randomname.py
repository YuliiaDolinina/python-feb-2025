import random
import string

def generate_ec2_name(department_name, instance_count):
    ec2_names = []
    
    for i in range(instance_count):
        # Generate random characters (letters + numbers)
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        
        # Format EC2 name: department name followed by a random string
        ec2_name = f"{department_name}-{random_str}"
        ec2_names.append(ec2_name)
    
    return ec2_names

def main():
    # User input for department and instance count
    department_name = input("Enter the department name: ")
    instance_count = int(input("How many EC2 instances do you want names for? "))
    
    # Generate EC2 names
    ec2_names = generate_ec2_name(department_name, instance_count)
    
    # Display the unique EC2 names
    print("\nGenerated EC2 Instance Names:")
    for name in ec2_names:
        print(name)

if __name__ == "__main__":
    main()
