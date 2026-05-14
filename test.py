try:
    from chicken_classifier import logger
    print("Package imported successfully!")
    print("You are ready to start coding!")
except ImportError as e:
    print(f"Import failed: {e}")