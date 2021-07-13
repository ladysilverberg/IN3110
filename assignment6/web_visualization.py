import matplotlib.pyplot as plt
from flask import Flask
from flask import render_template
from flask import request
from visualize import visualize
from fitting import fit
from fitting import calculate_score
from fitting import create_classifier
from data import read_datasets

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Methods
methods = ["SVC", "KNN", "GaussianNB"]

# Initialize Datasets and Features
data, training_set, validation_set = read_datasets("diabetes.csv")
data.replace(["pos", "neg"], [1, 0], inplace=True)
training_set.replace(["pos", "neg"], [1, 0], inplace=True)
validation_set.replace(["pos", "neg"], [1, 0], inplace=True)
features = []
for col in data.columns:
    col = col.capitalize()
    features.append(col)
features.pop(0)

# Process, Visualize and Save Data as Image
def process_data(method, features):
    classifier = create_classifier(method)
    visualize(classifier, training_set, data, "diabetes", features)
    verification_score = calculate_score(classifier, validation_set, features, "diabetes")
    training_score = calculate_score(classifier, training_set, features, "diabetes")
    plt.savefig('static/img/visualize.png')
    plt.clf()
    return verification_score, training_score

@app.route("/")
def visualize_data():
    verification_score, training_score = process_data("svc", ["age", "pregnant"])
    return render_template('visualization.html', v_score=verification_score, t_score=training_score,
    methods=methods, features=features, cur_method="SVC", cur_feature_x="Age", cur_feature_y="Pregnant")

@app.route('/', methods=["POST"])
def post_visualize_data():
    # Process Post Data
    method = request.form["method"]
    feature_x = request.form["featurex"]
    feature_y = request.form["featurey"]
    feat = [feature_x.lower(), feature_y.lower()]

    verification_score, training_score = process_data(method.lower(), feat)
    return render_template('visualization.html', v_score=verification_score, t_score=training_score,
    methods=methods, features=features, cur_method=method, cur_feature_x=feature_x, cur_feature_y=feature_y)

# Cache Busting
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

if __name__ == "__main__":
    app.run(port=1337)
