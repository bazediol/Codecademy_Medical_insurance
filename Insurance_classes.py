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

    def addInsurance(self, insurance):
        self.insurance_list.append(insurance)
        self.total_charges = self.get_total_charges()

    def __repr__(self) -> str:
        representation = ''
        for insurance in self.insurance_list:
            representation += '{}\n'.format(insurance)
        return representation
    
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






        

