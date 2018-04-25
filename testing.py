import requests
import hashlib
import os

def datest():
    HTTP_ENCODE = "These%20are%20not%20the%20droids%20you%20are%20looking%20for..."
    REC_ERROR = 'Key already exists. Would you like to update it? Y/N:'
    RET_ERROR = False
    md5_value1 = '098f6bcd4621d373cade4e832627b4f6' 
    md5_value2 = '5eb63bbbe01eeed093cb22bb8f5acdc3' 
    FIB_SEQ = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987]
    FIB_ERR = 'Invalid Error!'
    FAILED = 0
    PASSED = 0
    print ("Testing the damn api...\n")

    api_testing = {
        '/md5/test': (200, md5_value1), '/md5/hello%20world': (200, md5_value2), '/md5': (404, None),

        '/factorial/8': (200, 40320), '/factorial/6': (200, 720), '/factorial/test': (200, None),

        '/fibonacci/8': (200, FIB_SEQ[:7]), '/fibonacci/650': (200, FIB_SEQ[:16]), '/fibonacci/tcmg': (200, None), '/fibonacci/1': (200, FIB_SEQ[:3]),

        '/is-prime/1': (200, False), '/is-prime/24': (200, False), '/is-prime/4': (200, False),
        '/is-prime/7': (200, True), '/is-prime/508': (200, False), '/is-prime/2': (200, True),

        '/slack-alert/test': (200, True), '/slack-alert/'+HTTP_ENCODE: (200, True),

        '/kv-retrieve/blaksdj': (200, RET_ERROR)
    }
    
    
    for uri, test_result in api_testing.items():
        print (" * "), uri, ("... "),
        resp = requests.get('http://localhost:5000'+uri)
        if resp.status_code == test_result[0]:
            if test_result[1] == None or resp.json()['output'] == test_result[1]:
                print("Testing: "+uri+":::::")
                print ("Expected output: '%s'" % str(test_result[1]))
                print ("Success")
                PASSED += 1
            else: 
                print("Testing: "+uri+":::::")
                print ("Failure")
                print ("Expected output: '%s'" % str(test_result[1]))
                print ("Actual output:   '%s'" % str(resp.json()['output']))
                FAILED += 1
        else:
            print("Testing: "+uri+":::::")
            print ("HTTP status error")
            print ("- Expected HTTP status: %i" % test_result[0])
            print ("- Actual HTTP status:   %i" % resp.status_code)
            FAILED += 1

    rate = float(PASSED) / float(FAILED+PASSED) * 100.0
    total = FAILED+PASSED
    print ("\n\n Total API test completed: {} \n Number of successful tests: {} \n Acceptance rate:{:.2f}%".format(total, PASSED, rate))
    
    
datest()
