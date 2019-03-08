from flask import Flask, request, jsonify
#from flask_sslify import SSLify

app = Flask(__name__)
#sslify = SSLify(app)

@app.route('/webhook', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':

        data = request.get_json()
        API_KEY = data['entry'][0]['messaging'][0]['message'] #Key for Verify 
        hubverify = 'wadev12345'
      
       
        
        if hubverify == API_KEY : # Check data verify and mode
            print('WEBHOOK_VERIFIED')
            return "Wecome  "+ data['UserName'][0]['User'][0]['Name']  , 200 # Return 'Wecome User''

        
        else:
            return 'You Wrong Something' , 200

    elif request.method == 'POST':
        
        data = request.get_json()
        
        
        if data['object'] == "page":
            print(data['entry'][0]['messaging'][0]['message'])
            print(data['entry'])

            return data['UserName'][0]['User'][0]['Name'] +"  "+data['entry'][0]['messaging'][1]['message'] , 200


    elif request.method == 'GET':
        return 'GET' , 200

    else:
        return 'Forbidden' , 403

@app.route('/', methods=['GET','POST','PUT','DELETE'])
def index():
    if request.method == 'GET' or request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
        return 'Service Not Found', 404

if __name__ == '__main__':
    app.run()