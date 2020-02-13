from app import app

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
    # from gevent.pywsgi import WSGIServer
    # http_server = WSGIServer(('223.24.170.201'), app)
    # http_server.serve_forever()