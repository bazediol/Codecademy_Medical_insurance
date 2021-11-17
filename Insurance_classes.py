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
        self.total_charges = 0
        self.age_values = []
        self.sex_values = []
        self.bmi_values = []
        self.smoker_values = []
        self.children_values = []
        self.region_values = []

    def addInsurance(self, insurance):
        self.insurance_list.append(insurance)
        self.total_charges = self.get_total_charges()
        self.update_values(insurance)


    def __repr__(self) -> str:
        representation = ''
        for insurance in self.insurance_list:
            representation += '{}\n'.format(insurance)
        return representation

    def update_values(self, insurance):
        if insurance.age not in self.age_values:
            self.age_values.append(insurance.age)
            self.age_values.sort()
        if insurance.sex not in self.sex_values:
            self.sex_values.append(insurance.sex)
            self.sex_values.sort()
        if insurance.bmi not in self.bmi_values:
            self.bmi_values.append(insurance.bmi)
            self.bmi_values.sort()
        if insurance.smoker not in self.smoker_values:
            self.smoker_values.append(insurance.smoker)
            self.smoker_values.sort()
        if insurance.children not in self.children_values:
            self.children_values.append(insurance.children)
            self.children_values.sort()
        if insurance.region not in self.region_values:
            self.region_values.append(insurance.region)
            self.region_values.sort()
        
    
    def get_average_age(self):
        total_age = 0
        for insrurance in self.insurance_list:
            total_age += int(insrurance.age)
        return total_age/len(self.insurance_list)

    def get_coverage(self):
        coverage = {}
        for insurance in self.insurance_list:
            if insurance.region in coverage:
                coverage[insurance.region] += 1
            else:
                coverage[insurance.region] = 1
        return coverage

    def get_dataset_len(self):
        return len(self.insurance_list)

    def get_insurance_by_filter(self, filter, value):
        result = []
        for insurance in self.insurance_list:
            if getattr(insurance, filter) == value:
                result.append(insurance)
        return result

    def get_insurance_dataset_by_filter(self, filter, value):
        new_dataset = Dataset()
        for insurance in self.insurance_list:
            if getattr(insurance, filter) == value:
                new_dataset.addInsurance(insurance)
        return new_dataset

    def get_insurance_count_by_filter(self, filter, value):
        return len(self.get_insurance_by_filter(filter, value))

    def get_available_values_by_filter(self, filter):
        available_values = []
        for insurance in self.insurance_list:
            if (getattr(insurance, filter)) not in available_values:
                available_values.append(getattr(insurance, filter))
        return list(set(available_values))

    def get_summary_by_filter(self, filter):
        average_cost = {}
        #prepare result dict
        for value in self.get_available_values_by_filter(filter):
            total_charges = 0
            filtered_list = self.get_insurance_by_filter(filter, value)
            for insurance in filtered_list:
                total_charges += float(insurance.charges)
            average_cost[value] = {}
            average_cost[value]['average_cost'] = total_charges/len(filtered_list)
            average_cost[value]['percentage'] = total_charges/self.total_charges * 100
            average_cost['available_values'] = self.get_available_values_by_filter(filter)
        return average_cost

    def get_total_charges(self):
        total_charges = 0
        if len(self.insurance_list) >= 1:
            for insurance in self.insurance_list:
                total_charges += float(insurance.charges)
        return total_charges

    def get_average_age_for_patients_with_childrens (self):
        patients_with_childrens = []
        values_list = self.get_available_values_by_filter('children')
        for value in values_list:
            if value != 0:
                patients_with_childrens += self.get_insurance_by_filter('children', value)
        total_age = 0
        for insurance in patients_with_childrens:
            total_age += int(insurance.age)
        return total_age/len(patients_with_childrens)
        
    def get_cost_difference_somokers_in_average(self):
        summary = self.get_summary_by_filter('smoker')
        diff = summary['no']['average_cost'] - summary['yes']['average_cost']
        return 'In average nonsmokers charges is {} less'.format(diff)
    def split_to_datasets_by_param(self, param):
        map_dict = {'age': 'age_values',
                'sex': 'sex_values',
                'bmi': 'bmi_values',
                'children': 'children_values',
                'smoker': 'smoker_values',
                'region': 'region_values',
                }
        dataset_dict = {}
        for value in getattr(self, map_dict[param]):
            same_age_dataset = Dataset()
            same_age_dataset = self.get_insurance_dataset_by_filter(param, value)
            dataset_dict[value] = same_age_dataset
        return dataset_dict
              
    def sort_all_except(self, param):
        params_keys = {'age': ['sex', 'bmi', 'children', 'smoker', 'region'],
                       'sex': ['age', 'bmi', 'children', 'smoker', 'region'],
                       'bmi': ['sex', 'age', 'children', 'smoker', 'region'],
                       'children': ['sex', 'bmi', 'age', 'smoker', 'region'],
                       'smoker': ['sex', 'bmi', 'children', 'age', 'region'],
                       'region': ['sex', 'bmi', 'children', 'smoker', 'age']}
        result_dict = {}
        for value1_key, dataset1 in self.split_to_datasets_by_param(params_keys[param][0]).items():
            result_dict[value1_key] = {}
            for value2_key, dataset2 in dataset1.split_to_datasets_by_param(params_keys[param][1]).items():
                result_dict[value1_key][value2_key] = {}
                for value3_key, dataset3 in dataset2.split_to_datasets_by_param(params_keys[param][2]).items():
                    result_dict[value1_key][value2_key][value3_key] = {}
                    for value4_key, dataset4 in dataset3.split_to_datasets_by_param(params_keys[param][3]).items():
                        result_dict[value1_key][value2_key][value3_key][value4_key] = {}
                        for value5_key, dataset5 in dataset4.split_to_datasets_by_param(params_keys[param][4]).items():
                            result_dict[value1_key][value2_key][value3_key][value4_key][value5_key] = dataset5
        return result_dict
    def get_avg_cost_per_value(self, category):
        category_type = {
            'age': 'number',
            'sex': 'dual',
            'bmi': 'number',
            'children': 'number',
            'smoker': 'dual',
            'region': 'multy_value'
        }
        current_category_type = category_type[category]
        sorted_dataset = self.sort_all_except(category)
        charge_per_value = []
        more_expensive_value = ''
        for level0_value in sorted_dataset.values():
            for level1_value in level0_value.values():
                for level2_value in level1_value.values():
                    for level3_value in level2_value.values():
                        for level4_value in level3_value.values():
                            current_dataset = level4_value
                            if current_dataset.get_dataset_len() > 1:
                                if current_category_type == 'number':
                                    for i in range (0, current_dataset.get_dataset_len()-1):
                                        bmi_delt = abs(float(getattr(current_dataset[i], category)) - float(getattr(current_dataset[i+1], category)))
                                        if bmi_delt == 0:
                                            continue
                                        charge_delt = abs(float(current_dataset[i].charges) - float(current_dataset[i+1].charges))
                                        avg = charge_delt/bmi_delt
                                        charge_per_value.append(avg)
                                if current_category_type == 'dual' or current_category_type == 'multy_value':
                                    attr_name = category + '_values'
                                    summary_dict = {}
                                    available_values = getattr(self, attr_name)
                                    for value in available_values:
                                        summary_dict[value] = {'Total': 0, 'Counter': 0, 'Avg': 0, 'Name': value}
                                    for insurance in current_dataset:
                                        summary_dict[getattr(insurance, category)]['Total'] += float(getattr(insurance, 'charges'))
                                        summary_dict[getattr(insurance, category)]['Counter'] +=1
                                    if summary_dict[available_values[0]]['Counter'] == 0 or summary_dict[available_values[1]]['Counter'] == 0:
                                        continue
                                    for dict in summary_dict.values():
                                        if dict['Counter'] > 0:
                                            dict['Avg']= dict['Total']/dict['Counter']
                                    charge_per_value.append(abs(summary_dict[available_values[0]]['Avg'] - summary_dict[available_values[1]]['Avg']))
                                    if summary_dict[available_values[0]]['Avg'] > summary_dict[available_values[1]]['Avg']:
                                        more_expensive_value = summary_dict[available_values[0]]['Name']
                                    else:
                                        more_expensive_value = summary_dict[available_values[1]]['Name']
        if current_category_type == 'number':
            avg_value_cost = sum(charge_per_value)/len(charge_per_value)
            return avg_value_cost
        if current_category_type == 'dual':
            avg_value_cost = sum(charge_per_value)/len(charge_per_value)
            return 'Charges for {} more expensive in avarage for {} $'.format(more_expensive_value, avg_value_cost)
    def get_insurance_by_index(self, index):
        return self.insurance_list[index]
    def __iter__ (self):
        for insurance in self.insurance_list:
            yield insurance
    def __getitem__(self, index):
        return self.insurance_list[index]
