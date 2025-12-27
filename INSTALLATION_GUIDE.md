# Installation Guide for Blender 5.0

## Quick Install

### Method 1: Install from Folder
1. Open Blender 5.0
2. Go to `Edit > Preferences > Add-ons`
3. Click `Install...`
4. Navigate to the `Addon_BLENDER_OFL_VSE_CGVIRUS_V1.2` folder
5. Select either:
   - `Optical_Flare_VSE.py` - For optical flare effects
   - `VSE_Transform_Tool.py` - For enhanced transform tools
   - Or install both separately
6. Click `Install Add-on`
7. Enable the addon by checking the checkbox next to it

### Method 2: Manual Installation
1. Copy the addon files to your Blender addons directory:
   - **Windows**: `%APPDATA%\Blender Foundation\Blender\5.0\scripts\addons\`
   - **macOS**: `~/Library/Application Support/Blender/5.0/scripts/addons/`
   - **Linux**: `~/.config/blender/5.0/scripts/addons/`
2. Restart Blender
3. Go to `Edit > Preferences > Add-ons`
4. Search for "Optical Flare" or "VSE Transform"
5. Enable the addon(s)

## Usage

### Optical Flare Engine

Once installed, the Optical Flare panel will appear in the Sequencer sidebar:

1. Open the **Video Editing** workspace or switch to **Sequencer** mode
2. Press `N` to open the sidebar if not visible
3. Look for the **Optical Flare** tab
4. Select your flare strip in the sequencer
5. Use the buttons:
   - **Create links** - Sets up driver relationships for the flare system
   - **Clean links** - Removes drivers from muted strips
   - **Delete links** - Removes all drivers from the flare system

### VSE Transform Tools

Enhanced transform operations in the VSE preview window:

**Keyboard Shortcuts:**
- `G` - Move/Position transform strips
- `S` - Scale transform strips
- `R` - Rotate transform strips
- `T` - Add transform effect to selected strips
- `Q` - Adjust alpha/opacity
- `C` - Crop tool
- `I` - Insert keyframe menu
- `A` - Select all transform strips at current frame
- Hold `Alt` + shortcut to reset the property to default

**Transform Modifiers:**
- `Ctrl` - Snap to increments
- `Shift` - Precision mode (slower movement)
- `X` or `Y` - Constrain to axis
- `Middle Mouse Button` - Choose constraint axis dynamically

**Pivot Points:**
- Access via the header icon in Sequencer preview
- Options: Median Point, Individual Origins, 2D Cursor, Active Strip
- Set 2D Cursor with `Ctrl + Left Click` in preview

## Prerequisites

### Required Assets

The optical flare addon expects lens flare element images to be available. These are included in the `LENSE FLARE ELEMENTS` folder within the addon directory.

**Important**: The preset file `OFL_Preset_CGVIRUS.blend` contains pre-configured flare setups that can be appended into your project.

### Blender Version

- **Minimum**: Blender 5.0.0
- **Recommended**: Latest Blender 5.x release

## Troubleshooting

### Addon doesn't appear in preferences
- Make sure you're installing the `.py` files, not the folder
- Check that you're using Blender 5.0 or later
- Look in the console window (Window > Toggle System Console on Windows) for error messages

### Panel doesn't show in Sequencer
- Press `N` to toggle the sidebar visibility
- Make sure you're in the Sequencer area (not Timeline or other editor)
- Check that the addon is actually enabled in Preferences

### "Create links" button doesn't work
- Ensure you have an active strip selected in the sequencer
- The strip name should match the expected naming convention for the flare system
- Check the console for any error messages

### Transform tools keyboard shortcuts don't work
- Make sure you're hovering over the Sequencer Preview area (not the timeline)
- Check that you have a Transform strip type selected
- Verify the shortcuts haven't been overridden by other addons

### OpenGL/Drawing Issues
If you see visual glitches in the transform tools:
- The addon uses legacy OpenGL drawing (bgl module)
- This should work in Blender 5.0 but may need updates in future versions
- Check for addon updates if issues occur

## Known Limitations

1. **Legacy Drawing API**: The transform tools use the older `bgl` drawing API which may be deprecated in future Blender versions
2. **Naming Convention**: The optical flare system requires specific naming patterns for strips to function correctly
3. **Single Scene**: Drivers are scene-specific and won't transfer between scenes automatically

## Getting Help

If you encounter issues:

1. Check the Blender console for error messages
2. Verify you're using the correct Blender version (5.0+)
3. Review the `BLENDER_5_UPGRADE_NOTES.md` for technical details
4. Check the original addon documentation in the repository

## Credits

- **Original Author**: Fahad Hasan Pathik (CGVIRUS)
- **Transform Tools**: kgeogeo & DoubleZ
- **Blender 5.0 Update**: Community contribution

## License

This addon is distributed under the GNU General Public License v2.0 or later.
