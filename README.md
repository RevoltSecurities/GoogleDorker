# GoogleDorker - An next level of Google Dorking tool For Cybersecurity Community Members

GoogleDorker is a command-line-based Google Dorking tool designed for bug hunters and penetration testers. It enables users to perform in-depth searches using Google Dorks to gather information about their targets. Utilizing Google's provided free APIs, GoogleDorker empowers cybersecurity professionals to conduct comprehensive reconnaissance and vulnerability assessment.

# Features:
- **Google Dorking:** Perform advanced searches using Google Dorks to find specific information on the web.
- **Bug Hunting:** Uncover potential security vulnerabilities and misconfigurations.
- **Penetration Testing:** Gather valuable intelligence for penetration testing engagements.
- **Free Google APIs:** Utilize Google's free APIs to access powerful search capabilities.
- **Run Anywhere:** Google Dorker ability run anywhere in any OS so no dependency required in you Operating system

# Usage:
```bash
usage: dorker [-h] [-q QUERY] [-d DOMAIN] [-o OUTPUT]

A Powerfull Tool for google dorking

options:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        [ALERT]:G oogle dorking query for your target
  -d DOMAIN, --domain DOMAIN
                        [ALERT]:Target name for Google dorking
  -o OUTPUT, --output OUTPUT
                        [ALERT]:File name to save the dorking results that are found
```

# Installation for All users:

## Method 1:

```bash
pip install dorker

git clone https://github.com/sanjai-AK47/GoogleDorker.git

dorker -h

```

## Method 2:

```bash
git clone https://github.com/sanjai-AK47/GoogleDorker.git
pip install .
dorker -h
```

# Information:

For all users preferred Method 1 installtions for easy installtion and configuration for your api's after a successfull
Installation go to Dorker directory and located google-dorker.yaml file and configure your api keys as mentioned bellow


# Configurations:

Configure your api keys as a syntax That I have mentioned below

```yaml

Google-API: #Unlimited key are good

  - # API keys here

Google-CSE-ID: #Limited Id is enough

  - # your CSE id og goole


```

## How to Get api keys and CSE-ID? Follow my steps here!:

- **Step-1:** First login a google account in your browser
- **Step-2:** Visit
- [here](https://programmablesearchengine.google.com/controlpanel/create) and create a search engine and choose all web option like below mentioned in images

![Screenshot from 2023-10-07 07-52-40](https://github.com/sanjai-AK47/GoogleDorker/assets/119435129/7b871906-a08b-4473-bc47-31f797ae88f6)

- **Step-3:** After Creating your successfull search engine it time to copy your cx value and paste in yaml in below Google-CSE-ID with the following syntax given by me
- **Step-4:** After completing these all process now its time to grab your api keys of google [here](https://developers.google.com/custom-search/v1/introduction)
- **Step-5:** Press the get key button and create a new project with any name you want and click next , for example image in below
![Screenshot from 2023-10-07 07-57-25](https://github.com/sanjai-AK47/GoogleDorker/assets/119435129/b7e5618d-4d3c-41a3-8147-95b5d31cc266)

- **Step-6:** After creating and completing your api key is generated and press show key then copy it and paste in yaml file below Google-API with the following syntax given by me

- **Step-7:** With the same process from step 4 you can get unlimited api keys so grab nearly 10 api keys for you efficiency of dorking it mean you can query 1000 times when u set nealy 10 api keys or more than that

## Example Image of config yaml file
![Screenshot from 2023-10-07 08-47-19](https://github.com/sanjai-AK47/GoogleDorker/assets/119435129/5e8e2d50-d187-4e70-a3f3-65e176eb3ee8)

Ahh! Configuration are done now. NOW we will see how to use the dorker tool with a dorking query


## Query Methods

### Method1:

```bash
dorker -q "inurl:api site:bentley.com" --output google_dorks.txt

```

### Method2:

```bash
dorker -d bentley.com -q inurl:api -o google_dorks.txt

```

Query Methods are depends on your's and I preferred Method 1 will be best for all to get better results and for complicated dorking queries


## Issues:

Facing any issues? create a new issues and submit the issues you are facing in google dorker and that will be resolved as soon as possible


# Support

Hey guys Im [D.Sanjai Kumar](https://github.com/sanjai-AK47) Im the developer for these tools and try the other Tools in my repos for bug hunters and Show ur love ♥️ and give a ⭐ for this project
Which will encourage me to develop tools like this and also another tools I have made for subdomain enumeration which best in results and modes check it out the [Subdominator](https://github.com/sanjai-AK47/Subdominator) and its features
and Thanks to all supporters! in advance



















