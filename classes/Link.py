class Link:
    def __init__(self, brawlhalla_id, brawlhalla_name, discord_id, discord_name, 
                 region='', country='', ethnicity='', own_legend='random', mate_legend='random'):
        self.brawlhalla_id = brawlhalla_id
        self.brawlhalla_name = brawlhalla_name
        self.discord_id = discord_id
        self.discord_name = discord_name
        self.region = region
        self.country = country
        self.ethnicity = ethnicity
        self.legends_for_2v2 = Legends_for_2v2(own_legend, mate_legend).__dict__

class Legends_for_2v2:
    def __init__(self, own_legend, mate_legend):
        self.own_legend = own_legend
        self.mate_legend = mate_legend