
# pylogin

Manage logins within a single page. This project utilizes email address based organizations to direct a user's login to a specific web application server. 


## Run pylogin

Install dependencies

```bash
  pip install -r requirements.txt
```


Start the server in the background

```bash
  python pylogin.py start
```

Stop the background server process

```bash
  python pylogin.py stop
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file.

`MONGO_DB_URI` = `mongodb://localhost:27017/pylogin`

`PORT` = `5000`

`PID_FILE` = `pylogin.pid`

`ALLOWED_ORIGINS` = `https://example.com`


## API Reference

#### Add organization
This is run when you add an organization to your application. An internal application would run this call.

```https
  POST /api/organization
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `organization` | `string` | **Required**. Organization name |
| `server` | `string` | **Required**. Server URL |

#### Get Organization (HTTPS Secure POST endpoint)
This is run when a user is logging into your application. It fetches the server needed for the user to login.

```https
  POST /api/organization-details
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `organization`      | `string` | **Required**. Organization name |


## License

[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)


## Disclaimer

Use this code at your own risk. All liability is disclaimed.

By reading this disclaimer or using pylogin and/or any parts of its code, you agree to the terms and conditions set forth in the license and noted annotations in the code.

