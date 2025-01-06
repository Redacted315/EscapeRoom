# Login System Documentation

## Overview
This document explains the structure and functionality of the updated `login.py` script, which implements a GUI-based login system. It includes a numeric keypad, CAPTCHA verification, audio feedback, and a success GIF animation.

---

## Code Structure
This script is organized around the `Login` class. The `test` function has been commented out but can be re-enabled for testing.

### File Structure
The script expects assets to be organized as follows:
```
assets/
  images/
    captcha.png
    reset.png
    enter.png
  audio/
    wrong.mp3
    right.mp3
  animations/
    login.gif
```
Ensure that these files are present and correctly referenced in the script.

---

## Class: `Login`
This class defines the graphical user interface, user interaction, and overall application logic.

### Constructor
```python
__init__(self, gif_fps)
```
#### Parameters:
- `gif_fps` (int): Frames per second for the GIF animation playback.

#### Initialization:
- Configures the main window dimensions and appearance.
- Loads required assets (CAPTCHA image, button icons, and audio).
- Sets up the numeric keypad and digit display.

### Key Methods
#### `display_gif(self)`
- Plays the GIF animation in a loop.
- Ends the application after two full loops.

#### `enter_number(self, b)`
- Updates the digit display with the input number (`b`).
- Supports a three-digit input limit.

#### `clear_nums(self)`
- Resets all digit fields to their default value (`_`).

#### `submit(self)`
- Validates the entered digits against the hardcoded passcode (`458`).
- Plays success or error audio feedback.
- If successful, displays the success GIF animation.

---

## Dependencies
### Libraries
- `tkinter`: GUI creation.
- `pygame.mixer`: Audio playback.

### Assets
- **Images**: CAPTCHA (`captcha.png`), Reset and Enter buttons (`reset.png`, `enter.png`).
- **Audio**: Feedback sounds (`wrong.mp3`, `right.mp3`).
- **GIF**: Success animation (`login.gif`).

---

## Setup and Usage
1. Install dependencies:
   ```bash
   pip install pygame
   ```
2. Verify the asset paths and ensure all required files are present.
3. Uncomment the `test` function and the corresponding `__main__` block for testing:
   ```python
   def test():
       A = Login(15)

   if __name__ == "__main__":
       test()
   ```
4. Run the script:
   ```bash
   python login.py
   ```

---

## Updating the GIF
To replace the success animation GIF:
1. **Replace the GIF File**:
   - Place the new GIF in the `assets/animations/` directory.
   - Update the `self.gif_file` value in the constructor to the new file path.

2. **Update the Frame Count**:
   - Determine the number of frames in the new GIF (use an image editor or library like `Pillow` to count frames).
   - Update the `frameCnt` value in the `display_gif` method:
     ```python
     frameCnt = <number_of_frames>
     ```

3. **Adjust the `gif_fps` Parameter**:
   - Set the `gif_fps` parameter in the constructor to match the desired playback speed.

4. **Test the GIF**:
   - Run the script to ensure the new animation displays correctly.

---

## Modifications and Tips

### Changing the Passcode
To modify the passcode:
1. Locate the `submit` method in the `Login` class.
2. Replace `458` with your desired passcode:
   ```python
   if self.digit_1["text"] != "<digit1>" or self.digit_2["text"] != "<digit2>" or self.digit_3["text"] != "<digit3>":
   ```

### Adjusting the Window Size
- Modify `window_width` and `window_height` in the constructor.

### Adding More Input Digits
1. Update the `digit_frame` setup to include additional labels.
2. Adjust the `enter_number` and `clear_nums` methods to handle extra digits.
3. Update the `submit` method to validate the extended passcode.

### Replacing Assets
- Replace the existing image and audio files in the `assets/` directory.
- Update the file paths in the constructor.

### Enhancing Security
- Avoid hardcoding passcodes in the script.
- Use environment variables or an external configuration file for sensitive data.

---
