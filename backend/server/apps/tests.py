from django.test import TestCase

from apps.ml.declarations_classifier.random_forest import RandomForestClassifier

class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {
            "FIPS": "22037",
            "MaxPreceipitation": '2" to 4"',
            "WindSwathRadii": "39",
            "CountyOverlap": 1.93497637,
            "Value_1": "NA",
            "Value_2": "NA",
            "Value_3": "NA",
            "Value_4": "NA",
            "Value_5": "NA",
            "Value_7": "NA",
            "Stormsurge_Area": "NA",
            "SOCIAL": 0.670372594,
            "INFRASTRUCTURE": 0.126975254,
            "COMCAPITAL": 0.3971855967,
            "INSTITUTION": 0.520448794,
            "ENVIRONMENT": 0.567594855,
            "BRIC_SCORE": 2.724523219,
            "Unclassified": 0,
            "Open_Water": 12596400,
            "Perrennial_Snow_Ice": 0,
            "Developed_Open_Space": 56436300,
            "Developed_Low_Intensity": 5189400,
            "Developed_Medium_Intensity": 1373400,
            "Developed_High_Intensity": 328500,
            "Barren_Land": 6065100,
            "Deciduous_Forest": 49849200, 
            "Evergreen_Forest": 345513600,
            "Mixed_Forest": 153090000,
            "Shrub_Scrub": 65836800,
            "Herbaceous": 23125500,
            "Hay_Pasture": 237951900,
            "Cultivated_Crops": 4266900,
            "Woody_Wetlands": 215620200,
            "Emergent_Herbaceous_Wetlands": 3215700,
            "Population": 19412,
        }

        rf_algo = RandomForestClassifier()

        response = rf_algo.compute_prediction(input_data)

        self.assertEqual('OK', response['status'])

        self.assertTrue('label' in response)

        self.assertEqual('Yes', response['label'])