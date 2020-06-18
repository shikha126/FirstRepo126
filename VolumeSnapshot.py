import awsutils
import pprint  
import boto3 

session = awsutils.get_session('us-east-1')
#client = session.client('ec2')

#response = client.describe_instances(    
# InstanceIds=[
#        'i-0f82ea4e59ff0f349'
 #   ]
#)
#print(response)

ec2 = boto3.resource('ec2')

for i in ec2.instances.all():
    print (i.id)
for vol in ec2.volumes.all():
    #print(vol.id)
    volume4snip=vol.id
    print(volume4snip)
    result = ec2.create_snapshot(VolumeId=volume4snip,Description='Created by boto3')
    print(result.id)
    

