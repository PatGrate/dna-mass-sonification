"""
DNA Sonifier: Direct 1:1 Acoustic Scaling Model
Translates raw genomic text into absolute frequencies and MIDI pitches.
"""
import math

class DNASonifier:
    def __init__(self):
        # Universal physical mass weights (Daltons / g/mol)
        self.masses = {
            'C': 111.10,
            'T': 126.11,
            'A': 135.13,
            'G': 151.13
        }
        # Direct 1:1 Acoustic Scaling Constant (Octave shift to standard range)
        self.k_factor = 2.0
        self.middle_c_standard = 261.63 # International standard for C4

    def calculate_frequencies(self):
        """Calculates raw physical frequencies in Hz."""
        return {base: round(mass * self.k_factor, 2) for base, mass in self.masses.items()}

    def frequency_to_midi(self, freq_hz):
        """Maps frequency to exact fractional MIDI pitch number."""
        # 69 is MIDI pitch for A4 (440Hz)
        return 12 * math.log2(freq_hz / 440.0) + 69

    def get_musical_mapping(self):
        """Resolves the precise note allocations based on mass ratios."""
        freqs = self.calculate_frequencies()
        mapping_summary = {}
        
        for base, hz in freqs.items():
            midi_pitch = self.frequency_to_midi(hz)
            # Find closest standard pitch distance relative to Middle C (MIDI 60)
            semitones_from_c4 = round(midi_pitch - 60)
            
            note_names = {
                -3: "A3", 
                -1: "B3", 
                1: "C#4", 
                2: "D4"
            }
            mapping_summary[base] = {
                "Frequency (Hz)": hz,
                "MIDI Pitch": round(midi_pitch, 2),
                "Assigned Key": note_names.get(semitones_from_c4, "Unknown")
            }
        return mapping_summary

# Execution Block
if __name__ == "__main__":
    sonifier = DNASonifier()
    results = sonifier.get_musical_mapping()
    
    print("=== DNA DIRECT ACOUSTIC SCALING RESULTS ===")
    for base, data in results.items():
        print(f"Base {base} -> {data['Assigned Key']} ({data['Frequency (Hz)']} Hz) | MIDI: {data['MIDI Pitch']}")
