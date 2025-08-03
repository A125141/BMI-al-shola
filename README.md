<img width="2872" height="1684" alt="sleekshot" src="https://github.com/user-attachments/assets/80ba92ae-b54b-446b-8916-872c29560afc" />


# BMI Calculator – Python GUI App

This is a simple and interactive Body Mass Index (BMI) calculator built using Python's Tkinter library, along with CustomTkinter for a modern dark-themed interface. The app allows users to input height and weight, select gender, and view their BMI with visual feedback.

---

## Features

- Real-time BMI calculation based on height and weight.
- Dynamic sliders to adjust height (cm) and weight (kg).
- Gender selection (Male/Female) with specific BMI interpretation.
- Visual representation using an adjustable character image.
- Clean and responsive dark-themed UI using CustomTkinter.
- Clickable info icon that opens the project’s GitHub repo.

---

## How It Works

1. Enter your height and weight using the sliders or text inputs.
2. Choose your gender using the radio buttons.
3. Click the “View BMI” button to calculate your BMI.
4. The app displays:
   - Your BMI value
   - Your weight category (Underweight, Normal, Overweight)
   - A brief interpretation message
   - A resized character image that adjusts height visually

---

## Technologies Used

- **Python 3**
- **Tkinter** – Standard GUI library
- **CustomTkinter** – Enhanced styling and components
- **Pillow (PIL)** – Image processing and resizing
- **dark-title-bar** – Darkens the title bar on Windows for consistency

---

## Installation

1. Clone the repository:
   git clone https://github.com/ABooD125141/BMI-al-shola.git

2. Navigate to the project directory:
   cd BMI-al-shola

3. Install required libraries:
   pip install customtkinter pillow dark-title-bar

4. Run the app:
   python main.py

Make sure you have a folder named `Images` that contains the following files:
- icon.png
- BMI (2).png
- man.png
- info.png

---

## BMI Classification

| Category       | BMI Range     |
|----------------|---------------|
| Underweight    | ≤ 18.5        |
| Normal weight  | 18.5 – 25     |
| Overweight     | > 25          |

Note: Interpretation text is customized based on selected gender.

---

## About

This project was created as a beginner-friendly GUI practice project using Python and Tkinter, with a focus on interface design, image manipulation, and logic structuring.

Created by: **Abdulrahman F. Mubarak**

GitHub Repo:  
https://github.com/ABooD125141/BMI-al-shola

---

## License

This project is open-source and available under the MIT License.
