import gc

print(f"Initial GC thresholds: {gc.get_threshold()}")

gc.set_threshold(700, 10, 10)  # Example of setting custom thresholds
print(f"New GC thresholds: {gc.get_threshold()}")

collected = gc.collect()
print(f"Manually collected {collected} objects.")