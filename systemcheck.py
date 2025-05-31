# ✅ About the platform module
# The platform module in Python provides a way to access information about the underlying platform (i.e., the operating system, hardware, and Python interpreter version). It's part of Python's standard library and is useful for getting system-related details like OS name, release, version, architecture, etc.

#platform(aliased=0, terse=0)

# aliased (bool) – If True, it returns alternate names for some systems/OSes.
# terse (bool) – If True, it returns a simplified or shorter version of the platform string.

from platform import platform
print(platform()) # Windows-11-10.0.26100-SP0
print(platform(1)) #Windows-11-10.0.26100-SP0
print(platform(0, 1)) #Windows-11

# OS: Windows
# Release: 11 (windows 11)
# Version: 10.0.26100
# Service Pack: SP0

from platform import machine
print(machine()) # AMD64 (machine name)
from platform import processor
print(processor())
from platform import system
print(system()) # windows
from platform import version
print(version()) # 10.0.26100 
