
# CS 228 - Face Biometric Template Security

## Attack and Defense of Face Biometric Templates:
### Embedding Inversion vs. Cancelable Biometrics

**Course:** CS 228 - Biometric Security with AI  
**University:** San Jose State University  
**Semester:** Fall 2026

**Team Members:**
- Chinni Krishna Bhukya
- Yeraldin Crespo Valle

---

## 1. Project Overview

Face recognition systems often store numerical representations
of faces, known as biometric embeddings, instead of raw images.

Although these embeddings are useful for authentication,
they may still reveal sensitive identity information if
compromised.

Our project investigates two important aspects:

1. **Embedding Inversion Attacks:** Can an attacker recover
   identity information from stolen face embeddings?

2. **Cancelable Biometric Protection:** Can we transform
   biometric templates into revocable representations that
   reduce identity leakage while preserving authentication
   accuracy?

### Research Question

Can cancelable biometric template protection reduce identity
leakage from face embedding inversion attacks without
significantly degrading authentication performance?

### Project Nature

Attack and defend face biometric templates.

---

## 2. Checkpoint 1 - Current Progress

Checkpoint 1 focuses on establishing a reproducible
face-authentication baseline.

### Completed

- LFW dataset acquisition
- Dataset exploration and quality analysis
- Image preprocessing
- Pretrained FaceNet embedding extraction
- Genuine and impostor pair generation
- Cosine similarity-based face verification
- Authentication threshold calibration
- FAR, FRR, EER, and ROC-AUC evaluation
- Exploratory data analysis and visualization

### Future Work

- Optimization-based embedding inversion
- Learning-based embedding inversion
- Random projection template protection
- PolyProtect implementation
- Protected-template inversion evaluation
- Template unlinkability and revocability testing

---

## 3. Dataset

### Labeled Faces in the Wild (LFW)

Dataset source:
https://vis-www.cs.umass.edu/lfw/

The dataset contains face images collected from the web
and is widely used for face-recognition research.

### Dataset Statistics

| Property | Value |
|---|---|
| Dataset | LFW |
| Selected images | 4,324 |
| Selected identities | 158 |
| Minimum images per identity | 10 |
| Minimum images per identity observed | 10 |
| Median images per identity | 17 |
| Maximum images per identity | 530 |
| Exact image duplicates detected | 0 |
| Image dimensions used for analysis | 125 x 94 x 3 |
| Model input resolution | 160 x 160 |
| Embedding dimensions | 512 |

The dataset is downloaded automatically using
`sklearn.datasets.fetch_lfw_people`.

The dataset is not stored in this repository.

Dataset access and usage are subject to the original
LFW dataset terms.

---

## 4. Model Architecture

We use a pretrained FaceNet-style model for
face embedding extraction.

### Model Details

- Architecture: InceptionResnetV1
- Library: facenet-pytorch
- Pretrained weights: VGGFace2
- Embedding dimension: 512
- Similarity metric: Cosine similarity
- Authentication: Threshold-based verification

### Baseline Pipeline

```text
LFW Dataset
     |
     v
Image Preprocessing
     |
     v
Pretrained FaceNet
     |
     v
512-D Face Embeddings
     |
     v
Genuine / Impostor Comparisons
     |
     v
Cosine Similarity
     |
     v
Authentication Threshold
     |
     v
Accept / Reject
```

---

## 5. Experimental Setup

### Reproducibility

Random seed: `228`

The experiment uses separate validation and test
identity groups.

| Property | Value |
|---|---|
| Validation identities | 79 |
| Test identities | 79 |
| Validation genuine trials | 1,500 |
| Validation impostor trials | 1,500 |
| Test genuine trials | 1,500 |
| Test impostor trials | 1,500 |

The authentication threshold is selected using
validation data and evaluated on held-out test identities.

### Threshold Selection

The threshold is selected where validation FAR and FRR
are approximately equal.

Selected threshold:

`0.4868399500846863`

---

## 6. Baseline Results

### Face Verification Performance

| Metric | Result |
|---|---|
| False Acceptance Rate (FAR) | 0.47% |
| False Rejection Rate (FRR) | 5.00% |
| Equal Error Rate (EER) | 2.30% |
| ROC-AUC | 0.99696 |
| False acceptances | 7 / 1,500 |
| False rejections | 75 / 1,500 |
| Validation threshold | 0.48684 |

### Metric Definitions

**False Acceptance Rate (FAR)**

Percentage of impostor attempts incorrectly accepted.

**False Rejection Rate (FRR)**

Percentage of genuine attempts incorrectly rejected.

**Equal Error Rate (EER)**

Error rate at the operating point where FAR and FRR
are approximately equal.

**ROC-AUC**

Measures the model's ability to distinguish genuine
from impostor comparisons across thresholds.

### Preliminary Observations

- Genuine pairs generally produce higher cosine
  similarity than impostor pairs.
- The similarity distributions show some overlap.
- The dataset has substantial identity imbalance.
- Image brightness and contrast vary across samples.
- The selected threshold produces relatively low FAR
  but a higher FRR on the test set.

These results describe the unprotected baseline only.

---

## 7. Exploratory Data Analysis

The notebook performs:

1. Identity distribution analysis
2. Image brightness distribution
3. Image contrast analysis
4. Brightness versus contrast scatter analysis
5. Top-20 identity frequency analysis
6. Genuine versus impostor similarity analysis
7. FAR and FRR threshold analysis
8. ROC curve evaluation

Generated visualizations are saved in the `results/`
directory.

---

## 8. Installation and Execution

### Recommended Environment

Google Colab with a T4 GPU.

The checkpoint was run using:

- Python 3.13.16
- PyTorch 2.11.0+cu130
- Torchvision 0.26.0+cu130
- NumPy 2.1.3
- Pandas 2.2.3
- Scikit-learn 1.6.1
- Pillow 11.3.0

### Step 1 - Open Google Colab

https://colab.research.google.com/

### Step 2 - Upload the Notebook

Upload:

`CS228_Checkpoint1_Colab.ipynb`

### Step 3 - Enable GPU

Select:

Runtime > Change runtime type > T4 GPU

### Step 4 - Install FaceNet

The working Colab environment used:

```python
%pip install -q --no-deps facenet-pytorch
```

This avoids dependency changes to Colab's existing
PyTorch and Pillow installations.

Note: `--no-deps` bypasses dependency resolution.
The package versions must be compatible with the
runtime environment.

### Step 5 - Run the Notebook

Run all notebook cells sequentially.

The notebook will:

1. Load LFW automatically
2. Analyze dataset characteristics
3. Generate EDA plots
4. Load pretrained FaceNet weights
5. Extract face embeddings
6. Generate verification trials
7. Select the validation threshold
8. Evaluate the test set
9. Save results and figures

---

## 9. Output Files

The notebook generates files including:

```text
results/
    embeddings.npy
    metrics.json
    eda_univariate.png
    eda_bivariate.png
    eda_class_balance.png
    baseline_thresholds.png
    baseline_roc.png
```

`embeddings.npy` is generated locally and should not
be committed to the public repository.

The exact output filenames depend on the notebook version.

---

## 10. Limitations

- The experiment uses a filtered subset of LFW.
- Identity counts are imbalanced.
- The images are relatively low resolution.
- The current baseline uses resized face crops rather
  than a full landmark-based alignment pipeline.
- The pretrained model was trained externally on VGGFace2.
- Inversion attacks have not yet been implemented.
- Cancelable biometric protection has not yet been
  implemented.
- Results may differ across environments and versions.

---

## 11. Future Research

### Phase 1 - Embedding Inversion

Evaluate whether identity information can be recovered
from raw face embeddings using:

- Optimization-based inversion
- Learning-based inversion

### Phase 2 - Cancelable Biometrics

Evaluate protection techniques including:

- Random projection
- PolyProtect
- Optional BioHashing

### Phase 3 - Security Evaluation

Compare raw and protected templates using:

- Authentication FAR, FRR, and EER
- Identity leakage
- Reconstruction quality
- Template unlinkability
- Template revocability

---

## 12. References

1. G. B. Huang et al., "Labeled Faces in the Wild:
   A Database for Studying Face Recognition in
   Unconstrained Environments," 2007.

2. H. O. Shahreza and S. Marcel, "Template Inversion
   Attack against Face Recognition Systems using
   3D Face Reconstruction," ICCV, 2023.

3. V. Krivokuca Hahn and S. Marcel, "Towards Protecting
   Face Embeddings in Mobile Face Verification
   Scenarios," IEEE T-BIOM, 2022.

4. V. Krivokuca Hahn and S. Marcel, "Biometric Template
   Protection for Neural-Network-Based Face Recognition
   Systems: A Survey of Methods and Evaluation
   Techniques," IEEE TIFS, 2023.

---

## 13. Academic Information

This repository contains coursework developed for
CS 228: Biometric Security with AI at
San Jose State University.

The code and experiments are intended for academic
research and reproducibility.
