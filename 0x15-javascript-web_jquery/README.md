# JavaScript Tasks README

## Overview

This repository contains JavaScript tasks that interact with HTML elements and APIs to perform various actions. The scripts are designed to be used with HTML files provided in the repository. Each script uses jQuery to handle DOM manipulation and events.

## Tasks

### 1. Update Header Text Color

**File:** `100-script.js`

**Description:** This script updates the text color of the `<header>` element to red (`#FF0000`) when the script is loaded. The script uses `document.querySelector` to select the HTML tag.

**HTML File:** `100-main.html`

**Usage:**

- The script is automatically executed when the HTML file is loaded.
- The header text color will change to red.

### 2. Add, Remove, and Clear List Items

**File:** `101-script.js`

**Description:** This script manages the `<ul>` list by adding, removing, and clearing list items based on user interactions:

- Adds a new `<li>Item</li>` to the list when the user clicks on `DIV#add_item`.
- Removes the last `<li>` element from the list when the user clicks on `DIV#remove_item`.
- Clears all `<li>` elements from the list when the user clicks on `DIV#clear_list`.

**HTML File:** `101-main.html`

**Usage:**

- Click on "Add item" to add a new item to the list.
- Click on "Remove item" to remove the last item from the list.
- Click on "Clear list" to remove all items from the list.

### 3. Fetch and Display "Hello" Translation

**File:** `102-script.js`

**Description:** This script fetches the translation of "Hello" from the API based on the language code entered by the user. The translation is displayed in `DIV#hello` when the user clicks on `INPUT#btn_translate` or presses Enter in `INPUT#language_code`.

**HTML File:** `102-main.html`

**Usage:**

- Enter a language code into the input field.
- Click "Translate" or press Enter to fetch and display the translation in `DIV#hello`.

### 4. Fetch and Display "Hello" with Enter Key Handling

**File:** `103-script.js`

**Description:** This script extends the previous task by also handling the Enter key press when the input field is focused. The translation is fetched and displayed in `DIV#hello` when the user clicks on `INPUT#btn_translate` or presses Enter.

**HTML File:** `103-main.html`

**Usage:**

- Enter a language code into the input field.
- Click "Translate" or press Enter to fetch and display the translation in `DIV#hello`.

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Open the HTML files in a web browser to test the functionality.**

3. **Ensure that the jQuery library is correctly included in the HTML files, as the scripts depend on it.**

## Dependencies

- jQuery (version 3.2.1 or later)

**Scripts are designed to be included in the `<head>` tag of the HTML files. Ensure that the paths to the script files are correct in the HTML files.**

## Contributing

If you find any issues or have suggestions for improvements, please submit a pull request or open an issue.
