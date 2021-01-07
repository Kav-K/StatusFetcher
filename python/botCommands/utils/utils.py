import discord
from lazy_streams import stream
global GUILDS

#TODO PUT THESE INTO THE ENVIRONMENT FILE
ADMIN_ROLE_NAME = "Admin"
ADMIN_CHANNEL_NAME = "admin-chat"


#Check if a user has a set of roles
def hasRoles(memberToCheck,roleNames,guild):
    if (len(roleNames)< 2):
        return getRole(roleNames[0],guild) in memberToCheck.roles
    else:
        mappedRoles = stream(roleNames).map(lambda x: getRole(x,guild)).to_list()
        return set(mappedRoles).issubset(memberToCheck.roles)

#Get a category by identifier
def getCategory(categoryIdentifier,guild):
    if (type(categoryIdentifier) == int):
        return discord.utils.get(guild.categories,id=categoryIdentifier)
    else:
        return discord.utils.get(guild.categories,name=categoryIdentifier)

#Get channel by identifier
def getChannel(channelIdentifier,guild):
    if (type(channelIdentifier) == int):
        return discord.utils.get(guild.channels,id=channelIdentifier)
    else:
        return discord.utils.get(guild.channels,name=channelIdentifier)

#Return a single role given a identifier
def getRole(roleIdentifier,guild):
    if (type(roleIdentifier) == int):
        return discord.utils.get(guild.roles, id=roleIdentifier)
    else:
        return discord.utils.get(guild.roles, name=roleIdentifier)


#Get all members or get members with a specific set of roles
def getMembers(guild,roles=[]):
    if (len(roles)<1):
        return guild.members
    else:
        mappedRoles = stream(roles).map(lambda x: getRole(x,guild)).to_list()
        membersWithRoles = stream(guild.members).filter(lambda x: set(mappedRoles).issubset(x.roles)).to_list()
        return membersWithRoles

#Send a DM
async def send_dm(member: discord.Member, content):
    channel = await member.create_dm()
    await channel.send(content)

#See if a user is permitted to run an admin command
def permittedAdmin(user):
    return ADMIN_ROLE_NAME in stream(user.roles).map(lambda x: x.name).to_list()


