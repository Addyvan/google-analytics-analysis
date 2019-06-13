from createService import initialize_analyticsreporting
import pandas as pd

class gcga_v2:

    def __init__(self):
        self.analytics = initialize_analyticsreporting()
        self.platforms =  {
            "gccollab": "ga:127642570",
            "gcconnex": "ga:55943097",
            "gcpedia": "ga:39673253"
        }
    
    def example_load_times():
        return analytics.reports().batchGet(
            body={
            'reportRequests': [
            {
                'viewId': self.platforms["gccollab"],
                'dateRanges': [{'startDate': '2019-05-01', 'endDate': '2019-05-31'}],
                'metrics': [{'expression': 'ga:pageLoadTime'}],
                'dimensions': [
                    {'name': 'ga:pagePathLevel1'},
                    {'name': 'ga:pagePathLevel2'},
                    {'name': 'ga:pagePathLevel3'},
                    {'name': 'ga:pagePathLevel4'},
                    {'name': 'ga:dateHourMinute'},
                    {'name': 'ga:country'}, 
                    {'name': 'ga:city'}, 
                    {'name': 'ga:browser'}]
            }]
            }
        ).execute()
    
    def create_dataframe(report):



if __name__ == "__main__":
    gcga = gcga_v2()