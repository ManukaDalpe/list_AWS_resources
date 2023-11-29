import boto3

def list_resources_for_iam_user(access_key, secret_key, iam_user_name, resources):
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    config_client = session.client('config')

    for resource in resources:
        try:
            response = config_client.list_discovered_resources(
                ResourceType=resource,
                resourceFilters=[
                    {
                        'value': iam_user_name,
                        'key': 'AWS:Principal:Service',
                    },
                ],
            )

            print('##################### {} #################'.format(resource))

            for i in range(len(response['resourceIdentifiers'])):
                print('{} , {}'.format(
                    response['resourceIdentifiers'][i]['resourceType'],
                    response['resourceIdentifiers'][i]['resourceId']
                ))

        except Exception as e:
            print(f"Error listing resources for {resource}: {str(e)}")

if __name__ == "__main__":
    # Replace 'your-access-key' and 'your-secret-key' with your actual AWS access key and secret key
    access_key = ''
    secret_key = ''

    # Replace 'user2' with the actual IAM user name
    iam_user_name = 'user2'

resources = [
    "AWS::EC2::CustomerGateway", "AWS::EC2::EIP", "AWS::EC2::Host", "AWS::EC2::Instance", "AWS::EC2::InternetGateway",
    "AWS::EC2::NetworkAcl", "AWS::EC2::NetworkInterface", "AWS::EC2::RouteTable", "AWS::EC2::SecurityGroup",


    "AWS::EC2::Subnet", "AWS::CloudTrail::Trail", "AWS::EC2::Volume", "AWS::EC2::VPC", "AWS::EC2::VPNConnection",
    "AWS::EC2::VPNGateway", "AWS::EC2::RegisteredHAInstance", "AWS::EC2::NatGateway",
    "AWS::EC2::EgressOnlyInternetGateway", "AWS::EC2::VPCEndpoint", "AWS::EC2::VPCEndpointService",
    "AWS::EC2::FlowLog", "AWS::EC2::VPCPeeringConnection", "AWS::IAM::Group", "AWS::IAM::Policy", "AWS::IAM::Role",
    "AWS::IAM::User", "AWS::ElasticLoadBalancingV2::LoadBalancer", "AWS::ACM::Certificate", "AWS::RDS::DBInstance",
    "AWS::RDS::DBParameterGroup", "AWS::RDS::DBOptionGroup", "AWS::RDS::DBSubnetGroup", "AWS::RDS::DBSecurityGroup",
    "AWS::RDS::DBSnapshot", "AWS::RDS::DBCluster", "AWS::RDS::DBClusterParameterGroup", "AWS::RDS::DBClusterSnapshot",
    "AWS::RDS::EventSubscription", "AWS::S3::Bucket", "AWS::S3::AccountPublicAccessBlock", "AWS::Redshift::Cluster",
    "AWS::Redshift::ClusterSnapshot", "AWS::Redshift::ClusterParameterGroup", "AWS::Redshift::ClusterSecurityGroup",
    "AWS::Redshift::ClusterSubnetGroup", "AWS::Redshift::EventSubscription", "AWS::SSM::ManagedInstanceInventory",
    "AWS::CloudWatch::Alarm", "AWS::CloudFormation::Stack", "AWS::ElasticLoadBalancing::LoadBalancer",
    "AWS::AutoScaling::AutoScalingGroup", "AWS::AutoScaling::LaunchConfiguration", "AWS::AutoScaling::ScalingPolicy",
    "AWS::AutoScaling::ScheduledAction", "AWS::DynamoDB::Table", "AWS::CodeBuild::Project", "AWS::WAF::RateBasedRule",
    "AWS::WAF::Rule", "AWS::WAF::RuleGroup", "AWS::WAF::WebACL", "AWS::WAFRegional::RateBasedRule", "AWS::WAFRegional::Rule",
    "AWS::WAFRegional::RuleGroup", "AWS::WAFRegional::WebACL", "AWS::CloudFront::Distribution",
    "AWS::CloudFront::StreamingDistribution", "AWS::Lambda::Alias", "AWS::Lambda::Function",
    "AWS::ElasticBeanstalk::Application", "AWS::ElasticBeanstalk::ApplicationVersion",
    "AWS::ElasticBeanstalk::Environment", "AWS::MobileHub::Project", "AWS::XRay::EncryptionConfig",
    "AWS::SSM::AssociationCompliance", "AWS::SSM::PatchCompliance", "AWS::Shield::Protection",
    "AWS::ShieldRegional::Protection", "AWS::Config::ResourceCompliance", "AWS::LicenseManager::LicenseConfiguration",
    "AWS::ApiGateway::DomainName", "AWS::ApiGateway::Method", "AWS::ApiGateway::Stage", "AWS::ApiGateway::RestApi",
    "AWS::ApiGatewayV2::DomainName", "AWS::ApiGatewayV2::Stage", "AWS::ApiGatewayV2::Api", "AWS::CodePipeline::Pipeline",
    "AWS::ServiceCatalog::CloudFormationProvisionedProduct", "AWS::ServiceCatalog::CloudFormationProduct",
    "AWS::ServiceCatalog::Portfolio"
]


list_resources_for_iam_user(access_key, secret_key, iam_user_name, resources)
