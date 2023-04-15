import discord
from discord import app_commands


intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# create an empty dictionary to store user lists for each server
users_lists = {}


@tree.command(name="commandname", description="My first application Command")
async def first_command(interaction):
    await interaction.response.send_message("Hello!")


@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user.name} (ID: {client.user.id})")
    print("------")


@client.event
async def on_message(message):
    print(f"Received message: {message.content}")
    if message.content == "!join":
        # check if the server has a user list
        if message.guild.id not in users_lists:
            # if not, create a new user list for the server
            users_lists[message.guild.id] = []
        # check if the user has already joined
        if message.author.name not in users_lists[message.guild.id]:
            # add the user to the list
            users_lists[message.guild.id].append(message.author.name)
            # Get the "Ark Member" role.
            role = discord.utils.get(message.guild.roles, name="Ark Member")

            # Give the user the role.
            await message.author.add_roles(role)
            # generate a numbered list of users
            users_list_str = "\n".join(
                [
                    f"{i + 1}. {user}"
                    for i, user in enumerate(users_lists[message.guild.id])
                ]
            )
            await message.channel.send(
                f"{message.author.name} has registered for ark!\n "
            )
        else:
            await message.channel.send(
                f"{message.author.name} has already registered for ark."
            )
    elif message.content == "!members":
        # check if the server has a user list
        if message.guild.id not in users_lists:
            await message.channel.send("No users have registered for ark yet.")
        else:
            # generate a numbered list of users
            users_list_str = "\n".join(
                [
                    f"{i + 1}. {user}"
                    for i, user in enumerate(users_lists[message.guild.id])
                ]
            )
            await message.channel.send(f"Current signups:\n{users_list_str}")

    elif message.content == "!clear":
        # check if the user is an administrator
        if message.author.guild_permissions.administrator:
            # check if the server has a user list
            if message.guild.id not in users_lists:
                await message.channel.send("No users have registered for ark yet.")
            else:
                # clear the user list
                users_lists[message.guild.id] = []
                await message.channel.send(
                    "All users have been removed from ark registration."
                )
        else:
            await message.channel.send(
                "You do not have permission to clear the list"
            )

    elif message.content == "!leave":
        # check if the server has a user list
        if message.guild.id not in users_lists:
            await message.channel.send("You are not currently registered for ark.")
        # check if the user is on the list
        elif message.author.name in users_lists[message.guild.id]:
            # remove the user from the list
            users_lists[message.guild.id].remove(message.author.name)
            # remove the role from the user
            role = discord.utils.get(message.guild.roles, name="Ark Member")
            await message.author.remove_roles(role)
            await message.channel.send(
                f"{message.author.name} has been removed from ark registration."
            )
        else:
            await message.channel.send("You are not currently on registered for ark.")


client.run("TOKEN")
