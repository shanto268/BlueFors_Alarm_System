import asyncio

import BlueFors
from Slack_Messenger import Slack_er

folder_path = 'Bluefors_Logs'

bf = BlueFors.BlueFors('bf_fridge',
              folder_path=folder_path,
              channel_vacuum_can=1,
              channel_pumping_line=2,
              channel_compressor_outlet=3,
              channel_compressor_inlet=4,
              channel_mixture_tank=5,
              channel_venting_line=6,
              channel_50k_plate=1,
              channel_4k_plate=2,
              channel_magnet=None,
              channel_still=6,
              channel_mixing_chamber=5)

mc_channel_id=6
Slacker = Slack_er(bf)
asyncio.run(Slacker.listen_to_slack_events())

print(bf.get_pulse_tube_status())
print(bf.get_temperature(mc_channel_id))