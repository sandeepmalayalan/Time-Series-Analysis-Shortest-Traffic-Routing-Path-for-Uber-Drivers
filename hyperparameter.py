#Hyperparameter tuning for lstm model
def run1(run_dir, hparams,session):
  with tf.summary.create_file_writer(run_dir).as_default():
    hp.hparams(hparams)
    score,pred1 = model(trainx,trainy,run_dir,hparams)
    tf.summary.scalar(METRIC_ACCURACY, score, step=session)
    return score,pred1
session=0
num_units_list = [100,200,300] # Number of units in the dense layer
dropout_rate_list = [0.1, 0.2,0.3] # Dropout rate
optimizer_list = ['adam']
val={}
for num_units in num_units_list:
  for dropout_rate in dropout_rate_list:
    for optimizer in optimizer_list:
      para= {'num_units': num_units, 'dropout': dropout_rate, 'optimizer': optimizer}
      print('Running training session', str(session))
      print(para)
      score,pred1=run1('logs/hparam/' + str(session), para,session)
      val[score]=pred1
      session += 1
