# Define a data frame grouped by gender, all values
gender_grp_df = pd.DataFrame({"Gender"})
gender_grp_df = purch_data.groupby(["Gender"])
gender_grp_df.head()
# Create purchase count column
#pa_gender_df = gender_grp_df.loc[:,["Purchase ID"]]
#pa_gender_df = gender_grp_df["Purchase ID"].count()
#pa_gender_df = pa_gender_df.rename(columns={"Purchase ID" : "Purchase Count"})

# Create average purchase price
#pa_gender_df["Average Purchase Price"] = 

#pa_gender_df



# POSSIBLE code for GENDER DEMOS section
grouped_gender_df = purch_data.groupby(["Gender", "SN"])
grouped_gender_df.count()