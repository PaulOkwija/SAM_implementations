from models.segment_anything import build_sam as sm
from models.segment_anything_samus.build_sam_us import samus_model_registry
from models.segment_anything_samus_autoprompt.build_samus import autosamus_model_registry
from models.medsam import build_medsam as mdsm
# import models.samed.sam_lora_image_encoder as lora 


def get_model(modelname="SAM", input_size=256, ckpt=None, opt=None, lora_cpt=None):
    if modelname == "SAM":
        model = sm.sam_model_registry['vit_b'](checkpoint=ckpt)
    elif modelname == "SAMUS":
        model = samus_model_registry['vit_b'](input_size, checkpoint=ckpt)
    elif modelname == "MedSAM":
        model = mdsm.sam_model_registry['vit_b'](checkpoint=ckpt)
    elif modelname == "AutoSAMUS":
        model = autosamus_model_registry['vit_b'](input_size, checkpoint=opt.load_path)
    else:
        raise RuntimeError("Could not find the model:", modelname)
    return model
