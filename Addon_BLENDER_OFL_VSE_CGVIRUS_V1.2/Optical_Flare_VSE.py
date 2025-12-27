# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Blender Optical Flare Engine",
    "description": "Optical Flare Engine for VSE",
    "author": "Fahad Hasan Pathik CGVIRUS",
    "version": (1, 2),
    "blender": (2, 78, 0),
    "category": "Sequencer",
    "warning":     ""
    }


import bpy
import random
from math import *


def main(context):

    # OBJECT VAR CALLS

    bpyobj = bpy.context.scene.sequence_editor.sequences_all
    stringnum = "%s" % context.scene.sequence_editor.active_strip.name

    coreobj  = bpyobj["[TR]-OLVSE_Coreobject_1%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_2%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_3%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_4%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_5%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_6%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_7%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_8%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_9%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_10%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_11%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_12%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_13%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_14%s"%stringnum]

    spreadobj  = bpyobj["[TR]-OLVSE_spreaadobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_14%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_15%s"%stringnum]

    coreextraobj  = bpyobj["[TR]-OLVSE_coreextraobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_14%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_15%s"%stringnum]

    primestrixobj  = bpyobj["[TR]-OLVSE_Strix_1%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_2%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_3%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_4%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_5%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_6%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_7%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_8%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_9%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_10%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_11%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_12%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_13%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_14%s"%stringnum]

    secondstrixobj = bpyobj["[TR]-OLVSE_Strix_15%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_16%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_17%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_18%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_19%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_20%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_21%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_22%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_23%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_24%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_25%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_26%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_27%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_28%s"%stringnum]

    spriteaobj  = bpyobj["[TR]-OLVSE_Spriteobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_14%s"%stringnum]

    anamstixobj  = bpyobj["[TR]-OLVSE_Anamstrixobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_14%s"%stringnum]

    extraobj  = bpyobj["[TR]-OLVSE_Extraobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_14%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_15%s"%stringnum]

    gritmaskobj = bpyobj["[TR]-OLVSE_Grit_Mask%s"%stringnum]

    ghostXobj = bpyobj["[TR]-OLVSE_primary_hoopx%s"%stringnum], bpyobj["[TR]-OLVSE_secondary_hoopx%s"%stringnum], bpyobj["[TR]-OLVSE_ghost1_x%s"%stringnum], bpyobj["[TR]-OLVSE_ghost2_x%s"%stringnum], bpyobj["[TR]-OLVSE_ghost3_x%s"%stringnum], bpyobj["[TR]-OLVSE_ghost4_x%s"%stringnum], bpyobj["[TR]-OLVSE_ghost5_x%s"%stringnum]

    ghostYobj = bpyobj["[TR]-OLVSE_primary_hoopy%s"%stringnum], bpyobj["[TR]-OLVSE_secondary_hoopy%s"%stringnum], bpyobj["[TR]-OLVSE_ghost1_y%s"%stringnum], bpyobj["[TR]-OLVSE_ghost2_y%s"%stringnum], bpyobj["[TR]-OLVSE_ghost3_y%s"%stringnum], bpyobj["[TR]-OLVSE_ghost4_y%s"%stringnum], bpyobj["[TR]-OLVSE_ghost5_y%s"%stringnum]

    anamghostXobj  = bpyobj["[TR]-OLVSE_anam_ghostx_1%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_2%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_3%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_4%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_5%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_6%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_7%s"%stringnum]

    anamghostYobj  = bpyobj["[TR]-OLVSE_anam_ghosty_1%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_2%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_3%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_4%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_5%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_6%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_7%s"%stringnum]

    # CONTROLLER VER CALLS
    core = bpy.context.scene.sequence_editor.sequences_all["[TR]-OLVSE_Core%s"%stringnum]
    tail = bpy.context.scene.sequence_editor.sequences_all["[TR]-OLVSE_Tail%s"%stringnum]
    centeroid = bpy.context.scene.sequence_editor.sequences_all["[TR]-OLVSE_centeroid%s"%stringnum]
    corename = "[TR]-OLVSE_Core%s"%stringnum
    tailname = "[TR]-OLVSE_Tail%s"%stringnum
    centername = "[TR]-OLVSE_centeroid%s"%stringnum
    globctrlname = "[TR]-OLVSE_global_control%s"%stringnum
    globalcenteroidname = "[TR]-OLVSE_globalcenteroid%s"%stringnum



    # Definitions

    def norm_miris(l,c):
        return (l - c)*.08
    bpy.app.driver_namespace['norm_miris'] = norm_miris

    def rand_miris(min, seed, max=2):
        random.seed(seed)
        random_factor = random.uniform(min, max)
        return random_factor
    bpy.app.driver_namespace['rand_miris'] = rand_miris

    def normalizehoop(l,c):
        return (l-c)
    bpy.app.driver_namespace['normalizehoop'] = normalizehoop

    #Global control with centeroid link

    drv = centeroid.driver_add("translate_start_x")

    var = drv.driver.variables.new()
    var.name = "trans_x"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % globalcenteroidname
    drv.driver.expression = '%s' % var.name

    drv = centeroid.driver_add("translate_start_y")

    var = drv.driver.variables.new()
    var.name = "trans_y"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % globalcenteroidname
    drv.driver.expression = '%s' % var.name


    #Global control with core driver link

    drv = core.driver_add("translate_start_x")

    var = drv.driver.variables.new()
    var.name = "trans_x"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % globctrlname
    drv.driver.expression = '%s' % var.name

    drv = core.driver_add("translate_start_y")

    var = drv.driver.variables.new()
    var.name = "trans_y"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % globctrlname
    drv.driver.expression = '%s' % var.name

    drv = core.driver_add("scale_start_x")

    var = drv.driver.variables.new()
    var.name = "scale_x"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % globctrlname
    drv.driver.expression = '(.56*.1)*9.25*%s' % var.name

    drv = core.driver_add("scale_start_y")

    var = drv.driver.variables.new()
    var.name = "scale_y"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_y" % globctrlname
    drv.driver.expression = '(1*.1)*9*%s' % var.name

    drv = core.driver_add("rotation_start")

    var = drv.driver.variables.new()
    var.name = "rotation"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].rotation_start" % globctrlname
    drv.driver.expression = '%s' % var.name

    drv = core.driver_add("color_multiply")

    var = drv.driver.variables.new()
    var.name = "cmult"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].color_multiply" % globctrlname
    drv.driver.expression = '%s' % var.name

    drv = core.driver_add("color_saturation")

    var = drv.driver.variables.new()
    var.name = "csatu"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].color_saturation" % globctrlname
    drv.driver.expression = '%s' % var.name


    # Tail link
        
    drv = tail.driver_add("translate_start_x")

    var = drv.driver.variables.new()
    var.name = "cpx"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % centername

    drv = tail.driver_add("translate_start_x")

    var = drv.driver.variables.new()
    var.name = "clx"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % corename

    drv.driver.expression = 'cpx - clx'

    drv = tail.driver_add("translate_start_y")

    var = drv.driver.variables.new()
    var.name = "cpy"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % centername

    drv = tail.driver_add("translate_start_y")

    var = drv.driver.variables.new()
    var.name = "cly"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename

    drv.driver.expression = 'cpy - cly'



    # all coreobj driver link

    for coreobjs in coreobj:

        drv = coreobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % corename


        drv.driver.expression = "%s" %var.name

        drv = coreobjs.driver_add("translate_start_y")

        var = drv.driver.variables.new()
        var.name = "ly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename

        drv.driver.expression = "%s" %var.name
        
        drv = coreobjs.driver_add("scale_start_x")

        var = drv.driver.variables.new()
        var.name = "scale_x"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename


        drv.driver.expression = "%s" %var.name

        drv = coreobjs.driver_add("scale_start_y")

        var = drv.driver.variables.new()
        var.name = "scale_y"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_y" % corename

        drv.driver.expression = "%s" %var.name
        
        drv = coreobjs.driver_add("rotation_start")

        var = drv.driver.variables.new()
        var.name = "rotation"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].rotation_start" % corename


        drv.driver.expression = "%s" %var.name

        drv = coreobjs.driver_add("color_multiply")

        var = drv.driver.variables.new()
        var.name = "cmult"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_multiply" % corename

        drv.driver.expression = "%s" %var.name
        
        drv = coreobjs.driver_add("color_saturation")

        var = drv.driver.variables.new()
        var.name = "csatu"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_saturation" % corename
        drv.driver.expression = '%s' % var.name
        
    # all spreadobj driver link

    for spreadobjs in spreadobj:
        
        drv = spreadobjs.driver_add("translate_start_y")

        var = drv.driver.variables.new()
        var.name = "ly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename

        drv.driver.expression = "%s" %var.name
        
        drv = spreadobjs.driver_add("color_multiply")

        var = drv.driver.variables.new()
        var.name = "cmult"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_multiply" % corename
        
        drv = spreadobjs.driver_add("color_multiply")

        var = drv.driver.variables.new()
        var.name = "csx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename


        drv.driver.expression = "cmult * csx*2.5"

        
        drv = spreadobjs.driver_add("color_saturation")

        var = drv.driver.variables.new()
        var.name = "csatu"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_saturation" % corename
        drv.driver.expression = '%s' % var.name
        
    # all coreextraobj link

    for coreextraobjs in coreextraobj:

        drv = coreextraobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % corename


        drv.driver.expression = "%s" %var.name

        drv = coreextraobjs.driver_add("translate_start_y")

        var = drv.driver.variables.new()
        var.name = "ly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename

        drv.driver.expression = "%s" %var.name
        
        drv = coreextraobjs.driver_add("scale_start_x")

        var = drv.driver.variables.new()
        var.name = "scale_x"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename


        drv.driver.expression = "(0.56*.1)*90 * %s" %var.name

        drv = coreextraobjs.driver_add("scale_start_y")

        var = drv.driver.variables.new()
        var.name = "scale_y"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_y" % corename

        drv.driver.expression = "(1*.1)*50 * %s" %var.name
        
        drv = coreextraobjs.driver_add("rotation_start")

        var = drv.driver.variables.new()
        var.name = "rotation"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].rotation_start" % corename


        drv.driver.expression = "%s" %var.name



        drv = coreextraobjs.driver_add("color_multiply")

        var = drv.driver.variables.new()
        var.name = "cmult"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_multiply" % corename

        drv.driver.expression = "%s" %var.name
        
        drv = coreextraobjs.driver_add("color_saturation")

        var = drv.driver.variables.new()
        var.name = "csatu"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_saturation" % corename
        drv.driver.expression = '%s' % var.name    
        
    # all primestrixobj links

    for primestrixobjs in primestrixobj:

        itrbl = primestrixobjs.channel

        ########### Translate

        drv = primestrixobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % corename

        drv = primestrixobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "tx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % tailname

        drv.driver.expression = ('norm_miris(lx,tx) * ((%d/2)-3)+tx') % itrbl

        drv = primestrixobjs.driver_add("translate_start_y")

        var = drv.driver.variables.new()
        var.name = "ly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename

        drv = primestrixobjs.driver_add("translate_start_y")

        var = drv.driver.variables.new()
        var.name = "ty"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % tailname

        drv.driver.expression = ('norm_miris(ly,ty) * ((%d/2)-3)+ty') % itrbl
        
        ########### Random Scale (The Scale of difference should be 5.5 for making aspect ratio correct. e.g: 3-8.5 = 5.5)
            
        drv = primestrixobjs.driver_add("scale_start_x")

        var = drv.driver.variables.new()
        var.name = "sx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename

        drv.driver.expression = ('((0.56*.1) * sx *rand_miris(.1,%d,1))*8')%itrbl
        
        
        drv = primestrixobjs.driver_add("scale_start_y")

        var = drv.driver.variables.new()
        var.name = "sy"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_y" % corename

        drv.driver.expression = ('((1*.1) * sy *rand_miris(.1,%d,1))*4.5')%itrbl
        
        drv = primestrixobjs.driver_add("color_multiply")

        var = drv.driver.variables.new()
        var.name = "cmult"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_multiply" % corename

        drv.driver.expression = "%s" %var.name
        
        drv = primestrixobjs.driver_add("color_saturation")

        var = drv.driver.variables.new()
        var.name = "csatu"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_saturation" % corename
        drv.driver.expression = '%s' % var.name
        
    # all secondstrixobj links

    for secondstrixobjs in secondstrixobj:

        itrbl = secondstrixobjs.channel

        ########### Translate

        drv = secondstrixobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % corename

        drv = secondstrixobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "tx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % tailname

        drv.driver.expression = ('norm_miris(lx,tx) * ((%d*.32)-2)+tx') % itrbl

        drv = secondstrixobjs.driver_add("translate_start_y")

        var = drv.driver.variables.new()
        var.name = "ly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename

        drv = secondstrixobjs.driver_add("translate_start_y")

        var = drv.driver.variables.new()
        var.name = "ty"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % tailname

        drv.driver.expression = ('norm_miris(ly,ty) * ((%d*.32)-2)+ty') % itrbl
        
        ########### Random Scale (The Scale of difference should be 5.5 for making aspect ratio correct. e.g: 4-9.5 = 5.5)
            
        drv = secondstrixobjs.driver_add("scale_start_x")

        var = drv.driver.variables.new()
        var.name = "sx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename

        drv.driver.expression = ('((0.56*.1) * sx *rand_miris(.1,%d,1))*9.5')%itrbl
        
        drv = secondstrixobjs.driver_add("scale_start_y")

        var = drv.driver.variables.new()
        var.name = "sy"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_y" % corename

        drv.driver.expression = ('((1*.1) * sy *rand_miris(.1,%d,1))*5.5')%itrbl
        
        drv = secondstrixobjs.driver_add("color_multiply")

        var = drv.driver.variables.new()
        var.name = "cmult"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_multiply" % corename

        drv.driver.expression = "%s" %var.name
        
        drv = secondstrixobjs.driver_add("color_saturation")

        var = drv.driver.variables.new()
        var.name = "csatu"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_saturation" % corename
        drv.driver.expression = '%s' % var.name
        
        
    # all spriteaobj links

    for spriteaobjs in spriteaobj:

        itrbl = spriteaobjs.channel

        ########### Translate

        drv = spriteaobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % corename

        drv = spriteaobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "tx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % tailname

        drv.driver.expression = ('norm_miris(lx,tx) * ((%d/2)-3)+tx') % itrbl

        drv = spriteaobjs.driver_add("translate_start_y")

        var = drv.driver.variables.new()
        var.name = "ly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename

        drv = spriteaobjs.driver_add("translate_start_y")

        var = drv.driver.variables.new()
        var.name = "ty"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % tailname

        drv.driver.expression = ('norm_miris(ly,ty) * ((%d/2)-3)+ty') % itrbl
        
        ########### Random Scale (The Scale of difference should be 5.5 for making aspect ratio correct. e.g: 8-13.5 = 5.5)
            
        drv = spriteaobjs.driver_add("scale_start_x")

        var = drv.driver.variables.new()
        var.name = "sx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename

        drv.driver.expression = ('((0.56*.1) * sx *rand_miris(.1,%d,1))*13.5')%itrbl
        
        drv = spriteaobjs.driver_add("scale_start_y")

        var = drv.driver.variables.new()
        var.name = "sy"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_y" % corename

        drv.driver.expression = ('((1*.1) * sy *rand_miris(.1,%d,1))*8')%itrbl
        
        drv = spriteaobjs.driver_add("color_multiply")

        var = drv.driver.variables.new()
        var.name = "cmult"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_multiply" % corename

        drv.driver.expression = "%s" %var.name
        
        drv = spriteaobjs.driver_add("color_saturation")

        var = drv.driver.variables.new()
        var.name = "csatu"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_saturation" % corename
        drv.driver.expression = '%s' % var.name
        
        
    # all anamstixobj links

    for anamstixobjs in anamstixobj:

        itrbl = anamstixobjs.channel

        ########### Translate

        drv = anamstixobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % corename

        drv = anamstixobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "tx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % tailname

        drv.driver.expression = ('norm_miris(lx,tx) * ((%d*.8)-2)+tx') % itrbl
        
        drv = anamstixobjs.driver_add("translate_start_y")

        var = drv.driver.variables.new()
        var.name = "ly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename

        drv.driver.expression = ('ly')


        
        ########### Random Scale
            
        drv = anamstixobjs.driver_add("scale_start_x")

        var = drv.driver.variables.new()
        var.name = "sx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename

        drv.driver.expression = ('((0.56*.1) * sx *rand_miris(.1,%d,1))*10')%itrbl
        
        drv = anamstixobjs.driver_add("scale_start_y")

        var = drv.driver.variables.new()
        var.name = "sy"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_y" % corename

        drv.driver.expression = ('((1*.1) * sy *rand_miris(.1,%d,1))*10')%itrbl
        
        drv = anamstixobjs.driver_add("color_multiply")

        var = drv.driver.variables.new()
        var.name = "cmult"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_multiply" % corename

        drv.driver.expression = "%s" %var.name
        
        drv = anamstixobjs.driver_add("color_saturation")

        var = drv.driver.variables.new()
        var.name = "csatu"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_saturation" % corename
        drv.driver.expression = '%s' % var.name
        
        
    # all ghostXobj driver link

    for ghostXobjs in ghostXobj:

        drv = ghostXobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % corename


        drv.driver.expression = "lx"

        drv = ghostXobjs.driver_add("translate_start_y")

        var = drv.driver.variables.new()
        var.name = "ly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename

        drv.driver.expression = "ly"

        #############

        drv = ghostXobjs.driver_add("rotation_start")

        var = drv.driver.variables.new()
        var.name = "ly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename
        
        drv = ghostXobjs.driver_add("rotation_start")

        var = drv.driver.variables.new()
        var.name = "cy"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % centername
   
        drv.driver.expression = "-(ly-cy)"

####################

        drv = ghostXobjs.driver_add("scale_start_x")

        var = drv.driver.variables.new()
        var.name = "tlx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % tailname

        var = drv.driver.variables.new()
        var.name = "tly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % tailname

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename

        drv.driver.expression = "0 if tlx==0 and tly==0 else ((tlx*lx*2)*.06)"

        drv = ghostXobjs.driver_add("scale_start_y")

        var = drv.driver.variables.new()
        var.name = "tlx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % tailname

        drv = ghostXobjs.driver_add("scale_start_y")

        var = drv.driver.variables.new()
        var.name = "tly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % tailname

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename

        drv.driver.expression = "0 if tlx==0 and tly==0 else ((tlx*lx*2)*.06)"
        
        drv = ghostXobjs.driver_add("color_multiply")

        var = drv.driver.variables.new()
        var.name = "cmult"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_multiply" % corename

        drv.driver.expression = "%s" %var.name
        
        drv = ghostXobjs.driver_add("color_saturation")

        var = drv.driver.variables.new()
        var.name = "csatu"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_saturation" % corename
        drv.driver.expression = '%s' % var.name
        
    # all ghostYobj driver link

    for ghostYobjs in ghostYobj:

        drv = ghostYobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % corename


        drv.driver.expression = "lx"

        drv = ghostYobjs.driver_add("translate_start_y")

        var = drv.driver.variables.new()
        var.name = "ly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename

        drv.driver.expression = "ly"

        #############
       
        drv = ghostYobjs.driver_add("rotation_start")

        var = drv.driver.variables.new()
        var.name = "ly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename
        
        drv = ghostYobjs.driver_add("rotation_start")

        var = drv.driver.variables.new()
        var.name = "cy"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % centername
        
        drv.driver.expression = "ly-cy"




        drv = ghostYobjs.driver_add("scale_start_x")

        var = drv.driver.variables.new()
        var.name = "tlx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % tailname

        var = drv.driver.variables.new()
        var.name = "tly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % tailname

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename

        drv.driver.expression = "0 if tlx==0 and tly==0 else -((tlx*lx*2)*.06)"

        drv = ghostYobjs.driver_add("scale_start_y")

        var = drv.driver.variables.new()
        var.name = "tlx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % tailname

        var = drv.driver.variables.new()
        var.name = "tly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % tailname

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename

        drv.driver.expression = "0 if tlx==0 and tly==0 else -((tlx*lx*2)*.06)"
        
            
        drv = ghostYobjs.driver_add("color_multiply")

        var = drv.driver.variables.new()
        var.name = "cmult"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_multiply" % corename

        drv.driver.expression = "%s" %var.name
        
        drv = ghostYobjs.driver_add("color_saturation")

        var = drv.driver.variables.new()
        var.name = "csatu"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_saturation" % corename
        drv.driver.expression = '%s' % var.name
        
    # all anamghostXobj driver link

    for anamghostXobjs in anamghostXobj:

        drv = anamghostXobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % corename


        drv.driver.expression = "lx"

        drv = anamghostXobjs.driver_add("translate_start_y")

        var = drv.driver.variables.new()
        var.name = "ly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename

        drv.driver.expression = "ly"

        drv = anamghostXobjs.driver_add("scale_start_x")

        var = drv.driver.variables.new()
        var.name = "tlx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % tailname

        var = drv.driver.variables.new()
        var.name = "tly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % tailname

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename

        drv.driver.expression = "0 if tlx==0 and tly==0 else ((tlx*lx*3)*.06)"

        drv = anamghostXobjs.driver_add("scale_start_y")

        var = drv.driver.variables.new()
        var.name = "tlx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % tailname

        drv = anamghostXobjs.driver_add("scale_start_y")

        var = drv.driver.variables.new()
        var.name = "tly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % tailname

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename

        drv.driver.expression = "0 if tlx==0 and tly==0 else ((tlx*lx*3)*.06)"
        
        drv = anamghostXobjs.driver_add("color_multiply")

        var = drv.driver.variables.new()
        var.name = "cmult"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_multiply" % corename

        drv.driver.expression = "%s" %var.name
        
        drv = anamghostXobjs.driver_add("color_saturation")

        var = drv.driver.variables.new()
        var.name = "csatu"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_saturation" % corename
        drv.driver.expression = '%s' % var.name
        
    # all anamghostYobj driver link

    for anamghostYobjs in anamghostYobj:

        drv = anamghostYobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % corename


        drv.driver.expression = "lx"

        drv = anamghostYobjs.driver_add("translate_start_y")

        var = drv.driver.variables.new()
        var.name = "ly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename

        drv.driver.expression = "ly"


        drv = anamghostYobjs.driver_add("scale_start_x")

        var = drv.driver.variables.new()
        var.name = "tlx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % tailname

        var = drv.driver.variables.new()
        var.name = "tly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % tailname

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename

        drv.driver.expression = "0 if tlx==0 and tly==0 else -((tlx*lx*3)*.06)"

        drv = anamghostYobjs.driver_add("scale_start_y")

        var = drv.driver.variables.new()
        var.name = "tlx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % tailname

        var = drv.driver.variables.new()
        var.name = "tly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % tailname

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename

        drv.driver.expression = "0 if tlx==0 and tly==0 else -((tlx*lx*3)*.06)"
        
            
        drv = anamghostYobjs.driver_add("color_multiply")

        var = drv.driver.variables.new()
        var.name = "cmult"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_multiply" % corename

        drv.driver.expression = "%s" %var.name
        
        drv = anamghostYobjs.driver_add("color_saturation")

        var = drv.driver.variables.new()
        var.name = "csatu"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_saturation" % corename
        drv.driver.expression = '%s' % var.name    
        
    # all gritmaskobj link

    drv = gritmaskobj.driver_add("translate_start_x")

    var = drv.driver.variables.new()
    var.name = "lx"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % corename


    drv.driver.expression = "%s" %var.name

    drv = gritmaskobj.driver_add("translate_start_y")

    var = drv.driver.variables.new()
    var.name = "ly"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename

    drv.driver.expression = "%s" %var.name

    drv = gritmaskobj.driver_add("scale_start_x")

    var = drv.driver.variables.new()
    var.name = "scale_x"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename


    drv.driver.expression = "(0.56*.1)*40 * %s" %var.name

    drv = gritmaskobj.driver_add("scale_start_y")

    var = drv.driver.variables.new()
    var.name = "scale_y"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_y" % corename

    drv.driver.expression = "(1*.1)*40 * %s" %var.name


    drv = gritmaskobj.driver_add("color_multiply")

    var = drv.driver.variables.new()
    var.name = "cmult"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].color_multiply" % corename

    drv.driver.expression = "%s" %var.name

    drv = gritmaskobj.driver_add("color_saturation")

    var = drv.driver.variables.new()
    var.name = "csatu"
    var.type = "SINGLE_PROP"
    target = var.targets[0]
    target.id_type = 'SCENE'
    target.id = bpy.data.scenes[bpy.context.scene.name]
    target.data_path = "sequence_editor.sequences_all[\"%s\"].color_saturation" % corename
    drv.driver.expression = '%s' % var.name

    #all extraobj driver link

    for extraobjs in extraobj:
        
        itrblextra = extraobjs.channel
        
        drv = extraobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "lx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % corename
        
        drv = extraobjs.driver_add("translate_start_x")

        var = drv.driver.variables.new()
        var.name = "cx"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_x" % centername
        
        drv.driver.expression = ('-lx + (%d/2-1) + cx') % itrblextra
        
        drv = extraobjs.driver_add("translate_start_y")
        
       
        var = drv.driver.variables.new()
        var.name = "ly"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % corename
        
        var = drv.driver.variables.new()
        var.name = "cy"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].translate_start_y" % centername
        
        drv.driver.expression = ('-ly + (%d/2-1) + cy') % itrblextra
            
        drv = extraobjs.driver_add("scale_start_x")

        var = drv.driver.variables.new()
        var.name = "scale_x"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_x" % corename
        drv.driver.expression = ('%s*.5 * ((%d/2-1))') % (var.name, itrblextra)
        
        drv = extraobjs.driver_add("scale_start_y")

        var = drv.driver.variables.new()
        var.name = "scale_y"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].scale_start_y" % corename
        drv.driver.expression = ('%s*.5 * ((%d/2-1))') % (var.name, itrblextra)
        
        drv = extraobjs.driver_add("rotation_start")

        var = drv.driver.variables.new()
        var.name = "rotation"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].rotation_start" % corename
        drv.driver.expression = ('%s + (%d/2-1)') % (var.name, itrblextra)
        
        drv = extraobjs.driver_add("color_multiply")

        var = drv.driver.variables.new()
        var.name = "cmult"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_multiply" % corename
        drv.driver.expression = '%s' % var.name
        
        drv = extraobjs.driver_add("color_saturation")

        var = drv.driver.variables.new()
        var.name = "csatu"
        var.type = "SINGLE_PROP"
        target = var.targets[0]
        target.id_type = 'SCENE'
        target.id = bpy.data.scenes[bpy.context.scene.name]
        target.data_path = "sequence_editor.sequences_all[\"%s\"].color_saturation" % corename
        drv.driver.expression = '%s' % var.name
    bpy.ops.sequencer.refresh_all()
        
# Cleaning Driver Functions

def main_del(context):

    # OBJECT VAR CALLS

    bpyobj = bpy.context.scene.sequence_editor.sequences_all
    stringnum = "%s" % context.scene.sequence_editor.active_strip.name

    flare  = bpyobj["[TR]-OLVSE_Coreobject_1%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_2%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_3%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_4%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_5%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_6%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_7%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_8%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_9%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_10%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_11%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_12%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_13%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_14%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_14%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_15%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_14%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_15%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_1%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_2%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_3%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_4%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_5%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_6%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_7%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_8%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_9%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_10%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_11%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_12%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_13%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_14%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_15%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_16%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_17%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_18%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_19%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_20%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_21%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_22%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_23%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_24%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_25%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_26%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_27%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_28%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_14%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_14%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_14%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_15%s"%stringnum], bpyobj["[TR]-OLVSE_Grit_Mask%s"%stringnum], bpyobj["[TR]-OLVSE_primary_hoopx%s"%stringnum], bpyobj["[TR]-OLVSE_secondary_hoopx%s"%stringnum], bpyobj["[TR]-OLVSE_ghost1_x%s"%stringnum], bpyobj["[TR]-OLVSE_ghost2_x%s"%stringnum], bpyobj["[TR]-OLVSE_ghost3_x%s"%stringnum], bpyobj["[TR]-OLVSE_ghost4_x%s"%stringnum], bpyobj["[TR]-OLVSE_ghost5_x%s"%stringnum], bpyobj["[TR]-OLVSE_primary_hoopy%s"%stringnum], bpyobj["[TR]-OLVSE_secondary_hoopy%s"%stringnum], bpyobj["[TR]-OLVSE_ghost1_y%s"%stringnum], bpyobj["[TR]-OLVSE_ghost2_y%s"%stringnum], bpyobj["[TR]-OLVSE_ghost3_y%s"%stringnum], bpyobj["[TR]-OLVSE_ghost4_y%s"%stringnum], bpyobj["[TR]-OLVSE_ghost5_y%s"%stringnum], bpyobj["[TR]-OLVSE_Core%s"%stringnum], bpyobj["[TR]-OLVSE_Tail%s"%stringnum], bpyobj["[TR]-OLVSE_centeroid%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_1%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_2%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_3%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_4%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_5%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_6%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_7%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_1%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_2%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_3%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_4%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_5%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_6%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_7%s"%stringnum]

    for flares in flare:
        if flares.mute == True:
            flares.driver_remove("translate_start_x")
            flares.driver_remove("translate_start_y")
            flares.driver_remove("scale_start_x")
            flares.driver_remove("scale_start_y")
            flares.driver_remove("rotation_start")
            flares.driver_remove("color_multiply")
            flares.driver_remove("color_saturation")
    bpy.ops.sequencer.refresh_all()
            


# Deleting Driver Functions

def main_delall(context):

    # OBJECT VAR CALLS

    bpyobj = bpy.context.scene.sequence_editor.sequences_all
    stringnum = "%s" % context.scene.sequence_editor.active_strip.name

    flare  = bpyobj["[TR]-OLVSE_Coreobject_1%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_2%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_3%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_4%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_5%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_6%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_7%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_8%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_9%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_10%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_11%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_12%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_13%s"%stringnum], bpyobj["[TR]-OLVSE_Coreobject_14%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_14%s"%stringnum], bpyobj["[TR]-OLVSE_spreaadobj_15%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_14%s"%stringnum], bpyobj["[TR]-OLVSE_coreextraobj_15%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_1%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_2%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_3%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_4%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_5%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_6%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_7%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_8%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_9%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_10%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_11%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_12%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_13%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_14%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_15%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_16%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_17%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_18%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_19%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_20%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_21%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_22%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_23%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_24%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_25%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_26%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_27%s"%stringnum], bpyobj["[TR]-OLVSE_Strix_28%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_Spriteobj_14%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_Anamstrixobj_14%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_1%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_2%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_3%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_4%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_5%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_6%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_7%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_8%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_9%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_10%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_11%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_12%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_13%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_14%s"%stringnum], bpyobj["[TR]-OLVSE_Extraobj_15%s"%stringnum], bpyobj["[TR]-OLVSE_Grit_Mask%s"%stringnum], bpyobj["[TR]-OLVSE_primary_hoopx%s"%stringnum], bpyobj["[TR]-OLVSE_secondary_hoopx%s"%stringnum], bpyobj["[TR]-OLVSE_ghost1_x%s"%stringnum], bpyobj["[TR]-OLVSE_ghost2_x%s"%stringnum], bpyobj["[TR]-OLVSE_ghost3_x%s"%stringnum], bpyobj["[TR]-OLVSE_ghost4_x%s"%stringnum], bpyobj["[TR]-OLVSE_ghost5_x%s"%stringnum], bpyobj["[TR]-OLVSE_primary_hoopy%s"%stringnum], bpyobj["[TR]-OLVSE_secondary_hoopy%s"%stringnum], bpyobj["[TR]-OLVSE_ghost1_y%s"%stringnum], bpyobj["[TR]-OLVSE_ghost2_y%s"%stringnum], bpyobj["[TR]-OLVSE_ghost3_y%s"%stringnum], bpyobj["[TR]-OLVSE_ghost4_y%s"%stringnum], bpyobj["[TR]-OLVSE_ghost5_y%s"%stringnum], bpyobj["[TR]-OLVSE_Core%s"%stringnum], bpyobj["[TR]-OLVSE_Tail%s"%stringnum], bpyobj["[TR]-OLVSE_centeroid%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_1%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_2%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_3%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_4%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_5%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_6%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghostx_7%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_1%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_2%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_3%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_4%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_5%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_6%s"%stringnum], bpyobj["[TR]-OLVSE_anam_ghosty_7%s"%stringnum]


    for flares in flare:
        
        flares.driver_remove("translate_start_x")
        flares.driver_remove("translate_start_y")
        flares.driver_remove("scale_start_x")
        flares.driver_remove("scale_start_y")
        flares.driver_remove("rotation_start")
        flares.driver_remove("color_multiply")
        flares.driver_remove("color_saturation")
    bpy.ops.sequencer.refresh_all()       




class OpticalFlare(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "sequencer.opticalflare"
    bl_label = "Optical Flare"


    def execute(self, context):
        main(context)
        return {'FINISHED'}
    
class OpticalFlareDel(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "sequencer.opticalflaredel"
    bl_label = "Optical Flare Del"


    def execute(self, context):
        main_del(context)
        return {'FINISHED'}
    
class OpticalFlareDelall(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "sequencer.opticalflaredelall"
    bl_label = "Optical Flare Delall"


    def execute(self, context):
        main_delall(context)
        return {'FINISHED'}    
    
#UI
class OpticalFlarePanel(bpy.types.Panel):
    
    '''Optical Flare Panel'''
    
    bl_space_type = "SEQUENCE_EDITOR"
    bl_region_type = "UI"
    bl_label = "Optical Flare"
    bl_idname = "SEQUENCER_OT_opticalflare"
    
    def draw(self, context):
        layout = self.layout
        
        split = layout.split(percentage=0.3)
        split.label(text="Flare Num:")
        split.prop(context.scene.sequence_editor.active_strip, "name", text="")
        layout.operator('sequencer.opticalflare',
        text='Create links', icon='PLUGIN')
        layout.operator('sequencer.opticalflaredel',
        text='Clean links', icon='FILE_TICK')
        layout.operator('sequencer.opticalflaredelall',
        text='Delete links', icon='CANCEL')
        
      

def register():
    
    
    bpy.utils.register_class(OpticalFlare)
    bpy.utils.register_class(OpticalFlareDel)
    bpy.utils.register_class(OpticalFlareDelall)   
    bpy.utils.register_class(OpticalFlarePanel)

def unregister():
    
    bpy.utils.unregister_class(OpticalFlare)
    bpy.utils.unregister_class(OpticalFlareDel) 
    bpy.utils.unregister_class(OpticalFlareDelall)  
    bpy.utils.unregister_class(OpticalFlarePanel)
    
    
if __name__ == "__main__":
    register()
