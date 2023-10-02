#! C:\Users\User\AppData\Local\Programs\Python\Python39\python.exe
# 0

# lines to add in Xampp httpd.config file
# AddHandler cgi-script .py
# ScriptInterpreterSource Registry-Strict

"""
Tasks
Make a form to collect the details of a student with proper validation and sanitization.
Make a form to perform arithmetic operators with proper validation and sanitization.
"""

# Import modules for CGI handling
import cgi

# Create instance of FieldStorage
form = cgi.FieldStorage()
errors = []

# Get data from fields
name = form.getvalue('name')
email  = form.getvalue('email')

print("Content-type:text/html")
print
print("")
print("")
print("Hello - Second CGI Program")
print("")
print("")
print("Hello %s %s" % (name, email))
print("")
print("")


# validation

if not name:
    errors.append("Name is required.")

if not email:
    errors.append("Email is required.")
elif '@' not in email:
    errors.append("Invalid email format.")

# Generate an HTML response
if errors:
    # Display validation errors
    print("<html>")
    print("<head><title>Form Submission Errors</title></head>")
    print("<body>")
    print("<h1>Form Submission Errors</h1>")
    print("<ul>")
    for error in errors:
        print(f"<li>{error}</li>")
    print("</ul>")
    print("</body>")
    print("</html>")
else:
    # Process the valid form data
    print("<html>")
    print("<head><title>Form Submission Success</title></head>")
    print("<body>")
    print("<h1>Form Submission Successful</h1>")
    print(f"<p>Name: {name}</p>")
    print(f"<p>Email: {email}</p>")
    print("</body>")
    print("</html>")





# senitization
# import html

# # Sanitization
# sanitized_comment = html.escape(email)

