import boto3
from scripted_bucket_common import get_regions


def delete_stack(region, stack_name):
    ''' Deletes stack if exists already '''

    try:
        cf.delete_stack(
            StackName=stack_name,
        )
    except Exception as e:
        print(e)


if __name__ == "__main__":
    stack_name = 'jk-test-01-cloudformation'

    for region in get_regions('scripted_bucket.json'):
        # Setup connection to AWS
        cf = boto3.client('cloudformation', region_name=region['Region'])
    
        # Delete stack in given region
        delete_stack(region['Region'], stack_name)
