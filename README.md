# StatusFetcher
A lightweight system that allows you to fetch your discord status externally and display it anywhere you want. This doesn't really provide any real value, I just thought it was cool.

# Components

## Python
The python components are a discord bot. This bot works right out of the box, all you need to do is invite the discord bot to your server, and create a .env file that has a token called DISCORD_TOKEN = "TOKEN HERE"

This discord bot will connect to the server that you're on and will create a web interface to retrieve a user ID's status remotely

## Middleware
In case you can't access the web interface created by your python bot instance directly (for instance, if it breaks your SSL or you would need to change CORS settings to do it), you can use the PHP middleware and it will proxy the connection.

## Javascript
The javascript code dynamically updates a dom element of your choice every X seconds with your discord status.
