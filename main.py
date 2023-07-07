import pandas as pd

# Read the Excel file
file_path = r"C:\Users\liamh\OneDrive\Desktop\Combined Data - 1.4.21 to Present.xlsx"
df = pd.read_excel(file_path)

# Remove specified columns
columns_to_remove = ['Hi', 'Low', 'Back Odd', 'Lay Odd', 'Weight Diff', 'WFF', 'FAV Rank']
df = df.drop(columns=columns_to_remove)

# Remove South Africa from the Country list
df = df[df['Country'] != 'South Africa']

# Save the modified DataFrame to a new Excel file in the Downloads folder
output_file_path = r"C:\Users\liamh\Downloads\Modified_Data.xlsx"
df.to_excel(output_file_path, index=False)

print("Modified DataFrame saved successfully.")
import pandas as pd

# Define the file path
file_path = r'C:\Users\liamh\Downloads\Modified_Data.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Change the "Date" format to "dd/mm/yyyy"
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d').dt.strftime('%d/%m/%Y')

# Drop the specified columns
columns_to_drop = ['Form', 'Last Form', 'Date Last Run', 'Beaten Favourite',
                   'Course Winner', 'Distance Winner', 'Course & Distance Winner',
                   'RDB Rating', 'ISP', 'RDB Rank', 'Distance From Winner', 'Improving Horse']
df = df.drop(columns=columns_to_drop)

# Save the modified DataFrame back to the Excel file
df.to_excel(file_path, index=False)
