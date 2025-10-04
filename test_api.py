"""
Test script to verify FastAPI is working correctly
Run this after starting the FastAPI server
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_api():
    print("=" * 60)
    print("Testing Task Manager API")
    print("=" * 60)
    
    # Test 1: Root endpoint
    print("\n1. Testing root endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 2: Get all tasks (should be empty)
    print("\n2. Getting all tasks (should be empty)...")
    response = requests.get(f"{BASE_URL}/tasks")
    print(f"Status: {response.status_code}")
    print(f"Tasks: {json.dumps(response.json(), indent=2)}")
    
    # Test 3: Create a task
    print("\n3. Creating a new task...")
    task_data = {
        "title": "Test Task 1",
        "description": "This is a test task",
        "completed": False
    }
    response = requests.post(f"{BASE_URL}/tasks", json=task_data)
    print(f"Status: {response.status_code}")
    task1 = response.json()
    print(f"Created Task: {json.dumps(task1, indent=2)}")
    task1_id = task1["id"]
    
    # Test 4: Create another task
    print("\n4. Creating another task...")
    task_data = {
        "title": "Test Task 2",
        "description": "This is another test task",
        "completed": False
    }
    response = requests.post(f"{BASE_URL}/tasks", json=task_data)
    print(f"Status: {response.status_code}")
    print(f"Created Task: {json.dumps(response.json(), indent=2)}")
    
    # Test 5: Get all tasks
    print("\n5. Getting all tasks...")
    response = requests.get(f"{BASE_URL}/tasks")
    print(f"Status: {response.status_code}")
    print(f"Tasks: {json.dumps(response.json(), indent=2)}")
    
    # Test 6: Get specific task
    print(f"\n6. Getting task {task1_id}...")
    response = requests.get(f"{BASE_URL}/tasks/{task1_id}")
    print(f"Status: {response.status_code}")
    print(f"Task: {json.dumps(response.json(), indent=2)}")
    
    # Test 7: Update task
    print(f"\n7. Updating task {task1_id}...")
    update_data = {
        "completed": True,
        "title": "Updated Test Task 1"
    }
    response = requests.put(f"{BASE_URL}/tasks/{task1_id}", json=update_data)
    print(f"Status: {response.status_code}")
    print(f"Updated Task: {json.dumps(response.json(), indent=2)}")
    
    # Test 8: Delete task
    print(f"\n8. Deleting task {task1_id}...")
    response = requests.delete(f"{BASE_URL}/tasks/{task1_id}")
    print(f"Status: {response.status_code}")
    print(f"Result: {json.dumps(response.json(), indent=2)}")
    
    # Test 9: Get all tasks (should have one left)
    print("\n9. Getting all remaining tasks...")
    response = requests.get(f"{BASE_URL}/tasks")
    print(f"Status: {response.status_code}")
    print(f"Tasks: {json.dumps(response.json(), indent=2)}")
    
    print("\n" + "=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to FastAPI server!")
        print("Make sure the FastAPI server is running on http://localhost:8000")
        print("Run: python app.py")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

