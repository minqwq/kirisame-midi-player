import pygame.midi

pygame.midi.init()
print("Init successful.")

input_count = pygame.midi.get_count()
print(f"Max MIDI Port: {input_count}")

for i in range(input_count):
    info = pygame.midi.get_device_info(i)
    print(f"Device {i}: {info}")
