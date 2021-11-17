import csv, os, json
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
    #print(dataset.get_bmi_deviation())
    #print(dataset.get_bmi_deviation())
    #with open('dvi.txt', 'w') as result_file:
      #json.dump(dataset.get_bmi_deviation(), result_file)
      #result_file.write(str(dataset.get_bmi_deviation()))

      #result_file.write(str(dataset.get_bmi_influence(dataset.prepare_bmi_deviation())))

    #print(dataset.get_bmi_influence(dataset.sort_all_except('bmi')))
    #print(dataset.get_avg_cost_per_value('bmi'))
    #print(dataset.get_age_influence(dataset.sort_all_except('age')))
    #print(dataset.get_avg_cost_per_value('age'))
    #print(dataset.get_smoker_influence(dataset.sort_all_except('smoker')))
    print(dataset.get_avg_cost_per_value('sex'))
    #print(dataset.get_avg_cost_per_value('sex'))