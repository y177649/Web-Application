import stripe
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Stripeの秘密キーを設定
stripe.api_key = 'sk_test_yourSecretKeyHere'

@app.route('/')
def index():
    return 'Welcome to the Online Shop!'

@app.route('/pay', methods=['POST'])
def pay():
    try:
        token = request.json['stripeToken']
        amount = 500  # 請求額を設定

        customer = stripe.Customer.create(
            email='customer@example.com',
            source=token
        )

        charge = stripe.Charge.create(
            customer=customer.id,
            amount=amount,
            currency='jpy',
            description='商品説明'
        )
        return jsonify(charge)
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/new-page')
def new_page():
    return render_template('new_page.html')

if __name__ == "__main__":
    app.run(debug=True)
