# Branded QR Code Generator
## Problem
The goal of this project is to make an easy-to-use, deployable, compute efficient, and brandable qr code generator.

Most online generators make your QR code expire. So instead of linking your direct link they make re-directs. This is good for shortterm QR codes, but is horrible for things that you want control over (example stickers).

Our generator takes your link, or other encodable data, and embeds it directly into the QR code. It also has the free feature of adding your brand to the QR code.

## API Usage
The API responds to get requests with the following query:
```
https://api.host.fake/brand-qr-code?url={URL}
```
Currently it only takes URLs that have been Base64 URL encoded. The API outputs a Base64 encoded PNG file.

## Building
### Download Serverless Dependency Plugin
```bash
serverless plugin install -n serverless-python-requirements
```

### Set Up VirtualEnv
Install virtualenv
```bash
pip install virtualenv
virtualenv --python=python3.9 env
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


## Deploy
### Setup serverless
In your terminal
```bash
serverless
```
Go through the prompts and setup an account. Connect AWS to your dashboard.

After connecting your AWS account, deploy the application. Run this command whenever there are changes to```serverless.yml```:

```bash
serverless deploy #--verbose
```
After this the API will show up on your Serveless dashboard.


If you make changes to code only use
```bash
serverless deploy function -f brand_qr
```

To delete your your service use the following:
```bash
serverless remove
```
