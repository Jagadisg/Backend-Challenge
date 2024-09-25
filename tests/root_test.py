def test_ready_endpoint(client):
    """Test the readiness endpoint"""
    response = client.get('/')
    
    assert response.status_code == 200
    
    json_data = response.get_json()
    assert json_data['status'] == 'ready'
    assert 'time' in json_data