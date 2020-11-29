class MockData:
    mock_jwt_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDY2NTI0NTgsIm5iZiI6MTYwNjY1MjQ1OCwianRpIjoiMzIyYTg5ZWEtNjcyMC00YmY0LTg4ODQtNzI1Mzk2YzQ4ZTE3IiwiZXhwIjoxNjA2NjUzMzU4LCJpZGVudGl0eSI6InRlc3QxMTEiLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.82uDJ3F-5-6ub-uTOQ4YI4r8RZMaTfHcd_zxMYIRNG0"
    mock_request_headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer '+mock_jwt_token
    }

    mock_sign_in_data = {
        "username": "test111",
        "password": "Test@#123"
    }

    mock_user_data = {
        "username": "test111",
        "password": "Test@#123",
        "name": "Test Account",
        "email": "test@gmail.com",
        "dob": "14/05/1995"
    }

    mock_update_user_data = {
        "name": "Updated Test Account"
    }

    mock_change_password_data = {
        "old_password": "Test@#123",
        "new_password": "Test@#456"
    }

    mock_movie_data = {
        "age_restriction": "16+",
        "cast": [
            "Harrison Ford",
            "Sean Connery",
            "Denholm Elliott"
        ],
        "category": "Action",
        "country": "US",
        "description": "This time he's after the Holy Grail. But the Nazis and snakes are back, and his dad's not making things any easier.",
        "duration": 7620000,
        "genres": [
            "Harrison Ford",
            "Sean Connery",
            "Denholm Elliott"
        ],
        "is_favourite": False,
        "media": [{
            "client": "Desktop",
            "path": "https://x.mp4",
            "type": ".mp4"
        }],
        "movie_type": "Exciting",
        "production": "Hollywood",
        "ratings": 96,
        "subtitles": [{
            "language": "eng",
            "path": "https://x.txt"
        }],
        "thumbnails": [{
            "client": "Desktop",
            "path": "https://images-na.ssl-images-amazon.com/images/I/81UOBSDQh0L._AC_SY741_.jpg",
            "size": "273x109",
            "type": "JPEG"
        }],
        "timestamp": 628193339,
        "title": "Test Indiana Jones"
    }

    mock_favourite_data = {
        "is_favourite": True
    }

    mock_user = 'test111'
    mock_api_version = '/api/v1'

    # Mock User API endpoints
    mock_profile_endpoint = mock_api_version+'/profile/'+mock_user
    mock_update_profile_endpoint = mock_api_version+'/update_profile/'+mock_user
    mock_change_password_endpoint = mock_api_version+'/change_password/'+mock_user
    mock_delete_account_endpoint = mock_api_version+'/delete_account/'+mock_user

    # Mock Movies api endpoints
    mock_movie_title = 'Test Indiana Jones'
    mock_add_movie_endpoint = mock_api_version+'/add_movie/'+mock_user
    mock_fetch_movies_endpoint = mock_api_version+'/fetch_movies/'+mock_user
    mock_search_movie_endpoint = mock_api_version +'/search_movie/'+mock_movie_title+'/'+mock_user
    mock_delete_movie_endpoint = mock_api_version +'/delete_movie/'+mock_movie_title+'/'+mock_user
    mock_favourite_movies_endpoint = mock_api_version +'/favourite_movies/'+mock_user
    mock_add_to_favourite_movie_endpoint = mock_api_version +'/add_to_favourite/'+mock_movie_title+'/'+mock_user
    mock_trending_now_endpoint = mock_api_version +'/trending_now/'+mock_user