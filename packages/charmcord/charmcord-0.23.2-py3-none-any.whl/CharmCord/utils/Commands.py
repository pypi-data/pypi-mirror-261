from CharmCord.tools import checkArgCheck, checkArgs, findBracketPairs, noArguments, lets, isValid


########################################
#              COMMANDS                #
########################################


class Commands:
    # Global variables

    @staticmethod
    def command(name: str, code: str, aliases: list = [], bot=None):
        from CharmCord.utils.CharmCord import TotalFuncs
        # Define command function dynamically

        @bot.command(name=name, aliases=aliases)
        async def go(ctx, *args, codes=code):
            context = ctx
            new_code = await checkArgCheck(args, codes, context)
            if new_code == "Failed":
                return
            code1 = await noArguments(new_code, TotalFuncs, context)
            code2 = checkArgs(args, code1)
            final_code = await isValid(code2, TotalFuncs)
            await findBracketPairs(final_code, TotalFuncs, context)
            if len(lets) >= 1:
                lets.clear()
