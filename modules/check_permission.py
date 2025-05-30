import discord

# be in one of these servers
BRAWLHALLA_HUNGARY_SERVER_ID = 1209624739635531857
# have on of these roles
M30W_ROLE = "M30W"
BRAWLHALLA_NL_ROLE_1 = "Nederland"
BRAWLHALLA_NL_ROLE_2 = "België"
M3W_ROLE = "M3W"
DEVOPS_ROLE = "DevOps"
LEGION_ROLE = "Legion ORG"
ROLES_TO_CHECK = [BRAWLHALLA_NL_ROLE_1, BRAWLHALLA_NL_ROLE_2, M30W_ROLE, M3W_ROLE, DEVOPS_ROLE, LEGION_ROLE]

def has_permission(interaction):
    if any(__has_role(interaction.user, role) for role in ROLES_TO_CHECK) or __is_member(interaction, BRAWLHALLA_HUNGARY_SERVER_ID):
        return True
    else:
        return False
    
def __has_role(member, role):
    if discord.utils.get(member.roles, name=role) is not None:
        return True
    else: 
        return False
    
def __is_member(interaction, server_id):
    if interaction.guild.id == server_id:
        return True
    else:
        return False