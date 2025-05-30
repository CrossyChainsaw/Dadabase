
from Dadabase.modules.format import format_color
from Dadabase.modules.validate_type import cast_to_int


class Server:
    def __init__(self, id, name, leaderboard_title, sorting_method, show_member_count, show_no_elo_players, 
                 channel_1v1_id="", channel_2v2_id="", channel_rotating_id="", color="", image="", flag_type:str=None, show_win_loss=False, show_1v1_legends=True, show_2v2_legends=False, links=[]):
        
        # Convert Fields
        channel_1v1_id = int(channel_1v1_id)
        channel_2v2_id = int(channel_2v2_id)
        channel_rotating_id = cast_to_int(channel_rotating_id)
        color = format_color(color)
        
        # Required
        self.id = id
        self.name = name
        self.leaderboard_title = leaderboard_title
        self.sorting_method = sorting_method
        self.show_member_count = show_member_count
        self.show_no_elo_players = show_no_elo_players

        # Optional
        self.channel_1v1_id = channel_1v1_id
        self.channel_2v2_id = channel_2v2_id
        self.channel_rotating_id = channel_rotating_id
        self.image = image
        self.color = color
        self.flag_type = flag_type
        self.show_win_loss = show_win_loss
        self.show_1v1_legends = show_1v1_legends
        self.show_2v2_legends = show_2v2_legends
        self.links = links