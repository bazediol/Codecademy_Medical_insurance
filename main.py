import csv, os
from Insurance_classes import Insurance, Dataset
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
    print(dataset.get_summary_by_filter('smoker'))
    print(dataset.get_cost_difference_somokers_in_average())
