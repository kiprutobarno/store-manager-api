from flask_restful import Resource


class LandingPage(Resource):
    def get(self):
        return "Welcome to Store Manager API "

