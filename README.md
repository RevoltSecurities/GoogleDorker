# GoogleDorker - Unleash the power of Google dorking for ethical hackers with custom search precision.

![GitHub last commit](https://img.shields.io/github/last-commit/RevoltSecurities/GoogleDorker) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/RevoltSecurities/GoogleDorker) [![GitHub license](https://img.shields.io/github/license/RevoltSecurities/GoogleDorker)](https://github.com/RevoltSecurities/GoogleDorker/blob/main/LICENSE)

**GoogleDorker** is a powerful command-line tool tailored for bug hunters and penetration testers, enabling efficient Google Dorking. It allows users to perform advanced, targeted searches to gather critical information about their targets. By leveraging Google's APIs, **GoogleDorker** simplifies comprehensive reconnaissance and enhances the effectiveness of vulnerability assessments for cybersecurity professionals.



### **Features**
- **Asynchronous Google Dorking:** Perform advanced and efficient searches using Google Dorks with high performance, powered by asynchronous processing.  
- **Bug Hunting and Reconnaissance:** Discover valuable intelligence, potential vulnerabilities, and misconfigurations during ethical hacking and penetration testing.  
- **Real-Time Progress Tracking:** Keep track of task progression with live updates for smooth operation.  
- **Cross-Platform Compatibility:** Fully compatible with all major operating systems, requiring no additional dependencies.  
- **Customizable Search Queries:** Fine-tune Google Dorks for targeted searches and precise results.  

### Usage:
```bash
dorker -h
```
```yaml
       __                   __
  ____/ /  ____    _____   / /__  ___    _____
 / __  /  / __ \  / ___/  / //_/ / _ \  / ___/
/ /_/ /  / /_/ / / /     / ,<   /  __/ / /
\__,_/   \____/ /_/     /_/|_|  \___/ /_/


                    - RevoltSecurities



[DESCRIPTION]: GoogleDorker - Unleash the power of Google dorking for ethical hackers with custom search precision.

[USAGE]:

    dorker [flags]

[FLAGS]:

    [INPUT]:

        -q,  --query                    :  single dorking query for Dorker to search
        -l,  --list                     :  filename that contains list of dorks with target name
        stdin/stdout                    :  Dorker now supports stdin/stdout for reading dorks

    [OUTPUT]:

        -o,   --output                  :  filename to save the outputs.

    [Rate-Limits]:

        -t,    --threads                : set the concurrency level for dorking (default 20)

    [OPTIMIZATION]:

        -t,   --timeout                 :  timeout value for every sources requests (default: 15).
        -d,   --delay                   :  specify a delay value between each requests (default: 1)

    [UPDATE]:

        -up,   --update                 :  updates Dorker tool to latest version (info: requires pip to be insalled).

    [CONFIG]:

        -px,  --proxy                   :  http proxy to use with Dorker's each request
        -cp,  --config-path             :  custom path of config file for Dorker to read api keys (default path: $HOME.config/dorker/provider-config.yaml).

    [DEBUG]:

        -h,   --help                    :  displays this help message and exits
        -s,   --silent                  :  disables showing banner and version of Dorker
        -v,   --verbose                 :  enable to increase the verbosity of the Dorker
```


### Easy Installation :
**PIP:**
```bash
pip install git+https://github.com/RevoltSecurities/GoogleDorker --break-system-packages
```

**PIPX:**
```bash
pipx install git+https://github.com/RevoltSecurities/GoogleDorker
```
## **Configuration**

To configure **GoogleDorker**, you need to provide your Google API keys and Search Engine IDs in a configuration file. By default, the tool automatically loads the configuration file from:  
`$HOME/.config/dorker/provider-config.yaml`  

You can specify a custom configuration file path using the `-cp` or `--config-path` flag.

---

### **Configuration File Syntax**
Define the API keys and Search Engine IDs in one of the following formats:

#### **Format 1 (Inline List):**
```yaml
google: [
    key1:cxid,
    key2:cxid,
    key3:cxid,
    key4:cxid,
    key5:cxid
]
```

#### **Format 2 (Key-Value Pairs):**
```yaml
google:
  - key1:cxid
  - key2:cxid
  - key3:cxid
  - key4:cxid
  - key5:cxid
```

---

### **Custom Path for Configuration**
If you want to load a configuration file from a custom location, use the `-cp` or `--config-path` flag as shown below:
```bash
dorker -cp /path/to/your/custom-config.yaml
```
This flexibility allows you to manage multiple configurations for different projects or environments efficiently.


## **How to Get API Keys and CSE-ID? Follow These Steps:**

Configuring **GoogleDorker** requires Google API keys and a Custom Search Engine ID (CSE-ID). Below is a step-by-step guide to obtaining and setting them up:

---

### **Step 1:** Log In to Your Google Account  
Ensure you're logged into your Google account in your browser before proceeding.

---

### **Step 2:** Create a Custom Search Engine  
1. Visit the [Programmable Search Engine](https://programmablesearchengine.google.com/controlpanel/create).  
2. Create a new search engine and choose the **Search the entire web** option, as shown below:

   ![Search Engine Creation](https://github.com/sanjai-AK47/GoogleDorker/assets/119435129/7b871906-a08b-4473-bc47-31f797ae88f6)

---

### **Step 3:** Retrieve Your Custom Search Engine ID (CSE-ID)  
Once your search engine is successfully created:  
1. Navigate to your search engine settings.  
2. Copy the **cx value** (CSE-ID).  
3. Add this value to your configuration YAML file under the **Google-CSE-ID** field, following the syntax provided.

---

### **Step 4:** Generate Your Google API Key  
1. Go to the [Google Custom Search API](https://developers.google.com/custom-search/v1/introduction).  
2. Click on the **Get Key** button.  
3. Create a new project with any name and proceed to the next step.  
   Example of creating a project:

   ![API Key Generation](https://github.com/sanjai-AK47/GoogleDorker/assets/119435129/b7e5618d-4d3c-41a3-8147-95b5d31cc266)

---

### **Step 5:** Copy and Save Your API Key  
Once the API key is generated:  
1. Click **Show Key** to reveal it.  
2. Copy the API key and add it to your configuration YAML file under the **Google-API** field.

---

### **Step 6:** Generate Additional API Keys for Efficiency  
To maximize dorking efficiency:  
- Repeat **Step 4** to generate multiple API keys (recommended: at least 10).  
- Each API key allows approximately 100 queries, so having multiple keys increases your query capacity.

---

### **Example of Configuration YAML File**  
Below is an example of how your configuration file should look:

```yaml
google:
  - key1: cxid
  - key2: cxid
  - key3: cxid
  - key4: cxid
  - key5: cxid
  - key6: cxid
  - key7: cxid
  - key8: cxid
  - key9: cxid
  - key10: cxid
```
---

### **Configuration Done!**  
Once you've completed the configuration, you're ready to use **GoogleDorker**.  


## Query Methods

### Method1:

```bash
dorker -q "inurl:api site:bentley.com" --output google_dorks.txt

```

### Method2:

```bash
dorker -d bentley.com -q inurl:api -o google_dorks.txt

```

## **Running Dorker:**

### **1. Pass a Single Query**

To pass a single query directly via the command line, use the `-q` or `--query` flag followed by the query string.

Example:
```bash
dorker -q "site:example.com inurl:admin"
```

---

### **2. Pass a Query File**

Use the `-l` or `--list` flag followed by the path to a file containing multiple queries. Each line in the file should represent a separate query.

Example:
```bash
dorker -l queries.txt
```

---

### **3. Pass Queries via stdin (Pipe Input)**

You can pass queries using stdin by piping input into **GoogleDorker**.

Example:
```bash
echo "site:example.com inurl:admin" | dorker
```

For multiple queries:
```bash
echo -e "site:example.com inurl:admin\nsite:example.com inurl:login" | dorker
```

---

### **Summary of Flags for Query Input:**

- `-q, --query`: Pass a single query string.
- `-l, --list`: Provide a file with a list of queries.
- `stdin`: Pipe input directly to **GoogleDorker** for dynamic queries.

## **Issues**
Encountering any issues? Create a new issue in the **GoogleDorker** repository and describe the problem you’re facing. Your concerns will be addressed promptly to ensure smooth usage of the tool.

---

## **Support**

This tool is developed by **[RevoltSecurities](https://github.com/RevoltSecurities)**. If you enjoy using **GoogleDorker**, don’t forget to explore more tools in our repository designed specifically for bug hunters and penetration testers.  
Show your support by giving this project a ⭐ on GitHub! Your encouragement inspires us to create more innovative tools for the cybersecurity community.  
Check out **[Subdominator](https://github.com/RevoltSecurities/Subdominator)** for powerful subdomain enumeration and much more tools by us! Thank you to all our supporters!


















