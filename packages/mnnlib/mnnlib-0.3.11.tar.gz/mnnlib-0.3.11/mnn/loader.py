from mnn.dataset import dataset
import csv
import logging


def load_csv(file_name:str):
  """
  DEPRECATED DO NOT USE!!!!
  """
  raise DeprecationWarning("This function is deprecated and will be removed in the future. Use csvreader.csvreader instead.")
  data = dataset()
  with open(file_name, 'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=";")
    t = 0
    for row in reader:
      if t != 0:
        try:
          inp = [
              round(int(row[30]) / 20) * 100,
              round(int(row[31]) / 20) * 100
          ]
          out = [round(int(row[32]) / 20) * 100]
          data.add_data(inp, out)
        except:
          pass
      t += 1
  return data
