def config_package():
    with open('config.py', 'w') as fichier_config:
        fichier_config.write(f"""import logging
import os
from requests.auth import HTTPBasicAuth \n
main_directory = os.path.dirname(os.path.abspath(__file__))

username = "BillGates" 
#Api token de jira 
api_token = "TATT3xFfGF0nqgTV-RGN17B9CmizmQD0Mmr5ZY-pU0t8TjTzz0lyX0MNJ0XoNdKNy_t4eq9Is3Gw51Mta-kHF0XrEjKUANWzJM1XpRqS_-wSssC"

auth = HTTPBasicAuth(username, api_token)

workflow_database_file = "sqlite:///" + main_directory + "/database/worflow_bd.db"

jira_url_base = "https://example.atlassian.net/"
project_key = "90009"
key_issue_type = "10005"
s1_id_in_jira = "customfield_10054"

statusesS1 = ["status1", "status2", "status3", "status4"]

module_to_use = "synch2jira.issue_S3"
class_to_use = "IssueImplementationS3"
                             
jql_query = 'project = KAN'

rate_column = 'Qualifications'
""")

