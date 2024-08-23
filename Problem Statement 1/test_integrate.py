import requests

# URL of the backend API endpoint
backend_url = "<Backend Url>"

# URL of the frontend page that should display the message
frontend_url = "<Frontend Url>"

def test_frontend_backend_integration():
    # Step 1: Get the message from the backend
    backend_response = requests.get(backend_url)
    
    # Check if the backend response is successful
    assert backend_response.status_code == 200, "Backend response failed"
    
    # Extract the message from the backend response
    expected_message = backend_response.json().get("message")
    
    # Step 2: Get the displayed message from the frontend
    frontend_response = requests.get(frontend_url)
    
    # Check if the frontend response is successful
    assert frontend_response.status_code == 200, "Frontend response failed"
    
    # Step 3: Verify that the frontend displays the correct message
    assert expected_message in frontend_response.text, "Message not correctly displayed on the frontend"

    print("Test passed: Frontend correctly displays the message returned by the backend.")

# Run the test
if __name__ == "__main__":
    test_frontend_backend_integration()
