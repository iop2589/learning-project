import json;

data = """
  {
    "id":"01",
    "language":"Java",
    "edition":"third",
    "author":"Herbert Schildt",
    "history":
    [
      {
        "date":"2015-03-11",
        "item":"iphone"
      },
      {
        "date":"2016-03-11",
        "item":"android"
      }
    ]
  }
""";

json_data = json.loads(data);

print(json_data);