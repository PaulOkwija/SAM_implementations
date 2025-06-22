
# Medical SAM Implementations Benchmark

This repository benchmarks and compares the performance of several Segment Anything Model (SAM) implementations on medical imaging data, with a focus on ultrasound segmentation. The workspace integrates and adapts code from multiple repositories, allowing for direct comparison and reproducibility.

## Included SAM Implementations

| Model/Implementation        | Description                                      | Original Repository Link | Implementation status | Performance (to be filled) |
|-----------------------------|--------------------------------------------------|-------------------------|----------------------------|----------------------------|
| Segment Anything (SAM)      | Original Meta AI SAM implementation              | [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything) |              Success              |                            |
| Segment Anything 2 (SAM2)      | Original Meta AI SAM2 implementation              | [facebookresearch/sam2](https://github.com/facebookresearch/sam2) |             Pending               |                            |
| SAMed                       | Customized Segment Anything Model for Medical Image Segmentation | [hitachinsk/SAMed](https://github.com/hitachinsk/SAMed) |           Failed           |                      |
| SAMUS                       | SAM adapted for ultrasound segmentation (SAMUS)  | [xianlin7/SAMUS](https://github.com/xianlin7/SAMUS) |         Success             |                      |                                                    

> **Note:** Performance metrics for each model will be added after benchmarking.

## Usage

- Each implementation is organized in its own folder under `models/` or as a top-level directory.
- Notebooks and scripts are provided for running experiments and evaluating results.
- For details on folder structure and mapping to original repositories, see `models/README.md`.

## References

- [Segment Anything (Meta AI)](https://ai.meta.com/research/publications/segment-anything/)
- [SAMed](https://arxiv.org/pdf/2304.13785)
- [SAMUS](https://arxiv.org/pdf/2309.06824)
- [SAM2](https://ai.meta.com/research/publications/sam-2-segment-anything-in-images-and-videos/)

## Yet into look into
-[MedSAM](https://github.com/bowang-lab/MedSAM/tree/main)
    -[Paper](https://www.nature.com/articles/s41467-024-44824-z)
    -[Updated-work](https://medsam2.github.io/)
-[SAM-Med2D](https://arxiv.org/pdf/2308.16184)

