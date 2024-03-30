from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Basic HTTP Server
@app.route('/')
def home():
    return "Hello, this is a basic web server!"

# Different Types of Content - JSON
@app.route('/json')
def json_response():
    data = {'message': 'This is a JSON response'}
    return jsonify(data)

# Different Types of Content - XML
@app.route('/xml')
def xml_response():
    xml_data = '<data><message>This is an XML response</message></data>'
    return app.response_class(xml_data, content_type='application/xml')

# Different Types of Content - CSV
@app.route('/csv')
def csv_response():
    csv_data = 'name,age\nJohn,25\nJane,30'
    return app.response_class(csv_data, content_type='text/csv')

# Serve HTML as strings
@app.route('/html')
def html_string():
    html_content = '<html><body><h1>This is an HTML response</h1></body></html>'
    return app.response_class(html_content, content_type='text/html')

# Load HTML files and serve content
@app.route('/html-file')
def html_file():
    return render_template('index.html')

# Routing using HTTP Request Object
@app.route('/dynamic/<name>')
def dynamic_route(name):
    return f"Hello, {name}! This is a dynamic route."

if __name__ == '__main__':
    app.run()
