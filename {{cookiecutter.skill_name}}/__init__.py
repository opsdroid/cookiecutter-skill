from opsdroid.skill import Skill
from opsdroid.matchers import match_regex


class {{cookiecutter.skill_name.capitalize()}}Skill(Skill):

    @match_regex(r'hi')
    async def hello(self, message):
        await message.respond('Hey')
