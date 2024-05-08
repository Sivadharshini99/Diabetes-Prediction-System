from django.shortcuts import render
from django.shortcuts import render, redirect
import numpy as np
import joblib

model = joblib.load('C:/html prgm/Diabetes Prediction System/Deploy/app/RF.pkl')

# Create your views here.
def home(request):
    return render(request, "index.html")
    

def predict(request):
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features)]
        print(final_features)
        prediction = model.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(output)
        if output == 'No diabetes':
            output = 'No diabetes'
        else:
            output = 'Diabetes'

        return render(request, 'index.html', {"prediction_text":output})
        
