import joblib
from flask import Flask, render_template,request,redirect


# creating flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    N = float(request.form['Nitrogen'])
    P = float(request.form['Phosporus'])
    K = float(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    pH = float(request.form['pH'])
    rainfall = float(request.form['Rainfall'])

    feature_list = [N, P, K, temp, humidity, pH, rainfall]

    if pH>0 and pH<=14 and temp<100 and humidity>0:
        joblib.load('finalized_model','r')
        model=joblib.load(open('finalized_model','rb'))
        arr=[feature_list]
        res= model.predict(arr)
        return render_template('index.html',prediction=res[0])

    
    else:
        return "Sorry, we could not determine the best crop to be cultivated with the provided data."
    



# python main
if __name__ == "__main__":
    app.run(debug=True)
