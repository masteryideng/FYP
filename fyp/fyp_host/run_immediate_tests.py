import jenkins
import sys
import requests


server = jenkins.Jenkins('http://localhost:8080/', username='masteryideng', password='nyzy945==')
# crumb = requests.get('http://localhost:8080/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)', auth=('masteryideng', 'nyzy945=='))

payload = (('file0', open(sys.argv[5], "rb")),
            ('json', '{"parameter":['
                     '{"name":"fyp/android-debug.apk", "file":"file0"}, '
                     '{"name":"platformVersion", "value":"%s"}, '
                     '{"name":"deviceName", "value":"%s"}, '
                     '{"name":"traversal_time", "value":"%s"}, '
                     '{"name":"monkey_time", "value":"%s"}]}' % (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])))

resp = requests.post("http://localhost:8080/job/Immediately_Test/build",
                     auth=('masteryideng','nyzy945=='),
                     headers={"Jenkins-Crumb":"7ced540fa41adc5e5a65157ef265bc82"},
                     files=payload)

last_build_number = server.get_job_info("Immediately_Test")['lastCompletedBuild']['number']
build_info = server.get_build_info("Immediately_Test", last_build_number)
print (last_build_number + 1)
