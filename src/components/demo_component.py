from src.models.DemoResponse import DemoResponse
from src.services.demo_service import fetch_external_data

def process_demo_response_data():
    data = fetch_external_data()
    response = DemoResponse(message="Success", data=data, status=200)
    return response
