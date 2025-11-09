#!/usr/bin/env python3
"""
Quick script to test Sustainabite API endpoints after deployment
Usage: python test_endpoints.py <your-render-url>
Example: python test_endpoints.py https://sustainabite-backend.onrender.com
"""

import sys
import requests
import json


def test_endpoint(base_url: str):
    """Test all API endpoints"""
    
    print(f"\n{'='*60}")
    print(f"Testing Sustainabite API at: {base_url}")
    print(f"{'='*60}\n")
    
    # Test 1: Root endpoint
    print("1. Testing root endpoint (/)...")
    try:
        response = requests.get(f"{base_url}/")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {json.dumps(response.json(), indent=2)}")
        print("   ✅ Root endpoint working!\n")
    except Exception as e:
        print(f"   ❌ Error: {e}\n")
    
    # Test 2: Health check
    print("2. Testing health check (/health)...")
    try:
        response = requests.get(f"{base_url}/health")
        print(f"   Status: {response.status_code}")
        data = response.json()
        print(f"   Response: {json.dumps(data, indent=2)}")
        if data.get("gemini_available"):
            print("   ✅ Health check passed! Gemini API configured.\n")
        else:
            print("   ⚠️  Health check passed but Gemini API not configured.\n")
    except Exception as e:
        print(f"   ❌ Error: {e}\n")
    
    # Test 3: Random restaurant
    print("3. Testing random restaurant (/api/restaurant)...")
    try:
        response = requests.get(f"{base_url}/api/restaurant")
        print(f"   Status: {response.status_code}")
        data = response.json()
        print(f"   Restaurant: {data.get('name', 'N/A')}")
        print(f"   Description: {data.get('description', 'N/A')}")
        print(f"   Image URL: {data.get('img', 'N/A')}")
        print("   ✅ Restaurant endpoint working!\n")
    except Exception as e:
        print(f"   ❌ Error: {e}\n")
    
    # Test 4: API Documentation
    print("4. Testing API docs (/docs)...")
    try:
        response = requests.get(f"{base_url}/docs")
        if response.status_code == 200:
            print(f"   Status: {response.status_code}")
            print(f"   ✅ API documentation available at: {base_url}/docs\n")
        else:
            print(f"   ⚠️  Status: {response.status_code}\n")
    except Exception as e:
        print(f"   ❌ Error: {e}\n")
    
    # Test 5: Recipe generation (requires Gemini API)
    print("5. Testing recipe generation (/api/recipes)...")
    try:
        payload = {
            "available_ingredients": ["chicken", "rice", "onion", "garlic"],
            "available_utensils": ["pot", "pan", "knife"],
            "preference": "quick and healthy",
            "budget": 10.0
        }
        response = requests.post(f"{base_url}/api/recipes", json=payload)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"   Title: {data.get('Title', 'N/A')}")
            recipes = data.get('recipes', [])
            print(f"   Number of recipes: {len(recipes)}")
            if recipes:
                print(f"   First recipe: {recipes[0].get('name', 'N/A')}")
            print("   ✅ Recipe generation working!\n")
        elif response.status_code == 503:
            print("   ⚠️  Gemini API not configured. Set GEMINI_API_KEY environment variable.\n")
        else:
            print(f"   Response: {response.text}\n")
    except Exception as e:
        print(f"   ❌ Error: {e}\n")
    
    print(f"{'='*60}")
    print("Testing complete!")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_endpoints.py <base-url>")
        print("Example: python test_endpoints.py https://sustainabite-backend.onrender.com")
        print("\nTesting with default local URL: http://localhost:8000")
        base_url = "http://localhost:8000"
    else:
        base_url = sys.argv[1].rstrip('/')
    
    test_endpoint(base_url)

