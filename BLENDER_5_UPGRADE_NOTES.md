# Blender 5.0 Upgrade Notes

This document outlines the changes made to update the Blender Optical Flare VSE addon from Blender 2.78 compatibility to Blender 5.0 compatibility.

## Summary of Changes

The addon has been updated to work with Blender 5.0's redesigned VSE (Video Sequence Editor) and compositor architecture. The primary changes involve updating deprecated API calls and modernizing the addon's code structure.

## Detailed Changes

### 1. Optical_Flare_VSE.py

#### bl_info Updates
- **Blender version**: Updated from `(2, 78, 0)` to `(5, 0, 0)`
- **Addon version**: Bumped from `(1, 2)` to `(1, 3)`

#### Panel Registration
- **bl_idname**: Changed from `"SEQUENCER_OT_opticalflare"` to `"SEQUENCER_PT_opticalflare"`
  - Rationale: Panel identifiers should use the `PT` prefix (Panel Type), not `OT` (Operator Type)
- **bl_category**: Added `"Optical Flare"` to properly categorize the panel in the UI

#### UI Layout
- **layout.split()**: Changed `percentage=0.3` parameter to `factor=0.3`
  - Rationale: The `percentage` parameter was deprecated in favor of `factor` in later Blender versions

### 2. VSE_Transform_Tool.py

#### bl_info Updates
- **Blender version**: Updated from `(2, 6, 5)` to `(5, 0, 0)`
- **Addon version**: Bumped from `(1, 0)` to `(1, 1)`

#### Preferences API
Replaced all instances of `context.user_preferences` with `context.preferences`:
- Line 1162: Theme color access
- Line 1163: Theme color access
- Line 1195: Input preferences access
- Line 1530: Input preferences access

**Rationale**: The `user_preferences` attribute was renamed to `preferences` in Blender 2.80+

#### Registration System
Replaced deprecated `bpy.utils.register_module(__name__)` with explicit class registration:

**Before:**
```python
def register():
    bpy.utils.register_module(__name__)
    # ... other code ...

def unregister():
    bpy.utils.unregister_module(__name__)
    # ... other code ...
```

**After:**
```python
classes = (
    TF_Add_Transform,
    TF_Scale,
    TF_Rotation,
    TF_Position,
    TF_Alpha,
    TF_Crop,
    TF_Draw_Selection,
    TF_Select,
    TF_Call_Menu,
    TF_Insert_KeyFrame,
    TF_Menu_Insert_KF,
    TF_Call_Menu_Layers,
    TF_Menu_Layers,
    TF_Select_Layers,
    TF_Set_Cursor2D,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    # ... other code ...

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    # ... other code ...
```

**Rationale**: `register_module()` was deprecated and removed. Explicit class registration provides better control and clarity.

#### Property Cleanup
Added proper cleanup of Scene properties in unregister():
```python
del bpy.types.Scene.seq_cursor2d_loc
del bpy.types.Scene.seq_pivot_type
```

## API Compatibility Notes

### Sequencer API
The core sequencer functionality (accessing `sequence_editor.sequences_all`, driver management, etc.) remains compatible between Blender 2.78 and 5.0, as these APIs have been stable. The main changes were in the UI and preferences systems.

### Known Stable APIs Used
- `bpy.context.scene.sequence_editor.sequences_all` - Still functional
- `bpy.context.scene.sequence_editor.active_strip` - Still functional
- Driver API (`driver_add`, `driver.variables`, etc.) - Still functional
- Transform properties (`translate_start_x`, `scale_start_x`, etc.) - Still functional

### Breaking Changes Addressed
1. **UI/Preferences**: `user_preferences` → `preferences`
2. **Layout**: `percentage` → `factor`
3. **Registration**: `register_module()` → explicit class registration
4. **Panel naming**: Corrected `OT` to `PT` prefix

## Testing Recommendations

When testing this addon in Blender 5.0, verify:

1. **Panel appears correctly** in the Sequencer UI sidebar
2. **Create links button** successfully creates driver relationships
3. **Clean/Delete links buttons** properly manage drivers
4. **No console errors** during addon enable/disable
5. **Driver expressions** still evaluate correctly

Note: Transform tool keyboard shortcuts (G, S, R, etc.) are not available as VSE_Transform_Tool.py has been disabled. Use Blender's built-in VSE transform features instead.

## Potential Future Issues

Areas to monitor for potential issues in future Blender versions:

1. **Driver namespace**: `bpy.app.driver_namespace` usage (lines 85, 91, 95 in Optical_Flare_VSE.py)
2. **Sequence strip properties**: Monitor for any changes to transform strip property names or structures

## VSE Transform Tool - Disabled in Blender 5.0

The VSE_Transform_Tool.py component has been **disabled** in this release:

**Reason**: The addon uses the deprecated `bgl` (OpenGL) module extensively (176+ occurrences), which was removed in Blender 4.0+. The module would need to be completely rewritten to use the modern `gpu` and `gpu_extras` modules.

**Alternative**: Blender now includes built-in transform functionality in the Video Sequence Editor, making this addon component largely unnecessary for modern Blender versions.

**For Legacy Users**: If you need the VSE transform tools, use the original v1.2 addon package with Blender 2.78.

**File Status**: The file has been renamed to `VSE_Transform_Tool.py.disabled` and a README explains the situation.

## Installation

To install the updated addon in Blender 5.0:

1. Navigate to `Edit > Preferences > Add-ons`
2. Click "Install" and select:
   - `Optical_Flare_VSE.py` for the optical flare functionality (RECOMMENDED)
   - ~~`VSE_Transform_Tool.py`~~ - Disabled (uses deprecated bgl module)
3. Enable the addon by checking the checkbox
4. The panel should appear in the Sequencer sidebar (press 'N' to toggle sidebar)

## Version History

- **v1.3** (2024) - Updated for Blender 5.0 compatibility
- **v1.2** (2017) - Major update with improved workflow and 10 flare behaviors
- **v1.0** - Initial release for Blender 2.78
