# litecord

Litecord is a lightweight and easy-to-use library for creating Discord applications.

Current development status: **Pre-Alpha**

These applications implement the Discord Interactions API to act passively.
This means that Discord sends user interactions to the application, and it
responds to these interactions by (usually) sending a message back to the user.
These interactions can come from slash commands, buttons, select menus, or context menus.
These applications will not, however, receive any other events from Discord, and also won't be able to interact with users without prior interaction from them.
These limitations are what allow this library to be particularly easy to use,
and also help with making it more scalable. If you need a feature that requires
interacting with Discord via the websockets API, consider using
[discord.py](https://discordpy.readthedocs.io/en/latest/) (or one of its forks)
or [Hikari](https://docs.hikari-py.dev/en/latest/) instead.

## Anti-features

Usage of this library naturally requires interacting with Discord, a proprietary
web service. Interacting with Discord via the API as well as creating and
operating a Discord application requires agreeing to Discord's
[Terms of Service](https://discord.com/terms),
[Privacy Policy](https://discord.com/privacy),
[Developer Terms of Service](https://discord.com/developers/docs/policies-and-agreements/developer-terms-of-service)
and [Developer Policy](https://discord.com/developers/docs/policies-and-agreements/developer-policy).

## Disclaimer

This library is not endorsed by or affiliated with Discord.

There is another project called Litecord, which is a
[clean-room design reimplementation of Discord's API](https://gitlab.com/litecord/litecord).
This project is not related to that one, but we love what they're doing over there. ♥

Discord is a registered trademark of Discord Inc.

Except as otherwise noted, litecord is licensed under the ISC License (LICENSE or https://opensource.org/license/isc-license-txt).

SPDX-License-Identifier: ISC
