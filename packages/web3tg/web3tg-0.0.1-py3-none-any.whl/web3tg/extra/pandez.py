"""
pip install unicaps better-proxy
"""

import asyncio
import logging
import os
from io import BytesIO

import discord
from curl_cffi import requests
from discord import Invite
from discord.abc import Snowflake
from discord.http import Route
from unicaps import AsyncCaptchaSolver, CaptchaSolvingService
from unicaps.common import CaptchaCharType
from unicaps.exceptions import ServiceTooBusy
from web3db import DBHelper
from web3db.models import Profile
from dotenv import load_dotenv

from extra.capmonster import solve_captcha

load_dotenv()

INVITE = "whalesmarket"
VERIFIED_CHANNEL_ID = 1149109535651414116
PANDEZ_CHANNEL_ID = 1169487564051316758
PANDEZ_MESSAGE_ID = 1169487572217626716

CAPTCHA_API_KEY = os.getenv('TWOCAPTCHA_API_KEY')
CAPTCHA_SERVICE = CaptchaSolvingService.TWOCAPTCHA  # Должен поддерживать Image Captcha

discord.utils.setup_logging(level=logging.INFO)


class PandezGuildJoiner(discord.Client):
    """
    :param invite: Invite code or url
    :param verified_channel_id: The channel id that is available to the verified user (For example General, Announcement)
    """

    def __init__(
            self,
            invite: str,
            verified_channel_id: int,
            pandez_channel_id: int,
            pandez_message_id: int,
            captcha_solver: AsyncCaptchaSolver,
            **options,
    ):
        super().__init__(**options)
        self.captcha_solver = captcha_solver
        self.invite = invite
        self.pandez_channel_id = pandez_channel_id
        self.pandez_message_id = pandez_message_id
        self.verified_channel_id = verified_channel_id
        self.verified = False
        self.target_guild = None

    @staticmethod
    async def _click_button_by_label(message: discord.Message, label: str):
        for component in message.components:
            for button in component.children:
                if button.label == label:
                    await button.click()
                    break

    async def _check_verification(self, guild: discord.Guild):
        me = guild.get_member(self.user.id)
        verified_channel = await guild.fetch_channel(self.verified_channel_id)
        permissions = verified_channel.permissions_for(me)
        if permissions.read_messages:
            self.verified = True
            await self.close()
    async def on_ready(self):
        print(f'[@{self.user}] Logged on')

        if not self.user.phone:
            print(f"[@{self.user}] No phone number!")
            await self.close()
            return

        invite = await self.accept_invite(self.invite)
        self.target_guild = invite.guild
        # await self.agree_guild_rules(invite)

        await self._check_verification(invite.guild)

        if self.verified:
            return

        pandez_channel = invite.guild.get_channel(self.pandez_channel_id)
        pandez_message = await pandez_channel.fetch_message(self.pandez_message_id)
        await self._click_button_by_label(pandez_message, "Verify")

    async def on_message(self, message: discord.Message):
        if self.verified:
            return

        await self._click_button_by_label(message, "Continue")

    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if self.verified:
            return

        await self._click_button_by_label(after, "Continue")

        if not before.embeds:
            return

        if before.embeds[0].description != 'Generating captcha image. Please wait...':
            return

        captcha_image_url = after.embeds[0].image.url
        async with requests.AsyncSession() as session:
            response = await session.get(captcha_image_url)
        image = BytesIO(response.content)

        try:
            solved = await self.captcha_solver.solve_image_captcha(
                image=image,
                is_phrase=False,
                is_math=False,
                char_type=CaptchaCharType.NUMERIC,
                min_len=6,
                max_len=6,
            )
        except ServiceTooBusy:
            await self.close()
            raise

        solution = solved.solution.text
        for custom_id in solution:
            for component in after.components:
                for button in component.children:
                    if button.custom_id == custom_id:
                        await button.click()
                        break
                else:
                    continue
                break

        # TODO Повтор при неудачном решении

        await self._check_verification(self.target_guild)


async def join_guild():
    db = DBHelper(os.getenv('CONNECTION_STRING'))
    profiles: list[Profile] = await db.get_random_profiles_by_proxy()
    async with AsyncCaptchaSolver(CAPTCHA_SERVICE, CAPTCHA_API_KEY) as captcha_solver:
        for profile in profiles:
            joiner = PandezGuildJoiner(
                INVITE,
                VERIFIED_CHANNEL_ID,
                PANDEZ_CHANNEL_ID,
                PANDEZ_MESSAGE_ID,
                captcha_solver,
                proxy=profile.proxy.proxy_string,
                captcha_handler=solve_captcha
            )
            await joiner.start(profile.discord.auth_token)



asyncio.run(join_guild())
