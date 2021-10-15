# Docker Reverse Proxy Starter App

This repo is designed to lay out the required setup in order to preform a reverse proxy by subdomain using docker and flask. 

## Step 1
Download docker desktop 

## Step 2
Find your known hosts file on your system and add the following 

0.0.0.0 appa.test.com
<br>
0.0.0.0 appb.test.com

## Step 3 
Navigate to the root of the repository and run 
<br>
docker-compose up --build

## Step 4
Visit appa.test.com 
<br>
Visit appb.test.com

## Conclusion 
Notice that when you navigate to these different domains the requests are routed between appa and appb via port 80 on the nginx container. You can use this same structure no matter what stack you are using. Happy coding!!!