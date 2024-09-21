from flask import Flask
from flasgger import Swagger
from blueprints.auth import auth
from blueprints.dashboard import dashboard
from blueprints.tracking import tracking


app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(auth, url_prefix='/api/auth')
app.register_blueprint(tracking, url_prefix='/api/tracking')
app.register_blueprint(dashboard, url_prefix='/api/dashboard')

if __name__ == '__main__':
    app.run(debug=True)