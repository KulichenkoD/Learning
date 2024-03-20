import os, sys
print(os.name)
print([f for f in os.listdir() if os.path.isdir(f)])
print([f for f in os.listdir() if os.path.isfile(f)])
print(sys.platform)

print(sys.getwindowsversion())
print(sys.getwindowsversion().platform_version)