#LSTM model prediction 
from keras.models import Sequential
from keras.layers import Dense,LSTM,Dropout
def model(trainx,trainy,run_dir,params):
  n_timesteps, n_features, n_outputs = trainx.shape[1], trainx.shape[2], trainx.shape[1]
  model1 = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(200, activation='relu', input_shape=(n_timesteps, n_features)),
    tf.keras.layers.Dense(params["num_units"], activation='relu'),
    tf.keras.layers.Dropout(params["dropout"]),
    tf.keras.layers.Dense(24),
  ])
  logdir = run_dir + datetime.now().strftime("%Y%m%d-%H%M%S")
  model1.compile(loss='mse', optimizer=params["optimizer"])
  model1.fit(trainx, trainy, epochs=50, batch_size=16, verbose=1,validation_data=(testx,testy),callbacks=[tf.keras.callbacks.TensorBoard(logdir)])
  
  data = array(trainx)
  data = data.reshape((data.shape[0]*data.shape[1], data.shape[2]))
  # retrieve last observations for input data
  input1 = data[-24:, 0]
  input1 = input1.reshape((1,24,1))
  yhat = model1.predict(input1)
  pred1 = yhat[0]
  print(model1.summary())
  score=sqrt(mean_squared_error(test,pred1))
  return score,pred1
