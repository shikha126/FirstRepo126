"""Deleting snapshots which are older than x days"""

import boto3
import awsutils
from datetime import datetime,timedelta, timezone

ec2 = boto3.resource('ec2')

snapshots = ec2.snapshots.filter(OwnerIds=['self'])

for snapshot in snapshots:
    start_time = snapshot.start_time
    delete_time = datetime.now(tz=timezone.utc) - timedelta(minutes=1)
    #print(snapshot.id,start_time,delete_time)
    if delete_time > start_time:
        snapshot.delete()
        print(snapshot.id)