#!/usr/bin/env python3

import discord

from utils import main

bot = discord.Bot()


@bot.slash_command(
    description="Generate PDF resume from user information in YAML format",
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
)
@discord.option("file", description="YAML input file")
async def resumake(ctx, file: discord.Attachment):
    # TODO:
    # - read in file
    # - send it to hosted resumake
    # - get converted resume
    # - return resume PDF
    await ctx.respond("<PLACEHOLDER>")


if __name__ == "__main__":
    main(bot)
