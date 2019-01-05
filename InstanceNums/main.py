#!/usr/local/bin/python3

import boto3
import json
import os
import time
import sys

ec2 = boto3.client('ec2', region_name='ap-northeast-1')

def get_ec2_running_nums():
    ec2_response_running = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    ec2_instances_running = len(ec2_response_running['Reservations'])
    return ec2_instances_running

def get_ec2_stopped_nums():
    ec2_response_stopped = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
    ec2_instances_stopped = len(ec2_response_stopped['Reservations'])
    return ec2_instances_stopped



def mkr_prepare():
    if (os.environ.get('MACKEREL_AGENT_PLUGIN_META') == '1'):
        metrics = [
			{
                        	'name':'running',
                        	'label':'running'
         	        },
			{
                        	'name':'stopped',
                        	'label':'stopped'
         	        }
	]
        meta['graphs']['instance.num'] = {
 				    	    'label': 'instances',
					    'unit': 'integer',
				  	    'metrics': metrics
        }
        print(json.dumps(meta))
        sys.exit(0)


if __name__ == '__main__':
    mkr_prepare()
    print('\t'.join(['instance.num.running', str(get_ec2_running_nums()), str(time.time())]))
    print('\t'.join(['instance.num.stopped', str(get_ec2_stopped_nums()), str(time.time())]))

