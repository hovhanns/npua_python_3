from flask import Flask, request

app = Flask("valod")


@app.route('/', methods=['GET'])
def get_example():
    return 'This is a GET request example'


@app.route('/students', methods=['GET'])
def get_students():
    students = [
        {'name': 'John', 'age': 21},
        {'name': 'Jane', 'age': 22},
        {'name': 'Jim', 'age': 23}
    ]
    return {'students': students}


@app.route('/', methods=['POST'])
def post_example():
    data = request.get_json()
    print(request.data)
    return f'This is a POST request example. Received data: {data}'


@app.route('/', methods=['PUT'])
def put_example():
    data = request.get_json()
    return f'This is a PUT request example. Received data: {data}'


@app.route('/', methods=['DELETE'])
def delete_example():
    return 'This is a DELETE request example'


if __name__ == '__main__':
    app.run()

# # create curl requests to test the endpoints
