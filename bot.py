#!/usr/bin/env python3

import discord

from utils import main

bot = discord.Bot()

# ----------------- TODO: MAKE CHANGES BELOW ----------------- #


@bot.slash_command(description="Say hello")
@discord.option("name", description="Who to greet")
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello, {name}!")


# ----------------- TODO: MAKE CHANGES ABOVE ----------------- #


def serve_bot(token):
    bot.run(token)


if __name__ == "__main__":
    main(serve_bot)
