
# Medical SAM Implementations Benchmark

This repository benchmarks and compares the performance of several Segment Anything Model (SAM) implementations on medical imaging data, with a focus on ultrasound segmentation. The workspace integrates and adapts code from multiple repositories, allowing for direct comparison and reproducibility.

## Included SAM Implementations

| Model/Implementation         | Description                                      | Original Repository Link | Performance (to be filled) |
|-----------------------------|--------------------------------------------------|-------------------------|----------------------------|
| Segment Anything (SAM)      | Original Meta AI SAM implementation              | [facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything) |                            |
| SAMed                       | Customized Segment Anything Model for Medical Image Segmentation | [hitachinsk/SAMed](https://github.com/hitachinsk/SAMed) |                      |
| SAMUS                       | SAM adapted for ultrasound segmentation (SAMUS)  | [xianlin7/SAMUS](https://github.com/xianlin7/SAMUS) |                                                    

> **Note:** Performance metrics for each model will be added after benchmarking.

## Usage

- Each implementation is organized in its own folder under `models/` or as a top-level directory.
- Notebooks and scripts are provided for running experiments and evaluating results.
- For details on folder structure and mapping to original repositories, see `models/README.md`.

## References

- [Segment Anything (Meta AI)](https://github.com/facebookresearch/segment-anything)
- [SAMed](https://github.com/xianlin7/SAMed)
- [SAMUS](https://github.com/xianlin7/SAMUS)
