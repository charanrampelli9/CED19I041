#CED19I041
#Charan Kumar 
from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')

    result = []
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                result.extend(data)
            else:
                result.append({'error': f'Failed to fetch data from {url}', 'url': url})
        except Exception as e:
            result.append({'error': str(e), 'url': url})

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008,debug=True)
