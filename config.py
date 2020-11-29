class Config:
    # Mongo db connection url
    MONGO_DB_CONNECTION = 'mongodb://127.0.0.1:27017/netflix'
    
    # API Configs
    API_PATH = '/api/'
    API_VERSION = 'v1'
    BASE_URL = 'http://127.0.0.1:5000'

    # User API endpoint
    SIGN_IN = API_PATH+API_VERSION+'/sign_in'
    SIGN_UP = API_PATH+API_VERSION+'/sign_up'
    USER_PROFILE = API_PATH+API_VERSION+'/profile/<string:username>'
    UPDATE_PROFILE = API_PATH+API_VERSION+'/update_profile/<string:username>'
    CHANGE_PASSWORD = API_PATH+API_VERSION+'/change_password/<string:username>'
    DELETE_ACCOUNT = API_PATH+API_VERSION+'/delete_account/<string:username>'

    # Movies API endpoint
    TRENDING_NOW = API_PATH+API_VERSION+'/trending_now/<string:username>'
    FETCH_MOVIES = API_PATH+API_VERSION+'/fetch_movies/<string:username>'
    ADD_MOVIE = API_PATH+API_VERSION+'/add_movie/<string:username>'
    SEARCH_MOVIE = API_PATH+API_VERSION+'/search_movie/<string:title>/<string:username>'
    DELETE_MOVIE = API_PATH+API_VERSION+'/delete_movie/<string:title>/<string:username>'
    ADD_TO_FAVOURITE = API_PATH+API_VERSION+'/add_to_favourite/<string:title>/<string:username>'
    FAVOURITE_MOVIES = API_PATH+API_VERSION+'/favourite_movies/<string:username>'
