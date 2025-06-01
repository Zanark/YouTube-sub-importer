import csv

# Define keywords for game dev filtering
keywords = [
    'game dev', 'gamedev', 'game development', 'unity', 'unreal', 'godot', 'gdc', 'shader',
    'level design', 'game design', 'game programming', 'game engine', 'game art',
    'pixel art', 'indie dev', 'indie game', 'blender', '3d modeling', 'character rigging',
    'game ai', 'pathfinding', 'gameplay programming', 'procedural generation',
    'entity component system', 'ecs', 'game loop', 'ai behavior tree',
    'open world design', 'platformer', 'rpg game dev', 'top down shooter',
    '2d animation', 'tilemap', 'navmesh', 'photon multiplayer', 'netcode',
    'steamworks', 'itch.io', 'asset store', 'visual scripting', 'blueprint',
    'c# unity', 'c++ unreal', 'unity tutorial', 'unreal tutorial', 'godot tutorial',
    'game jam', 'ludum dare', 'global game jam', 'devlog', 'dev log', 'dev diary',
    'playmaker unity', 'cinemachine', 'game physics', 'ragdoll physics',
    'rigging blender', 'bake lighting', 'baked lighting', 'post processing',
    'game monetization', 'game marketing', 'level editor', 'game pipeline',
    'game production', 'game testing', 'bug fixing', 'debugging unity', 'profiling',
    'game architecture', 'finite state machine', 'fsm', 'openGL game',
    'vulkan game dev', 'game rendering', 'game lighting', 'game audio',
    'game sound design', 'fmod', 'wwise', 'unity input system', 'input manager',
    'gamepad input', 'character controller', 'game dev tips', 'gamemaker',
    'construct 3', 'pico-8', 'love2d', 'monogame', 'raylib', 'engine dev',
    'buildbox', 'game idea', 'game concept', 'game loop system', 'multiplayer sync',
    'game code architecture', 'asset optimization', 'game devlog', 'unity ecs',
    'unreal blueprint', 'game tools', 'vfx graph', 'shader graph'
]

# Read the CSV and filter based on title
filtered_channels = []
with open('subscriptions.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        title = row['Channel title']
        if any(kw.lower() in title.lower() for kw in keywords):
            filtered_channels.append(row)

# Save filtered channels to a new CSV
with open('game_dev_channels.csv', 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Channel ID', 'Channel URL', 'Channel title'])
    writer.writeheader()
    writer.writerows(filtered_channels)

# Optionally: Open each channel in browser (semi-automated subscribe)
import webbrowser
import time

for row in filtered_channels:
    webbrowser.open(row['Channel URL'])
    time.sleep(2)  # Small delay to avoid freezing
