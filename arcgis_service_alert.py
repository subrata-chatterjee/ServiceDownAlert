import psutil
import common

def sendEmail(service):   

    subject = "ArcGIS Service is STOPPED - Please Check"
    body ="""Hi Team,
    
    Kindly check below service. It's stopped. 

    {}  
    
    Br,
    Subrata""".format(service['name'])

    common.sendEmail(common.sender_email, common.receiver_email_to, common.receiver_email_cc, subject, body, "")
            
def getService(name):

    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        print(str(ex))
    return service

def checkservice():
    service = getService('ArcGIS Service')

    if service and service['status'] == 'stopped':
        sendEmail(service)

if __name__ == '__main__':    
    checkservice()
