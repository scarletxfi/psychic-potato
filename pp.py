#psychic-potato 

#display at5 time

#disaply air quality, by taking the average of brighton with melbourne cbd from 

import http.client, urllib.request, urllib.parse, urllib.error, base64
from dotenv import load_dotenv
load_dotenv()
import os
import requests

pkey = os.getenv('PRIMARY_KEY')
skey = os.getenv('SECONDARY_KEY')

headers = {
    # Request headers
    'X-TransactionID': '',
    'X-TrackingID': '',
    'X-SessionID': '',
    'X-CreationTime': '',
    'X-InitialSystem': '',
    'X-InitialComponent': '',
    'X-InitialOperation': '',
    'X-API-Key': pkey,
}

params = urllib.parse.urlencode({
    # Request parameters
    #'since': ' ',
    #'until': ' ',
    #'interval': ' ',
})

#Vic EPA monitoring sites:
#extracted from https://www.epa.vic.gov.au/for-community/airwatch/airwatch-table-data-page#
#site name, siteID, siteType
vicSitesList = [
    'Bairnsdale',        '1233a348-f5ee-4bb0-8f3f-20b754ded627', '',
    'Bright',            '86a5bb48-6847-49bc-ade6-b2d8ee82e7d0', '',
    'Coolaroo',          'a3f4cefe-eabb-47c7-b3eb-a6088cf6ddae', '',
    'Dallas',            '72db581f-19e3-4079-9e9b-80feaed6edb8', '',
    'Nicholson',         '983cddae-0c93-4cc7-9dff-d16f8a69f55d', '',
    'Omeo',              '0b52bdf2-a845-4a1a-8bc7-554fca3bb131', '',
    'Orbost',            'b88aa1d7-947a-4118-8d0d-8bd45b697066', '',
    "Swift's Creek",     '9187923e-aba9-4446-b779-f457c40b577d', '',
    'Wodonga',           '87c772a4-0410-41e2-95a2-511f1bcd5990', '',
    'Alphington',        'c69ed768-34d2-4d72-86f3-088c250758a8', '',
    'Box Hill',          '77062cb7-3e3b-4984-b6d0-03dda76177f2', '',
    'Brighton',          'd56ede8c-637a-41e9-a055-f53198e9456a', '',
    'Brooklyn',          'c45c92d1-7996-4bf0-b90d-249d15deabd2', '',
    'Churchill',         'ee780b50-0240-4c7e-99f8-0df759caf3a3', '',
    'Dandenong',         '69088979-01eb-4b48-9535-22b6d69421ec', '',
    'Footscray',         'd9345e0a-5eaf-4d0b-a07b-6bdfb8e98bac', '',
    'Geelong South',     '5fa9b7aa-651d-4c9d-96b1-8f6813b2d933', '',
    'Melbourne CBD',     '4afe6adc-cbac-4bf1-afbe-ff98d59564f9', '',
    'Melton',            'ea40fbea-46ce-4acf-8f3e-eb76c26c712b', '',
    'Moe',               'f5c385fd-c136-4398-99b0-35696b711b7b', '',
    'Mooroolbark',       'a535938e-57b9-4b1d-8749-5cb38457feae', '',
    'Morwell East',      '032edf91-3cb9-42be-8ff3-70d3f56dba68', '',
    'Morwell South',     '33f48fb3-f771-49e8-b554-0fcec8eb70bb', '',
    'Newborough',        'f86eb787-f0e5-4a7b-af59-d0e1b6a3c1ad', '',
    'Point Cook',        '15b90658-97fe-42a4-8bb8-cfc5cc90cdc9', '',
    'Rosedale',          '63a73778-4244-481b-82d9-3a7c416832eb', '',
    'Traralgon',         '70584bae-a7e7-4ae9-adf5-1e8e92b15386', '',
    'Wangaratta',        '8413d21d-5440-4f2b-81f9-2e5cfb8620d0', '',
    'Yinnar',            '932e8220-8d30-4e51-9200-e5b1ec8f87fb', '',
    'Boolarra',          '1adaf80a-f20f-4fd3-8fa1-60d87acfce61', '',
    'Boolarra South',    'dd8279c0-018d-469b-92c7-49eeeecd27de', '',
    'Callignee',         '56a01f92-efd2-4f9f-8ee8-19a2138434bd', '',
    'Flynn',             '86a49d71-03f4-4589-af5a-cc63b730faaf', '',
    'Flynns Creek',      '7e56abba-a570-4139-ad68-f45033862599', '',
    'Glengarry',         '3d1a81e7-ef78-4800-80c6-cc7e6ea01cf4', '',
    'Hazelwood Pondage', 'f0cdc1fe-90b9-40b6-bc5a-f6e639ccf114', '',
    'Hernes Oak',        '63fc308f-baf4-4dd5-9c3e-abe8f996342b', '',
    'Traralgon East',    '33fd2638-98ff-4b6c-8b75-5feecae706df', '',
    'Traralgon South',   'cddf953a-b932-4918-97ea-1d19583d507a', '',
    'Tyers',             'ce30ee54-f7f7-4d34-9708-0762c9f86878', '',
    'Tyers North',       '69fa2d5e-557c-457a-9103-21bc2609f5eb', '',
    'Willow Grove',      '3a0e909b-a278-4c5b-8786-975c5ef4c4c9', '',
    'Yallourn North',    'a4f9fa11-1e9b-45eb-9473-9a8418a1c6bf', '',
    'Yinnar',            'aa39a036-4514-4b51-aaf4-6276e98b036c', ''
]

siteID='4afe6adc-cbac-4bf1-afbe-ff98d59564f9'

try:
    conn = http.client.HTTPSConnection('gateway.api.epa.vic.gov.au')
    #conn.request('GET', "/environmentMonitoring/v1/sites/4afe6adc-cbac-4bf1-afbe-ff98d59564f9?%s" % params, '{body}', headers)
    conn.request('GET', '/environmentMonitoring/v1/sites/'+str(siteID), '', headers)
    response = conn.getresponse()
    data = response.read()
    #print(data)
    conn.close()
    #print JSON
    print(data.decode('UTF-8'))
except Exception as e:
    print(e)
    #print('[Errno {0}] {1}'.format(e.errno, e.strerror))
