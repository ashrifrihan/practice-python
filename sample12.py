import pandas as pd

class SalesData:
    def __init__(self, data_path="sales_data.csv"):
        """
        Initializes the SalesData class by loading sales data from a CSV file.

        Args:
            data_path (str): Path to the CSV file containing sales data. Defaults to "sales_data.csv".
        """
        try:
            self.df = pd.read_csv(data_path)
        except FileNotFoundError:
            print("Error: Sales data file not found. Please provide a valid path.")
            self.df = pd.DataFrame()  # Empty DataFrame if file is not found

    def get_data(self):
        """
        Returns the sales data as a Pandas DataFrame.

        Returns:
            pd.DataFrame: The sales data DataFrame.
        """
        return self.df

    def add_data(self, new_data):
        """
        Appends new sales data to the existing DataFrame.

        Args:
            new_data (dict): A dictionary representing new sales data, with keys matching the DataFrame columns.
        """
        self.df = self.df.append(new_data, ignore_index=True)

    def save_data(self, path="sales_data.csv"):
        """
        Saves the updated sales data to a CSV file.

        Args:
            path (str): Path to the CSV file to save the data. Defaults to "sales_data.csv".
        """
        self.df.to_csv(path, index=False)

import pandas as pd

class MonthlySalesAnalysis:
    def __init__(self, sales_data):
        self.sales_data = sales_data

    def analyze_monthly_sales(self, branch_name=None):
        """
        Analyzes monthly sales for a specific branch or all branches.

        Args:
            branch_name (str, optional): Name of the branch to analyze. Defaults to None (all branches).

        Returns:
            pd.DataFrame: DataFrame with monthly sales for the specified branch(es).
        """
        df = self.sales_data.get_data()
        if branch_name:
            df = df[df["Branch"] == branch_name]
        monthly_sales = df.groupby(pd.Grouper(key='Date', freq='M'))["Total Amount"].sum()
        return monthly_sales

    def print_monthly_sales(self, branch_name=None):
        """
        Prints a formatted summary of monthly sales.

        Args:
            branch_name (str, optional): Name of the branch to analyze. Defaults to None (all branches).
        """
        monthly_sales = self.analyze_monthly_sales(branch_name)
        print(f"Monthly Sales {'(All Branches)' if branch_name is None else f'({branch_name})'}:")
        print(monthly_sales)

import pandas as pd

class PriceAnalysis:
    def __init__(self, sales_data):
        self.sales_data = sales_data

    def analyze_product_prices(self, product_name):
        """
        Analyzes price changes for a specific product.

        Args:
            product_name (str): Name of the product to analyze.

        Returns:
            pd.DataFrame: DataFrame with price changes for the product.
        """
        df = self.sales_data.get_data()
        product_df = df[df["Product"] == product_name]
        return product_df[["Date", "Price"]]

    def print_price_analysis(self, product_name):
        """
        Prints a formatted summary of product price changes.

        Args:
            product_name (str): Name of the product to analyze.
        """
        price_changes = self.analyze_product_prices(product_name)
        print(f"Price Analysis for {product_name}:")
        print(price_changes)

import pandas as pd

class WeeklySalesAnalysis:
    def __init__(self, sales_data):
        self.sales_data = sales_data

    def analyze_weekly_sales(self):
        """
        Analyzes weekly sales for the entire supermarket network.

        Returns:
            pd.DataFrame: DataFrame with weekly sales totals.
        """
        df = self.sales_data.get_data()
        weekly_sales = df.groupby(pd.Grouper(key='Date', freq='W'))["Total Amount"].sum()
        return weekly_sales

    def print_weekly_sales(self):
        """
        Prints a formatted summary of weekly sales.
        """
        weekly_sales = self.analyze_weekly_sales()
        print("Weekly Sales (All Branches):")
        print(weekly_sales)

import pandas as pd

class ProductPreferenceAnalysis:
    def __init__(self, sales_data):
        self.sales_data = sales_data

    def analyze_product_preferences(self):
        """
        Analyzes product preferences based on sales quantity.

        Returns:
            pd.DataFrame: DataFrame with product preferences ranked by total quantity sold.
        """
        df = self.sales_data.get_data()
        product_preferences = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
        return product_preferences

    def print_product_preferences(self):
        """
        Prints a formatted summary of product preferences.
        """
        product_preferences = self.analyze_product_preferences()
        print("Product Preferences (Top Sellers):")
        print(product_preferences)

import pandas as pd

class SalesDistributionAnalysis:
    def __init__(self, sales_data):
        self.sales_data = sales_data

    def analyze_sales_distribution(self, bins=10):
        """
        Analyzes the distribution of total sales amounts.

        Args:
            bins (int, optional): Number of bins for the distribution analysis. Defaults to 10.

        Returns:
            pd.DataFrame: DataFrame with sales amount distribution statistics.
        """
        df = self.sales_data.get_data()
        sales_distribution = pd.cut(df["Total Amount"], bins=bins)
        return sales_distribution.value_counts()

    def print_sales_distribution(self, bins=10):
        """
        Prints a formatted summary of the sales amount distribution.

        Args:
            bins (int, optional): Number of bins for the distribution analysis. Defaults to 10.
        """
        sales_distribution = self.analyze_sales_distribution(bins)
        print("Sales Amount Distribution:")
        print(sales_distribution)

import argparse
from models.sales_data import SalesData
from analysis import MonthlySalesAnalysis, PriceAnalysis, WeeklySalesAnalysis, ProductPreferenceAnalysis, SalesDistributionAnalysis

def main():
    parser = argparse.ArgumentParser(description="Sales Data Analysis System")
    parser.add_argument("data_path", type=str, help="Path to the CSV file containing sales data")

    args = parser.parse_args()
    sales_data = SalesData(args.data_path)

    while True:
        print("\nSelect an analysis option:")
        print("1. Monthly Sales Analysis")
        print("2. Price Analysis")
        print("3. Weekly Sales Analysis")
        print("4. Product Preference Analysis")
        print("5. Sales Distribution Analysis")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            branch_name = input("Enter branch name (or leave blank for all branches): ")
            MonthlySalesAnalysis(sales_data).print_monthly_sales(branch_name)
        elif choice == "2":
            product_name = input("Enter product name: ")
            PriceAnalysis(sales_data).print_price_analysis(product_name)
        elif choice == "3":
            WeeklySalesAnalysis(sales_data).print_weekly_sales()
        elif choice == "4":
            ProductPreferenceAnalysis(sales_data).print_product_preferences()
        elif choice == "5":
            bins = int(input("Enter number of bins for sales distribution analysis (default 10): "))
            SalesDistributionAnalysis(sales_data).print_sales_distribution(bins)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
