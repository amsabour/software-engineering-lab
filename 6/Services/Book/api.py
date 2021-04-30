from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort, marshal, fields
import jwt

# Initialize Flask
app = Flask(__name__)
api = Api(app)

# Dictionary of books
books = {}
categories = {}
# Books auto incrementor
auto_index = 0

book_fields = {
    "title": fields.String,
    "author": fields.String,
    "category": fields.String
}


class BookRecord(Resource):
    # Initialize Flask's Request Parser and add arguments as in an expected request
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("title", type=str, location="json")
        self.reqparse.add_argument("category", type=str, location="json")
        self.reqparse.add_argument("author", type=str, location="json")
        self.reqparse.add_argument("token", type=str, location="headers")

        super(BookRecord, self).__init__()

    # GET - Returns a single book matching the ID
    def get(self, book_id):
        if book_id in books:
            book = books[book_id]
        else:
            abort(404)  # The book hasn't been found. So we should sent a 404 answer.
        # Otherwise the book should be returned.
        return {"book": marshal(book, book_fields)}
        # We assumed normal users can view books as well.

    # PUT - Given a book id -> update the book
    def put(self, book_id):
        args = self.reqparse.parse_args()
        if args["token"] is None:
            abort(401)  # The user is unauthenticated.
        if jwt.decode(args["token"], options={"verify_signature": False})["username"] != "admin":
            abort(401)  # The user is not the admin.

        if book_id in books:
            book = books[book_id]
        else:
            abort(404)  # The book hasn't been found. So we should sent a 404 answer.

        # Loop through all the passed agruments
        args = self.reqparse.parse_args()
        if 'category' in args:
            if book['category'] is not None:
                categories[book['category']].remove(book_id)
            if args['category'] in categories:
                categories[args['category']].append(book_id)
            else:
                categories[args['category']] = [book_id]
            
            
        for key, value in args.items():
            if value is not None:
                # if the passed value is not null, do the update.
                book[key] = value
                # TODO is the update complete?
        return {"book": marshal(book, book_fields)}
    
    
    # DELETE - Given a book id -> delete the book
    def delete(self, book_id):
        args = self.reqparse.parse_args()
        if args["token"] is None:
            abort(401)  # The user is unauthenticated.
        if jwt.decode(args["token"], options={"verify_signature": False})["username"] != "admin":
            abort(401)  # The user is not the admin.
            
        if book_id in books:
            book = books[book_id]
        else:
            abort(404)  # The book hasn't been found. So we should sent a 404 answer.
        
        if book['category'] is not None:
            categories[book['category']].remove(book_id)
            
        del books[book_id]
        return {"message": "Deletion was successful."}


class BookList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("title", type=str, required=True, location="json")
        self.reqparse.add_argument("category", type=str, location="json")
        self.reqparse.add_argument("author", type=str, location="json")
        self.reqparse.add_argument("token", type=str, location="headers")

    # Create a new book.
    def post(self):
        global auto_index
        args = self.reqparse.parse_args()

        if args["token"] is None:
            abort(401)  # The user is unauthenticated.

        if jwt.decode(args["token"], options={"verify_signature": False})["username"] != "admin":
            abort(401)  # The user is not the admin.
            
        
        book = {
            "title": args.get("title"),
            "category": args.get("category", None),
            "author": args.get("author", ""),
        }

        books[auto_index] = book
        if book['category'] is not None:
            if book['category'] in categories:
                categories[book['category']].append(auto_index)
            else:
                categories[book['category']] = [auto_index]
        auto_index += 1
        return {"message": "Book Created."}, 201


class BookSearch(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("title", type=str, location="json")
        self.reqparse.add_argument("category", type=str, location="json")
        
    # Search for a book
    def post(self):
        args = self.reqparse.parse_args()
        title = args.get("title", None)
        cat = args.get("category", None)
        if title is None and cat is None:
            return {"message": "At least one of the title or category should be provided."}, 400
        
        if cat is not None:
            answer_list = []
            if cat not in categories:
                return [], 200
            for book_id in categories[cat]:
                if title is None or title in books[book_id]["title"]:
                    answer_list.append((book_id, books[book_id]["title"]))
            return answer_list, 200
        
        answer_list = []
        for k, v in books.items():
            if title in v['title']:
                answer_list.append((k, v['title']))
        return answer_list, 200
        



api.add_resource(BookList, "/books")
api.add_resource(BookRecord, "/books/<int:book_id>")
api.add_resource(BookSearch, "/search")


@app.route('/is_alive', methods=['GET'])
def is_alive():
    return jsonify({'message': 'Service is alive'}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
    