class BrawlhallaAccount:
    def __init__(self, id:int, name:str, clan_index:int, discord_id=None, own_legend='random', mate_legend='random'):
        self.brawlhalla_id = id
        self.brawlhalla_name = name
        clan_index = clan_index
        # Optional
        self.discord_id = discord_id
        self.own_legend = own_legend
        self.mate_legend = mate_legend