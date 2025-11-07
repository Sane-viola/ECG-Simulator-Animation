# 🫀 ECG Loader Animation Generator

A smooth, minimal **ECG (electrocardiogram) waveform animation** built in Python using `matplotlib`.
This project generates a **slow, looping ECG GIF** ideal for use as a **website loader**, **medical animation**, or **UI element**.


![ecg_loader](https://github.com/user-attachments/assets/b59a4224-c2ea-459a-88b7-79ca288f210b)

---

## 🎬 Preview

The animation produces a **red ECG trace** with:

* Reduced **R** and **S** peak amplitudes
* A **longer, negative T wave**
* **More space** between heartbeats
* **Smooth, continuous motion** ideal for digital interfaces

---

## 🧠 Features

✅ Smooth real-time ECG animation
✅ Custom waveform shaping (R, S, and T wave adjustments)
✅ Configurable duration and frame rate
✅ Exports as an optimized **GIF** for web use
✅ Clean, white background and anti-aliased trace

---

## 🛠️ Requirements

Install dependencies before running the script:

```bash
pip install numpy matplotlib
```

---

## 🚀 Usage

Run the script to generate the ECG animation:

```bash
python ecg_loader.py
```

Once complete, the generated file will be:

```
ecg_loader.gif
```

The script will print the configuration details:

* Duration and FPS
* Waveform parameters (R, S, and T characteristics)

---

## ⚙️ Customization

You can tweak parameters inside the script:

| Parameter          | Description                       | Default                          |
| ------------------ | --------------------------------- | -------------------------------- |
| `duration`         | Length of one full animation loop | `10.0` seconds                   |
| `fps`              | Frames per second                 | `30`                             |
| `R wave amplitude` | Peak height                       | `0.35`                           |
| `S wave amplitude` | Negative dip                      | `0.05`                           |
| `T wave`           | Longer, negative wave for realism | `0.12 amplitude, 200ms duration` |

---

## 📦 Output Example

> The output file `ecg_loader.gif` is an elegant red ECG trace, perfect for embedding in websites, dashboards, or UI loaders.

---

## 🧩 DEPENDENCIES 
* **Python 3**
* **NumPy** — waveform generation
* **Matplotlib** — rendering & animation
* **PillowWriter** — GIF export
---

## 📄 License

This project is released under the **APACHE LICENSE** — feel free to use, modify, and share.

---

## 💡 Author

Developed by *Sane Viola* — inspired by the beauty of biomedical signals and clean visual design.

