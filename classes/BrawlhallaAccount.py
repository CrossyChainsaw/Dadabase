class BrawlhallaAccount:
    def __init__(self, id, name, legend_key='random'):
        self.brawlhalla_id = id
        self.brawlhalla_name = name
        # Optional
        self.legend_key = legend_key