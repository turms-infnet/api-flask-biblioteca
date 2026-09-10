from app import app

config = app.config

debug = config.get('DEBUG', False)

if __name__ == "__main__":
    app.run(debug=debug)