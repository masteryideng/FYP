import jenkins

server = jenkins.Jenkins('http://localhost:8080/', username='masteryideng', password='nyzy945==')
last_build_number = server.get_job_info('Immediately_Test')['lastCompletedBuild']['number']
console_output = server.get_build_console_output('Immediately_Test', last_build_number).encode('ascii', 'ignore').decode('ascii')
print console_output
