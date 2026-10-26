# DNA Direct Acoustic Scaling Model (Mass-to-Frequency Sonification)

An algorithmic framework that maps the four nitrogenous bases of DNA to absolute musical frequencies using unmanipulated physical mass ratios (Daltons to Hertz). By anchoring the physical midpoint of the genetic spectrum directly to Middle C, this model eliminates arbitrary human scaling parameters to discover natural acoustics embedded in subatomic physics.

## 🧬 Core Methodology

Unlike standard Parameter Mapping Sonification (PMSon) frameworks that arbitrarily map genetic sequences to western scales for aesthetic convenience, this project utilizes **Direct 1:1 Acoustic Scaling**. 

1. **Mass-to-Frequency Conversion:** 1 Dalton (Da) of physical molecular mass (calculated from exact subatomic proton and neutron counts) is mapped directly to 1 Hertz (Hz) of acoustic frequency.
2. **Audible Range Normalization:** Frequencies are shifted by a scale constant ($k = 2$) to optimize playback within the standard human vocal and instrumental octave.
3. **Midpoint Reference Calibration:** The mathematical midpoint of the absolute physical range sits at **131.12 Hz**, falling within a $0.22\%$ margin of error of a universal **C note** (C3 in physics tuning). Pinning this center to **Middle C (C4)** locks the structural rungs into a highly precise, conjunct musical scale:

| Base | Chemical Formula | Molecular Mass (Da) | Normalized Frequency (Hz) | Assigned Key |
| :--- | :--- | :--- | :--- | :--- |
| **Cytosine (C)** | C₄H₅N₃O | 111.10 Da | 222.20 Hz | **A3** |
| **Thymine (T)** | C₅H₆N₂O₂ | 126.11 Da | 252.22 Hz | **B3** (Leading Tone) |
| **Adenine (A)** | C₅H₅N₅ | 135.13 Da | 270.26 Hz | **C#4** |
| **Guanine (G)** | C₅H₅N₅O | 151.13 Da | 302.26 Hz | **D4** |

## 🎼 Structural & Harmonic Theorems

* **The Double-Helix Acoustic Drone:** When base pairs bond, their aggregate masses are virtually invariant. An A–T pair ($261.24\text{ Da}$) and a C–G pair ($262.23\text{ Da}$) share a structural mass uniformity of **$>99.62\%$**. The macro-structure of DNA acts as a physical acoustic drone, maintaining gravitational and vibrational consistency.
* **The Alternating Harmonic Symphony:** While the macro-structure hums at a stable baseline, individual rungs generate systematic tension and resolution:
  * **C–G Bonds** sound as an open, resonant **Perfect 4th** (A to D).
  * **A–T Bonds** sound as a dense, high-friction **Major 2nd** (B to C#).

## 🚀 Quick Start

### Prerequisites
* Python 3.x

### Running the Sonifier
Clone the repository and run the primary script to output the precise frequency and MIDI values derived from the biophysical constraints:

```bash
git clone https://github.com
cd dna-mass-sonification
python dna_sonifier.py
```

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details. This license allows for broad scientific adaptation provided that original attribution to the author is explicitly retained.

---
*Developed for publication alongside the formal preprint manuscript: "A Direct Acoustic Scaling Model of DNA: Mapping Molecular Mass to Uniform Structural Resonance".*
