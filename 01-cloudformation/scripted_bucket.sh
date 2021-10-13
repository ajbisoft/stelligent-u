#!/bin/bash

jq -c '.[]' scripted_bucket.json | while read i; do
    REGION=`echo $i | jq -r ".Region"`
    aws --region $REGION cloudformation create-stack --stack-name jk-test-01-cloudformation --template-body file://scripted_bucket.yml
done
