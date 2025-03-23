# resumake-bot

Discord bot to convert YAML resume files to PDF using [Resumake](<https://github.com/cybardev/resumake> "Resumake — resume generator")

<img height="128px" width="128px" src="./resumake.png" alt="resumake logo"><img height="128px" src="./resumake-banner.png" alt="resumake banner">

## Usage

1. Create a bot via Discord Developer Portal.

2. From the left list of tabs, select Installation and copy the Install Link.

3. Visit the Install Link in a browser and add your bot to desired server(s) and/or guild(s).
    - Add scope `application.commands` and `bot` with permissions `Send Messages`, `Send Messages in Threads`, and `Use Slash Commands` to the Invite Link before using it (Discord Developer Portal `>` Installation `>` Guild Install)

4. Deploy bot to Render using the button under [Deployment](#deployment).
    - Set the `BOT_TOKEN` environment variable to your bot's token (Discord Developer Portal `>` Bot `>` Token)

5. Send `/resumake <file> <filename:optional>` in a server/guild with the bot and attach a YAML file in [this format](<https://github.com/cybardev/resumake/blob/main/resume.yml> "YAML data input format for Resumake") and give an optional filename to get back a PDF resume.

## Deployment

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/cybardev/resumake-bot)