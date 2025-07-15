# How to Use the Coffee Sales Predictive Model

This usage guide will help you run the coffee sales predictive model. You will download the project, run the Python script, and view results using Power BI.

---

## Steps

1. **Download the project**  
   Click the green **“Code”** button at the top right of the repository, then select **“Download ZIP”**.

2. **Extract the ZIP file**  
   Unzip the downloaded folder to a location on your computer.

3. **Open the project in your Python editor**  
   Use an editor like **PyCharm**, **VS Code**, or **Jupyter Notebook** to open the extracted folder.

4. **Install the required packages**  
  Open the `requirements.txt` file located inside the `coffee_sales_prediction_model` folder and make sure you have the requiered packages installed.

5. **Run the model script**  
   Open and run the `model_training.py` file located in the `scripts/` folder.  
   This will generate two CSV files:
   - `predicted_sales.csv`
   - `model_metrics.csv`  

   Both files will be saved inside the `output/` folder.

7. **Open the Power BI dashboard**  
   Launch **Power BI Desktop** and open the file `coffee_sales_dashboard.pbix`.

8. **Refresh the data**  
   Click **“Refresh”** to load the latest results from the `output/` folder.  
   If refresh fails, manually connect the two CSV files:
     - Click **“Get Data” > “Text/CSV”**
     - Locate and select `predicted_sales.csv` and `model_metrics.csv` from the `output/` folder
