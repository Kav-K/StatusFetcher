import os
import sys
from dotenv import load_dotenv
from aiohttp import web
import asyncio
from botCommands.administrative import Administrative
import discord
from discord.ext import commands


load_dotenv()

SERVER_HOST = "0.0.0.0"
SERVER_PORT = "3000"

#HTTP Server to listen for retrieval requests for a specific discord ID
class Listener():

	def __init__(self, bot):
		self.bot = bot

	async def webserver(self):


		#Handle the retrieval of a user status
		async def retrieveStatusHandler(request):
			discordid = request.rel_url.query['discordId']
			for member in self.bot.guilds[0].members:
				if (str(member.id) == discordid):
					break

			return web.Response(text=str(member.status))


		app = web.Application()


		#Handler for the status retrieval functionality
		app.router.add_get('/retrieveStatus', retrieveStatusHandler)


		runner = web.AppRunner(app)
		await runner.setup()
		self.site = web.TCPSite(runner, SERVER_HOST, SERVER_PORT)
		await self.bot.wait_until_ready()
		await self.site.start()

	def __unload(self):
		asyncio.ensure_future(self.site.stop())



def main():
	bot = commands.Bot(command_prefix='~')
	bot.remove_command('help')
	bot.add_cog(Administrative(bot))
	httpServer = Listener(bot)
	bot.loop.create_task(httpServer.webserver())

	bot.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Caught keyboard interrupt, killing")
	except Exception as e:
		print(str(e))
	finally:
		sys.exit(0)