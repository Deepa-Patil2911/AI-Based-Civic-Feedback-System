import joblib

model_path = r"models\department_classifier.pkl"

model = joblib.load(model_path)

test_text = "Streetlight not working, the area is dark and unsafe, residents feel scared."
result = model.predict([test_text])

print("Predicted Department:", result)