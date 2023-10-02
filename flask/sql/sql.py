from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Replace 'your_username', 'your_password', 'your_database' with your MySQL credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'flask'
}

# Create a MySQL database connection
connection = mysql.connector.connect(**db_config)

# Create a cursor object to execute SQL queries
db = connection.cursor()


@app.route('/get_users', methods=['GET'])
def get_users():
    try:
        # Define your SQL query
        query = "SELECT * FROM users"

        # Execute the SQL query
        db.execute(query)

        # Fetch all the results
        results = db.fetchall()
        # for result in results:
        #     print(f"<h1>{result}</h1><br>")

        return render_template('show.html',results = results)
    
        # Create a list to store the results
        user_list = []

        # Iterate through the results and extract data
        for result in results:
            user_data = {
                'id': result[0],
                'username': result[1],
                'email': result[2]
            }
            user_list.append(user_data)

        # Close the cursor and the connection
        cursor.close()
        connection.close()

        # Return the list of users as JSON
        return jsonify(user_list)

    except Exception as e:
        return str(e)


@app.route('/add_user')
def add_user():
    try:
        # Get user data from the request
        fname = 'nouman'
        lname = 'rehman'
        email = 'noumanrehman@hotmail.com'


        # Define the SQL query to insert a new user
        query = "INSERT INTO users (fname, lname,email) VALUES (%s, %s,%s)"
        values = (fname,lname,email)

        # Execute the SQL query
        db.execute(query, values)

        # Commit the transaction
        connection.commit()

        # Close the cursor and the connection
        db.close()
        connection.close()

        return jsonify({'message': 'User added successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
