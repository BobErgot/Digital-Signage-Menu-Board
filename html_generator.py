import os
import csv
import webbrowser
import pandas as pd
from bs4 import BeautifulSoup


def sort_csv(input_file_path: str):
    """
    Sorts a CSV file first by 'Flag' (prioritizing 'v'), then by 'Price', and finally by 'Sandwich_Name'.

    Parameters:
    - input_file_path: Path to the input CSV file.

    Returns:
    - Sorted DataFrame.
    """
    df = pd.read_csv(input_file_path)
    # Ensure all 'Flag' values are strings and handle NaN
    df['Flag'] = df['Flag'].fillna('').apply(str)
    # Create a temporary sort key that puts 'v' at the top and then sorts by 'Price' and 'Sandwich_Name'
    df['Sort_Flag'] = df['Flag'].apply(lambda x: 0 if x.lower() == 'v' else 1)
    sorted_df = df.sort_values(['Sort_Flag', 'Price', 'Sandwich_Name'], ascending=[True, True, True])
    # Drop the temporary 'Sort_Flag' column as it's no longer needed
    sorted_df.drop('Sort_Flag', axis=1, inplace=True)
    return sorted_df


def read_sorted_menu(df):
    """
    Organizes menu items into lists based on the Menu_Index value from a DataFrame.

    Parameters:
    - df: DataFrame containing the menu data.

    Returns:
    - Tuple of two lists containing menu items for menu 1 and menu 2 respectively.
    """
    menu_1_list, menu_2_list = [], []
    for index, row in df.iterrows():
        item = [row['Sandwich_Name'], row['Ingredients'], str(row['Menu_Index']), str(row['Price']), str(row['Flag']).lower()]
        if row['Menu_Index'] == 1:
            menu_1_list.append(item)
        elif row['Menu_Index'] == 2:
            menu_2_list.append(item)
    return menu_1_list, menu_2_list


def append_menu_items(menu_list, soup):
    """
    Appends menu items to the provided BeautifulSoup object based on the menu list.

    Parameters:
    - menu_list: List of menu items to be added.
    - soup: BeautifulSoup object where the menu items will be added.
    """
    for item in menu_list:
        new_item = soup.new_tag("div", **{"class": "itemWrap"})
        item_name_wrap = soup.new_tag("div", **{"class": "itemNameWrap"})
        new_item.append(item_name_wrap)

        # Determining item style based on vegetarian status
        item_name_class = "itemName vegetarian" if item[4].lower() == 'v' else "itemName"
        item_name = soup.new_tag("span", **{"class": item_name_class})
        item_name.string = item[0]
        item_name_wrap.append(item_name)

        item_middle = soup.new_tag("span", **{"class": "itemMiddle"})
        item_name_wrap.append(item_middle)

        item_price = soup.new_tag("span", **{"class": "itemPrice"})
        item_price.string = item[3]
        item_name_wrap.append(item_price)

        item_description = soup.new_tag("span", **{"class": "itemDescription"})
        item_description.string = item[1]
        new_item.append(item_description)

        soup.div.append(new_item)


def create_and_display_html(menu_list, template_path, output_path):
    """
    Creates an HTML file for a menu list using a base template and opens it in a web browser.

    Parameters:
    - menu_list: List of menu items to be added to the HTML file.
    - template_path: Path to the HTML template file.
    - output_path: Path where the generated HTML file will be saved.
    """
    with open(template_path) as base_file:
        soup = BeautifulSoup(base_file, 'html.parser')
    append_menu_items(menu_list, soup)
    with open(output_path, "w") as output_file:
        output_file.write(soup.prettify())
    webbrowser.open_new(f'file://{os.path.realpath(output_path)}')


# Main flow
if __name__ == "__main__":
    input_csv = 'menu/menu.csv'
    sorted_df = sort_csv(input_csv)

    menu_1_list, menu_2_list = read_sorted_menu(sorted_df)

    create_and_display_html(menu_1_list, "template/index.html", "output/menu_1.html")
    create_and_display_html(menu_2_list, "template/index.html", "output/menu_2.html")
