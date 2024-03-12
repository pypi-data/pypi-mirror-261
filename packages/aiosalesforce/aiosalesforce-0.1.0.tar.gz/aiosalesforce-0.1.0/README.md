<p align="center" style="font-size:40px; margin:0px 10px 0px 10px">
    <em>aiosalesforce</em>
</p>
<p align="center">
    <em>Python client for the Salesforce REST API</em>
</p>
<p align="center">
<a href="https://pypi.org/project/aiosalesforce" target="_blank">
    <img src="https://badge.fury.io/py/aiosalesforce.svg" alt="PyPI Package">
</a>
</p>

# About

**Documentation:** https://georgebv.github.io/aiosalesforce

**License:** [MIT](https://opensource.org/licenses/MIT)

**Support:** [ask a question](https://github.com/georgebv/aiosalesforce/discussions)
or [create an issue](https://github.com/georgebv/aiosalesforce/issues/new/choose),
any input is appreciated and would help develop the project

`aiosalesforce` is a modern, production-ready Python client for the Salesforce REST API.
It is built on top of the `httpx` library and provides a simple and intuitive API
for interacting with Salesforce's REST API.

- **Fast:** designed from the ground up to be fully asynchronous
- **Fully typed:** every part of the library is fully typed and annotated
- **Intuitive:** API follows naming conventions of the Salesforce REST API while
  staying idiomatic to Python
- **Reliable:** flexible and robust retrying configuration
- **Salesforce first:** built with years of experience working with the Salesforce API
  it is configured to work out of the box and incorporates best practices and
  latest Salesforce API features
- **Track your API usage:** built-in support for tracking Salesforce API usage

## Requirements

`aiosalesforce` depends on:

- Python 3.11+
- [httpx](https://www.python-httpx.org/)

## Installation

```shell
pip install aiosalesforce
```

## Quickstart

Example below shows how to:

- Authenticate against Salesforce using the SOAP login method
- Create a Salesforce client
- Create a new Contact
- Read a Contact by ID
- Execute a SOQL query

```python
import asyncio

from aiosalesforce import Salesforce
from aiosalesforce.auth import SoapLogin
from httpx import AsyncClient

# Reuse authentication session across multiple clients (refreshes automatically)
auth = SoapLogin(
    username="your-username",
    password="your-password",
    security_token="your-security-token",
)

async def main():
    async with AsyncClient() as client:
        # Create a Salesforce client
        salesforce = Salesforce(
            client,
            base_url="https://your-instance.my.salesforce.com",
            auth=auth,
        )

        # Create a new Contact
        contact_id = await salesforce.sobject.create(
            "Contact",
            {
                "FirstName": "John",
                "LastName": "Doe",
                "Email": "john.doe@example.com",
            },
        )
        print(f"Created Contact with ID: {contact_id}")

        # Read Contact by ID
        contact = await salesforce.sobject.get("Contact", contact_id)
        print(contact)

        # Execute a SOQL query
        async for record in salesforce.query("SELECT Id, Name FROM Contact"):
            print(record)


if __name__ == "__main__":
    asyncio.run(main())
```
