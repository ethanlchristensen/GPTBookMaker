import os
import sys

current_directroy = os.getcwd()
sys.path.append(current_directroy + "/bruhbook")

from bruhbook import BruhBook

story_type = "A cyberpunk knight fighting his way through hell. Flames, lava, dark, alien like plasma monsters."
target_audience = "mature adults"

bb = BruhBook(create_cover_image=True)

story_outline = bb.generate_story_outline(
    story_type=story_type,
    target_audience=target_audience
)

bb.story_generator(
    story_type=story_type,
    target_audience=target_audience,
    story_outline=story_outline
)
    