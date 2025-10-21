import time
import random
import keyboard  # pip install keyboard

# --- Game Config ---
BPM = 120                    # beats per minute
BEAT_INTERVAL = 60 / BPM     # seconds between beats
KEYS = ['a', 's', 'd', 'f']  # keys used for rhythm input
BOSS_HEALTH = 12

# --- Game State ---
player_score = 0
boss_health = BOSS_HEALTH
running = True
beat_count = 0

# --- Utility ---
def print_banner():
    print("=============================================================")
    print("============= TERMINAL BOSS RUSH: STRIKE HOUR ===============")
    print("=============================================================")
    print("== Press A/S/D/F in time with the beat to attack the boss! ==")
    print("=============== Press Q to quit at any time! ================")
    print("=============================================================")
    print("==================== Hit Enter to start! ====================")
    print("=============================================================")

# --- Pattern Generator ---
def generate_pattern():
    """Generate a 4-beat pattern using keys and '.' for rests."""
    pattern = []
    for _ in range(4):
        if random.random() < 0.25:
            pattern.append('.')  # rest (no input expected)
        else:
            pattern.append(random.choice(KEYS))
    return pattern

# --- Game Logic ---
def play_pattern(pattern):
    """Play through one bar (4 beats) and check inputs."""
    global player_score, boss_health
    CALLOUTS = {1 : "ONE", 2 : "TWO", 3 : "THREE", 4 : "FOUR"}

    print("\nNext Pattern:")
    for i in range(4):
        print(CALLOUTS[i+1]+ ": " + " | ".join([p.upper() for p in pattern]))
        if i != 3:
            time.sleep(BEAT_INTERVAL)
    

    for i, target in enumerate(pattern):
        print(f"\nBeat {i+1}: ", end='', flush=True)
        if target == '.':
            print("(rest)")
        else:
            print(f"PRESS [{target.upper()}]!")

        beat_start = time.time()
        pressed_key = None

        while time.time() - beat_start < BEAT_INTERVAL:
            for key in KEYS:
                if keyboard.is_pressed(key):
                    pressed_key = key

        # Evaluate
        if target == '.':
            if pressed_key:
                print("❌ Should’ve rested!")
                player_score -= 50
            else:
                print("😌 Perfect Rest.")
                player_score += 25
        else:
            if pressed_key == target:
                print("🎯 Perfect Hit!")
                boss_health -= 1
                player_score += 100
            elif pressed_key:
                print("❌ Wrong key!")
                player_score -= 50
            else:
                print("⏱️ Miss!")

        print(f"Boss HP: {'❤' * boss_health}")
        time.sleep(BEAT_INTERVAL*0.2)  # short pause before next beat

        if boss_health <= 0:
            print("\n💥 Boss defeated! You win!")
            return False  # stop game early
    return True


# --- Main ---
print_banner()
input()

print("=============================================================")
print("================= Boss appears! Get ready... ================")
time.sleep(0.2)
print("===============                                ==============")
time.sleep(0.2)
print("=============                                    ============")
time.sleep(0.2)
print("===========                                        ==========")
time.sleep(0.2)
print("=========                                            ========")
time.sleep(0.2)
print("=======                                                ======")
time.sleep(0.2)
print("                      Here's the bpm!                        ")
for count in range(1, 5):
    print(f"============================ {count} ==============================")
    time.sleep(BEAT_INTERVAL)

while running:
    pattern = generate_pattern()
    still_alive = play_pattern(pattern)
    beat_count += 4

    if not still_alive:
        break

    # Quit option
    if keyboard.is_pressed('q'):
        print("\nGame Over (Quit)")
        break

print(f"\nFinal Score: {player_score}")
