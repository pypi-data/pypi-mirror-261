from mnn import dataset, network
from mnn.utils import mae_loss, list_avg, plus_minus
from random import choice, random, uniform

class trainer:
  """
  class used to train the network
  """
  def __init__(self, net:network, epochs:int, data:dataset, train_func=None,learn_rate=0.1):
    self.net = net
    self.epochs = epochs
    self.data = data
    self.learn_rate = learn_rate
    self.train_func = train_func
    self.debug = True

  def get_full_data_loss(self):
    """
    returns the loss of the full dataset fiven
    """
    losses = []
    for i,o in zip(self.data.inps, self.data.outs):
      losses.append(mae_loss(self.net.run(i),o))
    return list_avg(losses)

  def get_net(self):
    """
    returns the network
    """
    return self.net

  def print(self,string):
    if self.debug is True:
      print(string)

  def start_train(self):
    """
    starts training the network
    """
    for epoch in range(self.epochs):
      if self.train_func is not None:
        self.train_func(self.net, epoch, self)
      weights = self.net.get_weights()
      temp = {}
      old_loss = self.get_full_data_loss()
      for weight in weights:
        old_weight = weight.weight
        t = plus_minus(old_weight, self.learn_rate)
        weight.weight = t
        new_loss = self.get_full_data_loss()
        weight.weight = old_weight
        dif = old_loss - new_loss
        temp[dif] = (weight,t)
      temp = dict(sorted(temp.items(),reverse=True))
      _, t = next(iter(temp.items()))
      best, new = t
      best.weight = new
    