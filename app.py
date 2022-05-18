from flask import Flask, request, redirect
import numpy
import joblib

CAT_MODEL_PATH = "cat_ml/catboost_model.pkl"
CAT_SCALER_X_PATH = "cat_ml/scaler_x_cat.pkl"
CAT_SCALER_Y_PATH = "cat_ml/scaler_y_cat.pkl"

FOREST_MODEL_PATH = "forest_ml/forest_model.pkl"
FOREST_SCALER_X_PATH = "forest_ml/scaler_x_forest.pkl"
FOREST_SCALER_Y_PATH = "forest_ml/scaler_y_forest.pkl"

app = Flask(__name__)

@app.route('/predict_price', methods = ['GET'])
def predict():


    args = request.args
    cat = args.get('catboosted?(1/0)', default=-1, type=int)

    rooms = args.get('rooms', default=-1, type=int)
    area = args.get("area", default=-1, type=float)
    kitchen_area = args.get("kitchen_area", default=-1, type=float)
    ratio = args.get("area", default=-1, type=float)


    if cat == 1:

        model = joblib.load(CAT_MODEL_PATH)
        sc_x = joblib.load(CAT_SCALER_X_PATH)
        sc_y = joblib.load(CAT_SCALER_Y_PATH)

        x = numpy.array([rooms, area, ratio]).reshape(1, -1)
        x = sc_x.transform(x)
        result = model.predict(x)
        result = sc_y.inverse_transform(result.reshape(1, -1))

        return str(result[0][0])
    elif cat == 0:
        model2 = joblib.load(FOREST_MODEL_PATH)
        sc_x2 = joblib.load(FOREST_SCALER_X_PATH)
        sc_y2 = joblib.load(FOREST_SCALER_Y_PATH)

        x2 = numpy.array([rooms, area, kitchen_area, ratio]).reshape(1, -1)
        x2 = sc_x2.transform(x2)
        result2 = model2.predict(x2)
        result2 = sc_y2.inverse_transform(result2.reshape(1, -1))

        return str(result2[0][0])
    elif rooms == -1 or ratio == -1 or kitchen_area ==-1 or area == -1:
        return redirect('/error', code=302)
    elif cat != 0 or cat !=1 or cat != -1:
        return redirect('/badcat', code=302)
@app.route('/error', methods = ['POST', 'GET'])
def err():
    return """
    <h1>Not all data is present</h1>

    <iframe src="https://c.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif" width="853" height="480" frameborder="0" allowfullscreen></iframe>
    """
@app.route('/badcat')
def catbad():
    return """
    <h1>Cat got overpowered</h1>

    <iframe src="https://c.tenor.com/XbVvnGYv3aQAAAAC/cat-cats.gif" width="853" height="480" frameborder="0" allowfullscreen></iframe>
    """

@app.route('/form')
def form():
    return """<form action="/predict" method = "POST">
  <table style="border-collapse: collapse; width: 100%; height: 90px;" border="1">
    <tbody>
      <tr style="height: 18px;">
        <td style="width: 50%; height: 18px;">Catboost? 1 or 0</td>
        <td style="width: 50%; height: 18px;">
          <p><input name="cat" type="int" /></p>
        </td>
      </tr>
      <tr style="height: 18px;">
        <td style="width: 50%; height: 18px;">Rooms</td>
        <td style="width: 50%; height: 18px;"><p> <input type = "text" name = "rooms" /></p></td>
      </tr>
      <tr style="height: 18px;">
        <td style="width: 50%; height: 18px;">Area</td>
        <td style="width: 50%; height: 18px;"><p> <input type = "text" name = "area" /></p></td>
      </tr>
      <tr style="height: 18px;">
        <td style="width: 50%; height: 18px;">Kitchen area</td>
        <td style="width: 50%; height: 18px;"><p> <input type = "text" name = "kitchen_area" /></p></td>
      </tr>
      <tr style="height: 18px;">
        <td style="width: 50%; height: 18px;">Ratio</td>
        <td style="width: 50%; height: 18px;"><p> <input type = "text" name = "ratio" /></p></td>
      </tr>
    </tbody>
  </table>
  <p><input type = "submit" value = "Submit" /></p>
</form>"""








if __name__ == '__main__':
    app.run(debug=True, port=5444, host='0.0.0.0')
