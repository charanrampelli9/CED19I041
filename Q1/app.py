#CED19I041
#Charan Kumar 
from flask import Flask, request, jsonify
import asyncio
import aiohttp

app = Flask(__name__)

async def fetch_numbers(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("numbers", [])
            return []


@app.route('/numbers', methods=['GET'])
async def get_numbers():
    urls = request.args.getlist('url')
    tasks = [fetch_numbers(url) for url in urls]

    try:
        results = await asyncio.gather(*tasks)
    except asyncio.TimeoutError:
        results = []

    merged_numbers = sorted(set(number for result in results if isinstance(result, list) for number in result))
    
    return jsonify({"numbers": merged_numbers})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008,debug=True)
