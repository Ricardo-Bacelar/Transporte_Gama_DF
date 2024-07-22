from app import app

@app.route('/')
@app.route('/index'):
    return "Hello Word!"
