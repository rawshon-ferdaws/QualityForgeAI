class Endpoints:

    USERS = "/users"
    POSTS = "/posts"

    @staticmethod
    def user(user_id):
        return f"/users/{user_id}"

    @staticmethod
    def post(post_id):
        return f"/posts/{post_id}"
