import csv, os
#test
class Insurance:
    def __init__(self, age, sex, bmi, children, smoker, region, charges):
      self.age = age
      self.sex = sex
      self.bmi = bmi
      self.children = children
      self.smoker = smoker
      self.region = region
      self.charges = charges

    def __repr__(self):
        return 'Age {}, Sex {}, BMI {}, Children {}, Smoker {}, Region {}, Charges {}'.format(self.age, self.sex, self.bmi, self.children, self.smoker, self.region, self.charges)

class Dataset:

    def __init__ (self):
        self.insurance_list = []

    def addInsurance(self, insurance):
        self.insurance_list.append(insurance)

    def __repr__(self) -> str:
        representation = ''
        for insurance in self.insurance_list:
            representation += '{}\n'.format(insurance)
        return representation

def convert_file_to_dataset():
  file_location = os.getcwd() + '\insurance.csv'
  dataset = Dataset()
  with open(file_location) as raw_data:
      raw_data_reader = csv.DictReader(raw_data)
      for row in raw_data_reader:
          single_insurance = Insurance(row['age'],
          row['sex'],
          row['bmi'],
          row['children'],
          row['smoker'],
          row['region'],
          row['charges'])
          #print(single_insurance)
          dataset.addInsurance(single_insurance)
  return dataset

if __name__ == "__main__":
    dataset = Dataset()
    dataset = convert_file_to_dataset()
    print(dataset)

    