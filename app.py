import os
import json
import requests
from flask import Flask, request, jsonify
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

#MOCK DB Change when DB is available
MOCK_DB = [
    {"id": 1, "category": "Rice", "brand": "NFA Well-Milled", "unit": "kg", "price": 45.00},
    {"id": 2, "category": "Rice", "brand": "Sinandomeng Premium", "unit": "kg", "price": 58.00},
    {"id": 4, "category": "Chicken", "brand": "Palengke Cut", "unit": "kg", "price": 200.00},
    {"id": 5, "category": "Pork", "brand": "Kasim", "unit": "kg", "price": 320.00},
    {"id": 7, "category": "Canned Goods", "brand": "555 Sardines", "unit": "piece", "price": 19.50},
    {"id": 8, "category": "Canned Goods", "brand": "Ligo Sardines", "unit": "piece", "price": 21.00},
    {"id": 11, "category": "Instant Noodles", "brand": "Payless", "unit": "pack", "price": 9.00},
    {"id": 12, "category": "Instant Noodles", "brand": "Lucky Me!", "unit": "pack", "price": 11.50},
    {"id": 13, "category": "Bath Soap", "brand": "Bioderm Yellow", "unit": "bar", "price": 18.00},
    {"id": 14, "category": "Bath Soap", "brand": "Safeguard Pure White", "unit": "bar", "price": 31.25},
]

def parse_raw_groceries(raw_input_string):
    """Uses Gemini to clean and categorize messy user inputs."""
    client = genai.Client()
    prompt = f"""
    Map the following user input ONLY to these exact database categories:
    - Rice, Chicken, Pork, Canned Goods, Instant Noodles, Bath Soap, Shampoo.
    Return ONLY a valid JSON array of strings. No markdown.
    User Input: "{raw_input_string}"
    """
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(response_mime_type="application/json"),
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"Gemini Error: {e}")
        return []

def find_cheapest_and_alternatives(category_name):
    """Searches the mock DB for a category and sorts by cheapest price."""
    matched_items = [item for item in MOCK_DB if item['category'].lower() == category_name.lower()]
    if not matched_items:
        return None
        
    sorted_items = sorted(matched_items, key=lambda x: x['price'])
    return {
        "selected": sorted_items[0], 
        "alternatives": sorted_items[1:] 
    }

def get_nearby_stores(lat, lng):
    """
    Calls the Google Maps Places API with strict type filtering 
    to guarantee only retail food markets are returned.
    """
    api_key = os.getenv("MAPS_API_KEY")
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    
    params = {
        "location": f"{lat},{lng}",
        "radius": 5000,
        "keyword": "grocery OR wet market OR palengke",
        "type": "store",
        "key": api_key
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        stores = []
        for place in data.get('results', [])[:5]:
            
            stores.append({
                "name": place.get("name"),
                "address": place.get("vicinity"),
                "lat": place["geometry"]["location"]["lat"],
                "lng": place["geometry"]["location"]["lng"]
            })
        return stores
    except Exception as e:
        print(f"Maps API Error: {e}")
        return []

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "active", "message": "Sapat App Backend engine is running!"})

@app.route('/calculate', methods=['POST'])
def calculate_grocery_list():
    try:
        data = request.get_json()
        budget = float(data.get('budget', 0.0))
        raw_items_array = data.get('raw_items', [])

        raw_input_string = ", ".join(raw_items_array)

        clean_categories = parse_raw_groceries(raw_input_string)

        final_receipt = []
        total_cost = 0.0

        for category in clean_categories:
            result = find_cheapest_and_alternatives(category)
            if result:
                item_cost = result['selected']['price']
                total_cost += item_cost
                final_receipt.append(result)

        return jsonify({
            "status": "success",
            "original_budget": budget,
            "total_cost": total_cost,
            "remaining_balance": budget - total_cost,
            "receipt": final_receipt
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    
@app.route('/nearby-stores', methods=['POST'])
def nearby_stores():
    try:
        data = request.get_json()
        lat = data.get('lat')
        lng = data.get('lng')

        if not lat or not lng:
            return jsonify({"status": "error", "message": "Missing coordinates"}), 400

        stores = get_nearby_stores(lat, lng)

        return jsonify({
            "status": "success",
            "stores": stores
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)