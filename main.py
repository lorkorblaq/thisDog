from website import create_app
import secrets
app = create_app()
auth_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = f"{auth_key}"

if __name__ == "__main__":
    app.run(port=8080, debug=True)