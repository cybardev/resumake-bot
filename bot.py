#!/usr/bin/env python3

import discord

from utils import main, generate_resume

bot = discord.Bot()


@bot.slash_command(
    description="Generate PDF resume from user information in YAML format",
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
)
@discord.option("file", description="YAML input file")
async def resumake(ctx, file: discord.Attachment, filename: str = "resume"):
    await ctx.defer()
    await file.save(f"{filename}.yaml")
    await generate_resume(filename)
    await ctx.respond(file=discord.File(f"{filename}.pdf"))


if __name__ == "__main__":
    main(bot)
