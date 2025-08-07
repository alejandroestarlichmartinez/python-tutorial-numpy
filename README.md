# NumPy Mini-Tutorial 📈

A **tiny, self-contained introduction to NumPy**.  
Four short scripts that show how to create arrays, use universal functions (*ufuncs*), and visualise simple distributions.

> **Prerequisite:** basic Python knowledge.  
> Ideal companion to the [**Python Basics Tutorial**](../README.md).

---

## 🗂️ Contents

| File | Focus | Key lines |
|------|-------|-----------|
| **num_py.py** | Quick mash-up | Generate data, Creating 1-D / 2-D arrays, dtype, shape, reshape |
| **ufunc.py** | Universal functions | `np.add`, `np.sin`, broadcasting, element-wise ops |
| **distributions.py** | Random numbers | `np.random.normal`, histograms with Matplotlib |

*(Run them in this order or jump straight to the one you need.)*

---

## 🚀 Quick start

```bash
# 1 Clone / enter the repo root
git clone https://github.com/<your-user>/python-basics.git
cd python-basics

# 2 Activate the virtual environment you created for the main tutorial
#    or make a new one:
python -m venv .venv
# Windows: .\.venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 3 Install NumPy + plotting libs
pip install numpy matplotlib seaborn

# 4 Run the demos
python numpy/index.py
python numpy/ufunc.py
python numpy/distributions.py
python numpy/num_py.py
