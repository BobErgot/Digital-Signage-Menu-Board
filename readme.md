# Digital Signage Menu Board

The Digital Signage Menu Board project is designed to automate the process of displaying menu items for restaurants, cafes, or any food service establishments on digital screens. Utilizing Python, Pandas for data manipulation, BeautifulSoup for HTML parsing, and web technologies, it reads menu data from a CSV file, sorts and organizes this information, then generates and displays it in an aesthetically pleasing format on a digital menu board.

An insightful exploration of the UI/UX design process for a digital menu case-study can be found at [The Deli Dilemma: Perspective on Menu Accessibility and Customer Experience](https://bobbydoshi.com/uiux-deli-menu-redesign/), providing a rich context for understanding the visual and functional aspects of digital menu design.

## Features

- **CSV Menu Sorting:** Sorts menu items based on flags (with priority to vegetarian options), price, and name.
- **Menu Organization:** Dynamically organizes menu items into different sections or pages.
- **HTML Menu Generation:** Creates an HTML-based digital menu from a template, populating it with the sorted and organized menu data.
- **Automated Display:** Automatically opens and displays the generated digital menu in a web browser, making it ready to be displayed on a digital signage screen.

## Setup

### Requirements

- Python 3.x
- Pandas
- BeautifulSoup4

To install the necessary Python packages, run:

```bash
pip install requirements.txt
```

### Installation
Clone the project repository to your local machine:

```bash
git clone <repository-url>
cd Digital-Signage-Menu-Board
```

### Configuring Your Menu

1. **Prepare Your CSV File:** Format your menu data in a CSV file with the columns `Sandwich_Name`, `Ingredients`, `Menu_Index`, `Price`, and `Flag` (where `v` indicates a vegetarian option). Save this file as `menu/menu.csv`.

2. **HTML Template:** Ensure you have an HTML template named `index.html` in the `template` folder. This template should contain the basic structure of your menu board, where the menu items will be injected.

## Usage

To generate and display the digital menus, run the main script from the project directory:

```bash
python html_generator.py
```

This will read the menu data from `menu/menu.csv`, sort and organize the items, generate HTML files for each menu section, and automatically open these files in your default web browser.

## Customization

- **Menu CSV:** You can update the `menu/menu.csv` file to change the menu items as needed. This allows for easy menu updates and customization without needing to alter the code.

- **HTML Template:** Modify the `template/index.html` to change the design and layout of your digital menu board. The template should be structured to dynamically accommodate the injected menu items. This flexibility lets you adjust the appearance of your menu board to match your branding or decor.
