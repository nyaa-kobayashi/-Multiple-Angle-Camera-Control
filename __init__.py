"""
Camera Control Prompt Node - ComfyUI Custom Node
Optimized for dx8152's MultiAngle LoRA

Author: Lorenzo Mercu
Optimized for: dx8152's MultiAngle LoRA
License: MIT
"""

from .camera_control_prompt_node import CameraControlPromptNode

NODE_CLASS_MAPPINGS = {
    "CameraControlPromptNode": CameraControlPromptNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CameraControlPromptNode": "Camera Control Prompt Generator"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
