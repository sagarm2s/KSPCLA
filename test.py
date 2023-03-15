import requests

BASE_URL = "http://127.0.0.1:5000/"

# print(requests.get(BASE_URL + "admin/dashboard"))
data = {
        "full_name": "chithanya",
        "content_subject": "computer science",
        "eligibility": "phd",
        "clg_street_name": "jawahar",
        "clg_state": "Andhra Pradesh",
        "clg_city": " Adilabad ",
        "clg_contry": "India",
        "clg_zip_code": "222222",
        "clg_code": "22",
        "emp_street_name": "jawahar",
        "emp_state": "Andhra Pradesh",
        "emp_city": " Adilabad ",
        "emp_contry": "India",
        "emp_zip_code": "333333",
        "emp_contact": "9000000000",
        "emp_alt_contact": "9000000009",
        "issue_date": "2023-03-11",
        "joining_date": "2023-03-11",
        "fee": "1",
        "transact_date": "2023-03-10",
        "reciept_num": "33hh44",
        "blood_grp": "A-"
    }

requests.post(BASE_URL + "register/success/9945938823", data=data)

# requests.delete(BASE_URL + "admin/dashboard/9945938823")


