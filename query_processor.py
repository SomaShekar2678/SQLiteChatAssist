import re

def convert_query_to_sql(user_query):
    print(f"🔍 Received Query: {user_query}") 

    # Normalize input
    user_query = user_query.lower().strip().rstrip('?').rstrip('.')  # Remove trailing ? and .

    # Remove extra spaces between words
    user_query = re.sub(r'\s+', ' ', user_query)  

    patterns = {
        r"show me all employees in (.+)": 
            "SELECT Name FROM Employees WHERE LOWER(Department) = LOWER('{}')",

        r"who is the manager of (.+)":  
            "SELECT Manager FROM Departments WHERE LOWER(Name) = LOWER('{}')",  # Handles extra spaces

        r"list all employees hired after (\d{4}-\d{2}-\d{2})": 
            "SELECT Name FROM Employees WHERE Hire_Date > '{}'",

        r"what is the total salary expense for (.+)":  
            "SELECT SUM(Salary) FROM Employees WHERE LOWER(Department) = LOWER('{}')"
    }
    
    for pattern, sql_template in patterns.items():
        match = re.match(pattern, user_query)
        print(f"🧐 Trying pattern: {pattern}")  
        if match:
            matched_value = match.groups()[0].strip()  # Trim spaces in captured groups
            sql_query = sql_template.format(matched_value)
            print(f"✅ SQL Generated: {sql_query}")  
            return sql_query
    
    print("❌ No match found!")  
    return None
