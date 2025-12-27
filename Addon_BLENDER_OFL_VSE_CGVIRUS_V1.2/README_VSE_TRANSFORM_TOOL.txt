VSE Transform Tool - Disabled for Blender 5.0

The VSE_Transform_Tool.py addon has been disabled in this Blender 5.0 release because:

1. It uses the deprecated 'bgl' module which was removed in Blender 4.0+
2. Blender now has built-in transform functionality in the Video Sequence Editor
3. Migrating from bgl to gpu module would require extensive refactoring (176+ occurrences)

The original file has been renamed to VSE_Transform_Tool.py.disabled and is kept 
for reference purposes.

If you need the VSE transform functionality:
- Use Blender's built-in VSE transform tools (available natively in modern Blender)
- For Blender 2.78 users: Use the original v1.2 addon package

The main Optical Flare Engine (Optical_Flare_VSE.py) remains fully functional 
and does not use bgl, so it works perfectly with Blender 5.0.
