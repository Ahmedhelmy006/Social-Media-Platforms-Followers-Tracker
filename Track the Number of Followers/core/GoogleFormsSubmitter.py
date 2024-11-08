import requests

class GoogleFormsSubmitter:
    def __init__(self, form_url, form_fields):

        self.form_url = form_url
        self.form_fields = form_fields

    def submit_data(self, data):

        form_data = {self.form_fields[key]: value for key, value in data.items() if key in self.form_fields}
        
        response = requests.post(self.form_url, data=form_data)
        if response.status_code == 200:
            print("Data successfully submitted to Google Form!")
        else:
            print(f"Failed to submit data. Status code: {response.status_code}")