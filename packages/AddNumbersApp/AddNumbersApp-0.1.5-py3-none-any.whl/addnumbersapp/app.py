# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    # Get numbers from query parameters
    num1 = request.args.get('num1', type=int)
    num2 = request.args.get('num2', type=int)
    
    # Add the numbers
    result = num1 + num2
    
    # Return the result
    return jsonify({"result": result})

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
