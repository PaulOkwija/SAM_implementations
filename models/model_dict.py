from models.segment_anything.build_sam import sam_model_registry as sm
from models.segment_anything_samus.build_sam_us import samus_model_registry
from models.segment_anything_samus_autoprompt.build_samus import autosamus_model_registry
from models.medsam.build_medsam import sam_model_registry as mdsm
# import models.samed.sam_lora_image_encoder as lora 


def get_model(modelname="SAM", input_size=256, ckpt=None, opt=None, lora_cpt=None):
    if modelname == "SAM":
        model = sm['vit_b'](checkpoint=ckpt)
    elif modelname == "SAMUS":
        model = samus_model_registry['vit_b'](input_size, checkpoint=ckpt)
    elif modelname == "MedSAM":
        model = mdsm['vit_b'](checkpoint=ckpt)
    elif modelname == "AutoSAMUS":
        model = autosamus_model_registry['vit_b'](input_size, checkpoint=opt.load_path)
    else:
        raise RuntimeError("Could not find the model:", modelname)
    return model
