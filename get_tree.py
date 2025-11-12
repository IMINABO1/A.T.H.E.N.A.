import uiautomation as auto
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def print_tree(node, indent=0):
    """
    Recursively prints each UIA node’s ControlType, Name, and Bounds.
    """
    prefix = "  " * indent
    ctype = node.ControlTypeName                  # e.g. “Window”, “Button”, “Image”, etc.
    name = node.Name or "<no name>"               # Friendly name or fallback
    rect = node.BoundingRectangle                 # (left, top, right, bottom)

    print(f"{prefix}{ctype:12} | {name:30} | {rect}")
    for child in node.GetChildren():
        print_tree(child, indent + 1)

if __name__ == "__main__":
    print("[*] Switch focus to the window you want to inspect (you have 2 seconds)...")
    time.sleep(2)

    # Grab the UIA element for whatever window is currently focused
    root = auto.GetForegroundControl()
    if not root:
        print("[-] No foreground window found. Make sure a window is active.")
        exit(1)

    print(f"[*] UIA tree for: \"{root.Name}\"  (ClassName: {root.ClassName})")
    print_tree(root)
