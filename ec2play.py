import awsutils
import boto3

session = awsutils.get_session('us-east-1')

ec2 = boto3.resource('ec2')


for instance in ec2.instances.all():
    ec2.describe_instances(instance)
    print (instance.id , instance.state)
    #ec2.instances.stop() 
    #ec2.instances.start()
    #ec2.instances.reboot()
