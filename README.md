# Flask, Webhook Relay and Swarm

This is a simple example of how to use webhook to expose your localhost. In this repo, I will show you how to expose a Flask app to the internet through webhook relay.

## Requirements:
- A free account on WebHook Relay
- Be able to clone this repo
- Latest version of docker installed on your device

## Steps:
1. Clone this repository
```
git clone https://github.com/yorjaggy/poc_flask_webhook_relay.git
```

2. Create a tunnel in Webhook Relay (WR) website
In WR dashboard, go to tunnels and create a Tunnel, you should provide a tunnel name and destination host. Other parameters are set up by default
```
Name = myflasktunnel
Destination=http://flask_api:80
```

3. Create an access token to WR client
In WR dashboard, go to Access Tokens and create a new Token. Save the key and secret value created to use on docker-compose.yml file

4. Build a minimal docker image with Python and Gunicorn
Execute the next command to build the docker image to use in your docker-compose.yml file
```
docker build -t flask_gunicorn:latest .
```

5. In your docker-compose.yml file replace three values:
```
    - YOUR_TUNNEL_NAME -> using the tunnel name you've provided in the tunnel creation
    - WEBHOOK_KEY_VAL -> obtained in the 3rd step
    - WEBHOOK_SECRET_VAL -> obtained in the 3rd step
```

6. Deploy the services
```
docker-compose up
```

# That's all folks
