# pycord-template

Discord bot template using Pycord, with instructions on free Render deployment

## Usage

1. Click <kbd>Use this template</kbd> (green button, usually in the top-right area of this page)

2. Select "Create new repository"

3. In your repository, edit the following files:
    - [README.md](./README.md) (this file) for documentation
    - [TERMS.md](./TERMS.md) to reflect your bot's terms of service
    - [PRIVACY.md](./PRIVACY.md) to reflect your bot's privacy policy
    - [bot.py](./bot.py) for main bot functionality
    - [render.yml](./render.yaml) for deployment configuration
    - [requirements.txt](./requirements.txt) and [Dockerfile](./Dockerfile) if your bot requires additional dependencies
    - [.envrc](./.envrc) to change dev shell method or adding environment variables to dev shells
    - [shell.nix](./shell.nix) to modify the dev shell

4. Create a tagged release after you're done editing your bot, and let the GitHub Actions workflow run

5. Create a bot in the [Discord Developer Portal](<https://discord.com/developers/applications> "link to Discord Developer Portal")
    - copy the bot token and store it securely; this will be needed for deployment

6. Edit [render.yaml](./render.yaml) and set image URL to `ghcr.io/<your_username>/<your_repository>:latest`

7. Click on the <kbd>Deploy to Render</kbd> button under [Deployment](#deployment)

8. Add your bot token (from step 5) as the value of Environment Variable `BOT_TOKEN` and create the web service

9. Save the public URL of the web service (in the format `https://<service_name>.onrender.com`)
    - making a request at this link (in a browser or programmatically) will wake up the bot when Render spins it down due to idleness (it's a free tier limitation; to have your bot always on, upgrade and change service type to [background worker](<https://render.com/docs/background-workers> "Render Background Workers documentation"))

10. Go to the Settings page of the deployed web service from your Render Dashboard and copy the Render Deploy Hook URL

11. Add a repository secret called `RENDER_DEPLOY_HOOK` and paste the copied value from the previous step

12. Add your bot to a Discord server and see it in action

## Deployment

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

**PS**: If the above button does not work, you can replace the link (in the last parentheses) with this format:
- `https://render.com/deploy?repo=https://github.com/<your_username>/<your_repository>/tree/<branch_to_deploy>`