# Cloudflare URL Scanner PY-SDK

Python SDK for the Cloudflare URL Scanner API. It provides a simple way to interact with the API and scan URLs for malware, phishing, and more.
Read more about the Cloudflare URL Scanner API [here](https://developers.cloudflare.com/radar/investigate/url-scanner/).
> [!NOTE]
> This SDK is **not** an official Cloudflare product.

## Installation

You can install the SDK using pip:

```bash
pip install cloudflare-url-scanner
```

or from github:

```bash
python -m pip install -U git+https://github.com/alexraskin/cloudflare-url-scan
```

or from source:

```bash
git clone
cd cloudflare-url-scan
python -m pip install .
```

## Usage

```python
from cloudflare_scan import UrlScannerClient


cf_client = UrlScannerClient(
    cloudflare_api_key="", #or set the environment variable CLOUDFLARE_API_KEY
    cloudflare_account_id="", #or set the environment variable CLOUDFLARE_ACCOUNT_ID
)

# Scan a URL
scan = cf_client.scan("example.com")

# Get the scan result
result = scan.result

# Get the UUID of the scan
uuid = scan.uuid

# Get the screenshot of the scan
screenshot = cf_client.get_screen_shots(uuid, resolution="desktop")

# Get the HAR file of the scan
har = cf_client.get_har(uuid)

# Get the scan by UUID
scan = cf_client.get_scan(uuid)

# Search for a scan by hostname
scan = cf_client.search("example.com")

# Get the scan result
result = scan.result

# Get the json response
json = scan.json

# Get the text response
text = scan.text

# Get the status code
status_code = scan.status_code
```

## License

MIT
