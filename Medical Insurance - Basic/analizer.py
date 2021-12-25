import csv

class Analizer:
    def __init__(self, dataset):
        self.dataset = dataset

    def age_average(self):
         with open(self.dataset) as insurances:
            insurances_df = csv.DictReader(insurances)
            sum = 0
            quantity = 0
            for row in insurances_df:
                sum += int(row["age"])
                quantity +=1
            average = round(sum/quantity)
            return average

    def age_count(self, top=False):
        with open(self.dataset) as insurances:
            insurances_df = csv.DictReader(insurances)
            age = {}
            for row in insurances_df:
                if int(row["age"]) in age:
                    age[int(row["age"])]+=1
                elif int(row["age"]) not in age:
                    age[int(row["age"])] = 1

        keys = [i for i in age]
        keys.sort()
        final_result = {}
        for i in keys:
            final_result[i] = age[i]

        if top:
            max_quantity = 0
            key = 0
            for i in age:
                if age[i] > max_quantity:
                    max_quantity = age[i]
                    key = i
            return {
                "Age": key,
                "Ocurrences": max_quantity,
            }

        return final_result

    def smoker_count(self):
        with open(self.dataset) as insurances:
            insurances_df = csv.DictReader(insurances)
            smoker = {}
            for row in insurances_df:
                if row["smoker"] in smoker:
                    smoker[row["smoker"]]+=1
                elif row["sex"] not in smoker:
                    smoker[row["smoker"]] = 1

        return smoker

    def smoker_percent(self, chose=None):
        with open(self.dataset) as insurances:
            insurances_df = csv.DictReader(insurances)
            quantity = 0
            female = 0
            male = 0
            for row in insurances_df:
                quantity+=1
                if row["smoker"] == "yes":
                    female+=1
                elif row["smoker"] == "no":
                    male+=1
            smoker_percent = round(female/quantity, 2)
            no_smoker_percent = round(male/quantity, 2)

            if chose == None:
                message = {
                    "Smoker": smoker_percent,
                    "No Smoker": no_smoker_percent,
                }
            elif chose == 1:
                message = smoker_percent
            elif chose == 0:
                message = no_smoker_percent

        return message

    def sex_count(self):
        with open(self.dataset) as insurances:
            insurances_df = csv.DictReader(insurances)
            sex = {}
            for row in insurances_df:
                if row["sex"] in sex:
                    sex[row["sex"]]+=1
                elif row["sex"] not in sex:
                    sex[row["sex"]] = 1

        return sex

    def sex_percent(self, chose=None):
        with open(self.dataset) as insurances:
            insurances_df = csv.DictReader(insurances)
            quantity = 0
            female = 0
            male = 0
            for row in insurances_df:
                quantity+=1
                if row["sex"] == "female":
                    female+=1
                elif row["sex"] == "male":
                    male+=1
            female_percent = round(female/quantity, 2)
            male_percent = round(male/quantity, 2)

            if chose == None:
                message = {
                    "Female": female_percent,
                    "Male": male_percent,
                }
            elif chose == 1:
                message = female_percent
            elif chose == 0:
                message = male_percent

        return message

    def locations(self):
        with open(self.dataset) as insurances:
            insurances_df = csv.DictReader(insurances)
            locations = {}
            for row in insurances_df:
                if row["region"] in locations:
                    locations[row["region"]]+=1
                elif row["region"] not in locations:
                    locations[row["region"]] = 1

        return locations

    def __repr__(self):
        obj = \
            f"""
            Average Age: {self.age_average()}
            Smoker Percent: {self.smoker_percent()}
            Sex Percent: {self.sex_percent()}
            Locations: {self.locations()}
            """

        return str(obj)