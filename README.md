# RTA homework – production env

## flask application with model response. - iris data and Perceptron model

Please navigate to the right path and run the app

```
python app.py
```

Generate predictions via URL

```
http://127.0.0.1:5000/predict/?sl=60.1&pl=0.3
```

Expect to receive JSON response, For example:

```
{
  "features": "[[60.1, 0.3]]", 
  "predicted_class": "-1.0"
}
```

