#!/usr/bin/env python3
"""
Addon Validation Script for Blender 5.0 Compatibility
This script validates the addon code for syntax errors and checks
for deprecated API usage without requiring Blender to be installed.
"""

import ast
import os
import re
import sys

def check_syntax(filepath):
    """Check Python syntax of the file."""
    print(f"\nChecking syntax: {os.path.basename(filepath)}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        ast.parse(code)
        print("  [PASS] Syntax is valid")
        return True, code
    except SyntaxError as e:
        print(f"  [FAIL] Syntax error: {e}")
        return False, None

def check_deprecated_apis(filepath, code):
    """Check for deprecated API usage."""
    print(f"\nChecking deprecated APIs: {os.path.basename(filepath)}")
    
    deprecated_patterns = {
        r'user_preferences': 'Should use "preferences" instead',
        r'percentage\s*=': 'Should use "factor" instead of "percentage"',
        r'register_module': 'Should use explicit class registration',
        r'unregister_module': 'Should use explicit class unregistration',
    }
    
    issues_found = []
    for pattern, message in deprecated_patterns.items():
        matches = re.finditer(pattern, code)
        for match in matches:
            line_num = code[:match.start()].count('\n') + 1
            issues_found.append((line_num, pattern, message))
    
    if issues_found:
        print("  [FAIL] Found deprecated API usage:")
        for line_num, pattern, message in issues_found:
            print(f"    Line {line_num}: {pattern} - {message}")
        return False
    else:
        print("  [PASS] No deprecated APIs found")
        return True

def check_bl_info(filepath, code):
    """Check bl_info dictionary for proper Blender 5.0 version."""
    print(f"\nChecking bl_info: {os.path.basename(filepath)}")
    
    # Find bl_info dictionary
    bl_info_match = re.search(r'bl_info\s*=\s*\{([^}]+)\}', code, re.MULTILINE | re.DOTALL)
    if not bl_info_match:
        print("  [FAIL] bl_info dictionary not found")
        return False
    
    bl_info_str = bl_info_match.group(0)
    
    # Check Blender version
    version_match = re.search(r'"blender"\s*:\s*\((\d+),\s*(\d+),\s*(\d+)\)', bl_info_str)
    if not version_match:
        print("  [FAIL] Blender version not found in bl_info")
        return False
    
    major, minor, patch = map(int, version_match.groups())
    
    if major == 5 and minor == 0 and patch == 0:
        print(f"  [PASS] Blender version is 5.0.0")
        return True
    else:
        print(f"  [FAIL] Blender version is {major}.{minor}.{patch}, expected 5.0.0")
        return False

def check_registration_pattern(filepath, code):
    """Check for proper registration pattern."""
    print(f"\nChecking registration pattern: {os.path.basename(filepath)}")
    
    # Check for register/unregister functions
    if 'def register():' not in code:
        print("  [FAIL] register() function not found")
        return False
    
    if 'def unregister():' not in code:
        print("  [FAIL] unregister() function not found")
        return False
    
    # Check if using explicit registration (for VSE_Transform_Tool.py)
    if 'VSE_Transform' in filepath:
        if 'classes = (' in code:
            print("  [PASS] Using explicit class registration pattern")
            return True
        else:
            print("  [WARN] Should use explicit class registration")
            return True  # Warning but not failure
    else:
        # For Optical_Flare_VSE.py
        if 'register_class' in code:
            print("  [PASS] Using explicit class registration")
            return True
        else:
            print("  [FAIL] Not using explicit class registration")
            return False

def check_panel_naming(filepath, code):
    """Check panel naming conventions."""
    print(f"\nChecking panel naming: {os.path.basename(filepath)}")
    
    # Find panel bl_idname
    panel_matches = re.finditer(r'class\s+\w+\(bpy\.types\.Panel\):.*?bl_idname\s*=\s*["\']([^"\']+)["\']', 
                                 code, re.MULTILINE | re.DOTALL)
    
    all_good = True
    for match in panel_matches:
        bl_idname = match.group(1)
        if '_OT_' in bl_idname:
            print(f"  [FAIL] Panel bl_idname '{bl_idname}' uses _OT_ (should be _PT_)")
            all_good = False
        elif '_PT_' in bl_idname:
            print(f"  [PASS] Panel bl_idname '{bl_idname}' uses correct _PT_ prefix")
        else:
            print(f"  [WARN] Panel bl_idname '{bl_idname}' doesn't follow naming convention")
    
    return all_good

def validate_addon(filepath):
    """Run all validation checks on an addon file."""
    print(f"\n{'='*60}")
    print(f"Validating: {filepath}")
    print('='*60)
    
    # Check syntax
    syntax_ok, code = check_syntax(filepath)
    if not syntax_ok:
        return False
    
    # Check for deprecated APIs
    api_ok = check_deprecated_apis(filepath, code)
    
    # Check bl_info
    bl_info_ok = check_bl_info(filepath, code)
    
    # Check registration pattern
    reg_ok = check_registration_pattern(filepath, code)
    
    # Check panel naming
    panel_ok = check_panel_naming(filepath, code)
    
    # Overall result
    all_passed = syntax_ok and api_ok and bl_info_ok and reg_ok and panel_ok
    
    print(f"\n{'='*60}")
    if all_passed:
        print(f"[PASS] {os.path.basename(filepath)} - All checks passed!")
    else:
        print(f"[FAIL] {os.path.basename(filepath)} - Some checks failed")
    print('='*60)
    
    return all_passed

def main():
    """Main validation function."""
    addon_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'Addon_BLENDER_OFL_VSE_CGVIRUS_V1.2'
    )
    
    addon_files = [
        os.path.join(addon_dir, 'Optical_Flare_VSE.py'),
        os.path.join(addon_dir, 'VSE_Transform_Tool.py')
    ]
    
    print("Blender 5.0 Addon Validation Script")
    print("====================================")
    print("This script validates addon compatibility without requiring Blender.")
    
    all_passed = True
    for filepath in addon_files:
        if os.path.exists(filepath):
            if not validate_addon(filepath):
                all_passed = False
        else:
            print(f"\n[ERROR] File not found: {filepath}")
            all_passed = False
    
    print("\n" + "="*60)
    print("FINAL RESULT")
    print("="*60)
    if all_passed:
        print("[SUCCESS] All addons passed validation!")
        print("The addons should be compatible with Blender 5.0")
        sys.exit(0)
    else:
        print("[FAILURE] Some validation checks failed")
        print("Review the issues above before using with Blender 5.0")
        sys.exit(1)

if __name__ == '__main__':
    main()
