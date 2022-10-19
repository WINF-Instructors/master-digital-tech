import logging
from requests.auth import HTTPBasicAuth
import requests
import json
from api.config.credentials import credentials

from retrying import retry

LOG = logging.getLogger(__name__)

def retry_if_connection_error(exception):
    """Return True if we should retry (in this case when it's an IOError), False otherwise"""
    return isinstance(exception, ConnectionError)


@retry(wait_random_min=1000, wait_random_max=2000, stop_max_attempt_number=5, retry_on_exception=retry_if_connection_error)
def create_ticket(reason,desc):
    user=credentials.JIRA_USER
    password=credentials.JIRA_PASSWORD
    url="https://jira.net/rest/api/2/issue"
    headers={'Content-Type': 'application/json'}
    projectID="18149"
    LOG.info("Creating a ticket at some JIRA board...")
    
    payload={
        "fields":{
            "project": {
                "id": projectID
            },
            "summary": reason, 
            "description": desc,
            "issuetype": {
                "id": "3"
            }
            
        }
    }
    
    response=requests.post(url, headers=headers, data=json.dumps(payload),auth=HTTPBasicAuth(user, password))
    if response.status_code not in [200, 201, 202]:
        LOG.warning(response.reason)
        return (0,0)
    else:
        LOG.info("Ticket successfully created.")
        id=json.loads(response.text)["id"]
        key=json.loads(response.text)["key"]
        return key, id


@retry(wait_random_min=1000, wait_random_max=2000, stop_max_attempt_number=5, retry_on_exception=retry_if_connection_error)
def attach_file_to_ticket(filename,id):
    user=credentials.JIRA_USER
    password=credentials.JIRA_PASSWORD
    headers = {
        'X-Atlassian-Token': 'no-check',
    }
    files = {
        'file': (filename, open(filename, 'rb'))
    }
    url="https://jira.net/rest/api/2/issue/" + id + "/attachments"
    LOG.info("Attaching csv file...")
    response = requests.post(url, headers=headers, files=files, auth=HTTPBasicAuth(user, password))
    if response.status_code==200:
        LOG.info("File successfully attached.")
        return True
    else:
        LOG.warning("Attachment failed.")
        return False


@retry(wait_random_min=1000, wait_random_max=2000, stop_max_attempt_number=5, retry_on_exception=retry_if_connection_error)
def add_description_to_ticket(id,message):
    user=credentials.JIRA_USER
    password=credentials.JIRA_PASSWORD
    headers = {
        'X-Atlassian-Token': 'no-check',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    url="https://jira.net/rest/api/2/issue/" + id
    
    response = requests.get(url, headers=headers, auth=HTTPBasicAuth(user, password))
    response=response.json()
    desc=response['fields']['description']
    desc+="\n" + message
    payload={
        "fields": {
            "description": desc
        }
    }
    LOG.info(f"Adding {message} to description for ticket {id}...")
    response = requests.put(url, headers=headers, data=json.dumps(payload), auth=HTTPBasicAuth(user, password))
    if response.status_code in [200, 204]:
        LOG.info(f"Description successfully amended for ticket {id}.")
        return True
    else:
        LOG.warning(f"Amendment of description for ticket {id} failed.")
        return False


@retry(wait_random_min=1000, wait_random_max=2000, stop_max_attempt_number=5, retry_on_exception=retry_if_connection_error)
def transition_ticket(id,to):
    user=credentials.JIRA_USER
    password=credentials.JIRA_PASSWORD
    '''
        ids can be retrieved via GET https://jira.net/rest/api/2/issue/{ticketkeyorID}/transitions
    '''
    def switch(id):
        switcher={
            "In Progress": 11,
            "Review": 41,
            "Hold": 51,
            "Closed": 61,
            "On Hold": 81

        }
        return switcher.get(id)
    headers = {
        'X-Atlassian-Token': 'no-check',
        'Content-Type': 'application/json'
    }
    transition=str(switch(to))
    url=f"https://jira.zalando.net/rest/api/2/issue/{id}/transitions"
    payload={
        "transition": {
            "id": transition
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload), auth=HTTPBasicAuth(user, password))
    if response.status_code in [200, 204]:
        LOG.info(f"Ticket {id} successfully transferred to state {to}.")
        return True
    else:
        LOG.warning(f"Transition of ticket {id} to status {to} failed.")
        return False