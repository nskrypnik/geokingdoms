
aws cloudformation update-stack \
  --stack-name GeoKingdomsStack \
  --template-body file://$( pwd )/cf_template.yml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameters ParameterKey=MasterUsername,ParameterValue=${GK_DB_USERNAME} ParameterKey=MasterUserPassword,ParameterValue=${GK_DB_PASSWORD}
