import pandas as pd

# Function to read Excel data and ensure Date column is in datetime format
def read_excel_data(file_path):
    try:
        df = pd.read_excel(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return None

# Function to perform monthly sales analysis of each branch
def monthly_sales_analysis(df):
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_sales = df.groupby(['Branch', 'Month'])['Daily_Sales'].sum().reset_index()
    print("\nMonthly Sales Analysis of Each Branch:")
    print(monthly_sales)

# Function to perform price analysis of each product
def price_analysis(df):
    avg_price = df.groupby('Product')['Price'].mean().reset_index()
    print("\nPrice Analysis of Each Product:")
    print(avg_price)

# Function to perform weekly sales analysis of the supermarket network
def weekly_sales_analysis(df):
    df['Week'] = df['Date'].dt.to_period('W')
    weekly_sales = df.groupby(['Branch', 'Week'])['Daily_Sales'].sum().reset_index()
    print("\nWeekly Sales Analysis of Supermarket Network:")
    print(weekly_sales)

# Function to analyze product preferences based on sales
def product_preference_analysis(df):
    product_preference = df.groupby('Product')['Daily_Sales'].sum().reset_index().sort_values(by='Daily_Sales', ascending=False)
    print("\nProduct Preference Analysis:")
    print(product_preference)

# Function to analyze the distribution of total sales amount of purchases
def sales_distribution_analysis(df):
    distribution = df['Total_Amount'].describe()
    print("\nAnalysis of Distribution of Total Sales Amount of Purchases:")
    print(distribution)

# New function to analyze yearly sales trends of each branch
def yearly_sales_analysis(df):
    df['Year'] = df['Date'].dt.to_period('Y')
    yearly_sales = df.groupby(['Branch', 'Year'])['Daily_Sales'].sum().reset_index()
    print("\nYearly Sales Trends of Each Branch:")
    print(yearly_sales)

# Main function to handle user input and trigger analysis functions
def main():
    file_path = "D:\\HND\\Semi 4\\APDP\\details samples.xlsx"  # Specify your file path here
    sales_data = read_excel_data(file_path)
    if sales_data is None:
        return

    while True:
        print("\nWelcome to Sampath Food City Sales Data Analysis System")
        print("1. Monthly Sales Analysis of Each Branch")
        print("2. Price Analysis of Each Product")
        print("3. Weekly Sales Analysis of Supermarket Network")
        print("4. Product Preference Analysis")
        print("5. Analysis of Distribution of Total Sales Amount of Purchases")
        print("6. Yearly Sales Trends of Each Branch")
        print("7. Exit")
        
        choice = input("Please enter your choice (1-7): ")
        
        if choice == '1':
            monthly_sales_analysis(sales_data)
        elif choice == '2':
            price_analysis(sales_data)
        elif choice == '3':
            weekly_sales_analysis(sales_data)
        elif choice == '4':
            product_preference_analysis(sales_data)
        elif choice == '5':
            sales_distribution_analysis(sales_data)
        elif choice == '6':
            yearly_sales_analysis(sales_data)
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
