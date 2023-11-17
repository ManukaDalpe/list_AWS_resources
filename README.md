# Web_app_for_listing_AWS_resources
This web app made up from H2o wave app for listing AWS resources of users.

Here, my task is to build a web app for listing any AWS resources by a user. As my first attempt, I was able to make a web app for listing down AWS resources of an IAM user, but the problem with that is, it is not included each and every AWS resources but it covers most using services like EC2,S3,VPC etc.
Here I made 3 free AWS accounts and assigned a IAM user for each account as user1,user2 and user3.



https://github.com/ManukaDalpe/list_AWS_resources/assets/140248309/7281ef49-1da1-49c5-a2d7-a2602e80eeae



## Getting Started

## System Requirements
1. python 3.7+
2. pip

## 1. Clone the repository:
https://github.com/ManukaDalpe/list_AWS_resources

## 2. Create a virtual environment:
python -m venv venv

## 3. Activate the virtual environment:

source venv/bin/activate

### windows
venv/Scripts/activate.bat

To deactivate the virtual environment use deactivate command.

## 4. Install dependencies:
(venv) pip3 install -r requirements.txt

## 5. Run the app:
(venv) wave run app

## 6. View the app:
Point your favourite web browser to
http://localhost:10101/meetup

## 7. Check the app:
You can check the app by clickng user1,user2 buttons

## Others
https://wave.h2o.ai/docs/getting-started

My requirement is to list any AWS resource by a user, There are few methods to do that and I have listed down some of them here;

1. Use AWS billing console to identify the AWS services that you are using. Chances is that you would see services you are “not” supposed to be in use. Of course, I think it      would require lot of efforts to identify the specific instances of cloud resources which are not in active use this way. E.g. A Security group/VPC lying idle in a corner       waiting to be exploited.
2. AWS Tag Editor — Tag everything that is needed and use tag editor to search for all the resources that does not have this tag. I would say, first thing you wouldn’t end up     looking for tool here if your were already disciplined. In my opinion you will always have something untagged or uncontrolled. That nagging feeling in your head that           something is amiss!
3. AWS Config — I’m bit skeptical about this service, specially from pricing perspective. Also it seems the coverage is bit limited, approx 90 Cloud resources across 32 AWS       service.
4. https://vantage.sh — a new paid tool which would help to view cloud resources per your requirements (based on tags, or some other conditions )— I don’t know what kind of       conditions does it support or how many resources/AWS Services? No details on their page. I shall update once I try them.
5. https://www.fugue.co — an absolutely brillient service when it comes for visualization. In one screen you get to see everything needed. I have tried the trial and I’m          overwhelmed. But again what falls short is AWS Services and resource type coverage. Some of you may have already used their open source tool https://github.com/fugue/regula    for terraform checks.

As my second attempt was to write a python function for listing all AWS resources by user not only the most populer services. Then I first tried to add all the resources as an array and tried to list the AWS resources for perticular IAM user. Then I tried using the AWS Cloud Control API and I was able to list down all the resources created by AWS but not specific for a perticular user.I am still working on it.
Thank you!!!








