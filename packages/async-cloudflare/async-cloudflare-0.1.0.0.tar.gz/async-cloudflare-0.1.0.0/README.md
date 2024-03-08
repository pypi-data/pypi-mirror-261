# **async-cloudflare**

![](./img.webp)

\`**async-cloudflare**\` is an asynchronous Python module for interacting with the Cloudflare API. Designed for developers who
need to integrate Cloudflare services into their applications efficiently, it offers a streamlined, async interface to
manage DNS records, zones, and more. Whether you're automating website setups, managing DNS records, or controlling
Cloudflare settings programmatically, \`**async-cloudflare**\` simplifies the process with easy-to-use Python classes and
methods.

## **Features**

- **Asynchronous Design**: Utilize Python's async/await syntax for non-blocking API calls.
- **Comprehensive Coverage**: Supports a wide range of Cloudflare API endpoints, including zones, DNS records, and account settings.
- **Easy to Use**: Simplified methods and clear documentation make it easy to integrate into your projects.
- **Flexible**: Whether you're managing a single website or hundreds, \`**async-cloudflare**\` scales with your needs.

## **Installation**

To install \`**async-cloudflare**\`, simply use pip:

```bash
pip install async-cloudflare
```

## **Quick Start**

Here's a quick example to get you started with \`**async-cloudflare**\`:

```python
import asyncio
from async_cloudflare import CloudFlare

async def list_zones():
    cf = CloudFlare(token="YOUR_CLOUDFLARE_TOKEN", email="YOUR_EMAIL", auth_key="YOUR_AUTH_KEY")
    zones = await cf.zones.get()
    for zone in zones:
        print(zone.name)

loop = asyncio.get_event_loop()
loop.run_until_complete(list_zones())
```

## Documentation

For detailed documentation, including all classes and methods available, please refer to our [GitHub repository]().

## License

\`**async-cloudflare**\` is licensed under the Apache License, Version 2.0. See the LICENSE file for more details.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a pull request to add your changes. If you find a bug or have a feature request, please open an issue.

## Support

If you need help or have any questions, join our [Telegram group](https://t.me/fafatypoty_cloaca).


> [!IMPORTANT]
> This package is not officially affiliated with Cloudflare. All trademarks belong to their respective owners.