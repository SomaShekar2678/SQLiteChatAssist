from flask import Flask, request, jsonify, render_template
import sqlite3
from query_processor import convert_query_to_sql

app = Flask(__name__)

# Serve the HTML page
@app.route('/')
def home():
    return render_template("index.html")  # Renders the frontend

@app.route('/query', methods=['POST'])
def query_db():
    user_query = request.json.get('query')

    sql_query = convert_query_to_sql(user_query)
    if sql_query is None:
        return jsonify({"error": "Sorry, I didn't understand the question."}), 400

    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        conn.close()
        return jsonify({"response": results})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
