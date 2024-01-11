# Dadabase Documentation
This documentation is mainly aimed at myself since I will be the one setting up Dadabase in your server.
- [Configure Clan](#configure-clan)
- [Configure Server](#configure-server)

## Configure Clan
configuring a clan (server) enables the admin of the server to add console players to their Ranknir elo lists.

1. run `d!configureclan`

![image](https://github.com/Skyward-Brawlhalla/Dadabase/assets/74303221/39f85148-4f01-4983-b623-330d093e09c4)

2. now you can add console players using the command `d!ps4add brawlhalla_id brawlhalla_name`

![image](https://github.com/Skyward-Brawlhalla/Dadabase/assets/74303221/c98bd9f8-6bf6-4b65-a93f-1a745177be49)

3. you can list all console players you added to the list using `d!ps4list`

![image](https://github.com/Skyward-Brawlhalla/Dadabase/assets/74303221/dd2b7092-856d-453f-b958-9b67a059772f)

4. you can remove a player using `d!ps4remove brawlhalla_id`

![image](https://github.com/Skyward-Brawlhalla/Dadabase/assets/74303221/7307db3e-6d6b-42fe-b751-ab925e2c3976)

5. when you are satisfied adding and removing console players, wait for Ranknir to update. 

![image](https://github.com/Skyward-Brawlhalla/Dadabase/assets/74303221/8e7ef830-e8c0-4f4c-b3ba-41872b97ee38)

## Configure Server

1. run `d!configureserver`

![image](https://github.com/Skyward-Brawlhalla/Dadabase/assets/74303221/03b94abb-0e6e-4f0c-8e5c-fc67fc62009d)

2. Go in Ranknir Code and create a new file `data/server/Skyward/players.json`

![image](https://github.com/Skyward-Brawlhalla/Dadabase/assets/74303221/2cded985-8d73-491f-984f-e373920a6b32)

4. Make sure `Skyward_players.json` contains an empty array

![image](https://github.com/Skyward-Brawlhalla/Dadabase/assets/74303221/06cce104-5e7e-40c1-9058-ee5ef576530e)

5. now you can start using the command d!claim brawlhalla_id

![image](https://github.com/Skyward-Brawlhalla/Dadabase/assets/74303221/af65881a-2cf4-46a8-abe0-abffd7ab39f6)

