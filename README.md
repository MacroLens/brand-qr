# QR Code Generator.
## Problem
The goal of this project is to make an easy-to-use, deployable, compute efficient, and brandable qr code generator.

Most online generators make your QR code expire. So instead of linking your direct link they make re-directs. This is good for shortterm QR codes, but is horrible for things that you want control over (example stickers).

Our generator takes your link, or other encodable data, and embeds it directly into the QR code. It also has the free feature of adding your brand to the QR code.

## Goals

### Lambda
### API
### Web server


## Building
### Download Serverless Dependency Plugin
```bash
serverless plugin install -n serverless-python-requirements
```

### Set Up VirtualEnv
Install virtualenv
```bash
pip install virtualenv
virtualenv env --python=python3
source env/bin/activate
```
Install dependencies
```bash
pip install -r requirements.txt
```
Unset your virtualenv
```bash
deactivate
```

### Test Invocations
```local_request.json``` uses a base64 url encoded string for the URL.
To test the generator use the following command:
```bash
sls invoke local --function brand_qr --path local_request.json
```

