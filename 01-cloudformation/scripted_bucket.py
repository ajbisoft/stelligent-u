import json
import boto3


def get_regions(config_file):
    ''' Loads regions from config '''
    
    return json.load(open(config_file))


def create_update_stack(region, stack_name, template):
    ''' Creates or updates stack if exists already '''

    try:
        print(f"Creating stack in region {region}")
        cf.create_stack(
            StackName=stack_name,
            TemplateBody=template,
        )
    except cf.exceptions.AlreadyExistsException:
        print(f"Updating stack in region {region}")
        try:
            cf.update_stack(
                StackName=stack_name,
                TemplateBody=template,
            )
        except cf.exceptions.ClientError as e:
            print(e)
    

if __name__ == "__main__":
    stack_name = 'jk-test-01-cloudformation'
    template = open('scripted_bucket.yml').read()
    
    for region in get_regions('scripted_bucket.json'):
        # Setup connection to AWS
        cf = boto3.client('cloudformation', region_name=region['Region'])
    
        # Create or update stack in given region
        create_update_stack(region['Region'], stack_name, template)
