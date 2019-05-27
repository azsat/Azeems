
#!/usr/bin/env python3

# getAcctTransactions.py

# This is an example piece of Python logic that may be leveraged to make an API request
# This logic is used to retrieve customer account transaction history.
# You will need to supply your own header and parameter information in curly brackets
# The code is untested and just a proposed approach

import http.client

headers = {
    # Request headers
    'x-api-client-id': 'fractClient',
    'x-api-Partner-Id': '{partner}',
    'x-api-Company-Id': '{companyId}',
    # Token Obtained - used to make call
    'Authorization': '{idToken}'
}

params = {
           'bankID': '{bankID}',
           'bankAccountId': '{bankAccountId}',
           'status': '{status}',
           'fromDate': '{fromDate}',
           'toDate': '{toDate}'
}

try:
    conn = http.client.HTTPSConnection('https://r7p2rhg4ji.execute-api.eu-west-1.amazonaws.com/v1/banking/')

    conn.request("GET", ":bankId/accounts/:accountId/transactions?companyId={companyId}?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()

except Exception as e:
    print(str(e))
