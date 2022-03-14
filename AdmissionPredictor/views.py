from django.shortcuts import render

def index(req):
    context = {
        
    }
    return render(req, "AdmissionPredictor/admission.html", context=context)

def getData(req):
    return render(req, "AdmissionPredictor/getData.html")

def predict(req):
    return render(req, "AdmissionPredictor/predict.html")

def signIn(req):
    return render(req, "AdmissionPredictor/signIn.html")

def signUp(req):
    return render(req, "AdmissionPredictor/signUp.html")