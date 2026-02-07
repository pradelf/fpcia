def score_model(model, x_train, y_train, x_test, y_test):
    print(model.score(x_train, y_train))
    print(model.score(x_test, y_test))
